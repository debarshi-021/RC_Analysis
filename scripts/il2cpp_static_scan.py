#!/usr/bin/env python3
"""Static scanner for IL2CPP dummy DLL metadata.

Produces JSON/Markdown/DOT reports for architecture research. It does not patch,
hook, bypass anti-cheat, or modify runtime behavior.
"""
from __future__ import annotations

import argparse, json, re, struct
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

TABLES = {
    0:'Module',1:'TypeRef',2:'TypeDef',4:'Field',6:'MethodDef',8:'Param',9:'InterfaceImpl',10:'MemberRef',
    11:'Constant',12:'CustomAttribute',13:'FieldMarshal',14:'DeclSecurity',15:'ClassLayout',16:'FieldLayout',
    17:'StandAloneSig',18:'EventMap',20:'Event',21:'PropertyMap',23:'Property',24:'MethodSemantics',
    25:'MethodImpl',26:'ModuleRef',27:'TypeSpec',28:'ImplMap',29:'FieldRVA',32:'Assembly',35:'AssemblyRef',
    38:'File',39:'ExportedType',40:'ManifestResource',41:'NestedClass',42:'GenericParam',43:'MethodSpec',44:'GenericParamConstraint'
}
TABLE_ID = {v:k for k,v in TABLES.items()}
CODED = {
    'TypeDefOrRef': (2, ['TypeDef','TypeRef','TypeSpec']),
    'HasConstant': (2, ['Field','Param','Property']),
    'HasCustomAttribute': (5, ['MethodDef','Field','TypeRef','TypeDef','Param','InterfaceImpl','MemberRef','Module','DeclSecurity','Property','Event','StandAloneSig','ModuleRef','TypeSpec','Assembly','AssemblyRef','File','ExportedType','ManifestResource','GenericParam','GenericParamConstraint','MethodSpec']),
    'HasFieldMarshal': (1, ['Field','Param']),
    'HasDeclSecurity': (2, ['TypeDef','MethodDef','Assembly']),
    'MemberRefParent': (3, ['TypeDef','TypeRef','ModuleRef','MethodDef','TypeSpec']),
    'HasSemantics': (1, ['Event','Property']),
    'MethodDefOrRef': (1, ['MethodDef','MemberRef']),
    'MemberForwarded': (1, ['Field','MethodDef']),
    'Implementation': (2, ['File','AssemblyRef','ExportedType']),
    'CustomAttributeType': (3, [None,None,'MethodDef','MemberRef',None]),
    'ResolutionScope': (2, ['Module','ModuleRef','AssemblyRef','TypeRef']),
    'TypeOrMethodDef': (1, ['TypeDef','MethodDef']),
}
ELEM = {0x02:'bool',0x03:'char',0x04:'sbyte',0x05:'byte',0x06:'short',0x07:'ushort',0x08:'int',0x09:'uint',0x0a:'long',0x0b:'ulong',0x0c:'float',0x0d:'double',0x0e:'string',0x18:'IntPtr',0x19:'UIntPtr',0x1c:'object'}
INTEREST_TERMS = [
    'timing','batting','batsman','bat','shot','meter','input','animation','anim','frame','ai','probab',
    'difficulty','gameplay','touch','swipe','joystick','obscured','anticheat','actk','ball','bowler'
]
FOCUS_TERMS = ['PerfectTimingManipulation','BatTimingManipulation','BattingTiming','ShotTiming','BATTING_TIMING_METER','CalculateTimingMeterParameters','TimingMeter','GetAIShotTiming','get_PlayerBattingTiming','GameDataReader','AITimingProbabilities','CaptureFrameTimings']

@dataclass
class Method:
    name: str; rva: int; flags: int; sig: int; params: list[str] = field(default_factory=list); ret: str|None=None
@dataclass
class FieldInfo:
    name: str; sig: int; type_name: str|None=None
@dataclass
class TypeInfo:
    token: int; namespace: str; name: str; extends: str|None; fields: list[FieldInfo]; methods: list[Method]; nested_in: str|None=None
    @property
    def full(self): return f"{self.namespace}.{self.name}" if self.namespace else self.name

class PE:
    def __init__(self, data: bytes):
        self.data=data; self.sections=[]; self._parse()
    def u16(self,o): return struct.unpack_from('<H', self.data, o)[0]
    def u32(self,o): return struct.unpack_from('<I', self.data, o)[0]
    def _parse(self):
        pe=self.u32(0x3c); assert self.data[pe:pe+4]==b'PE\0\0'
        nsec=self.u16(pe+6); opt_size=self.u16(pe+20); opt=pe+24; magic=self.u16(opt)
        dd=opt+(112 if magic==0x20b else 96)
        self.cli_rva=self.u32(dd+14*8); self.cli_size=self.u32(dd+14*8+4)
        sec=opt+opt_size
        for i in range(nsec):
            off=sec+i*40; name=self.data[off:off+8].split(b'\0')[0].decode('ascii','ignore')
            vsz=self.u32(off+8); va=self.u32(off+12); rawsz=self.u32(off+16); rawptr=self.u32(off+20)
            self.sections.append((va, max(vsz,rawsz), rawptr, name))
    def rva_to_off(self,rva:int)->int:
        for va,sz,raw,name in self.sections:
            if va <= rva < va+sz: return raw+(rva-va)
        raise ValueError(f'RVA 0x{rva:x} not mapped')

class Metadata:
    def __init__(self, path: Path):
        self.path=path; self.data=path.read_bytes(); self.pe=PE(self.data); self.types=[]; self.rows={}; self.table_offsets={}; self.streams={}
        cli=self.pe.rva_to_off(self.pe.cli_rva); md_rva=struct.unpack_from('<I', self.data, cli+8)[0]
        self.md_off=self.pe.rva_to_off(md_rva); self._parse_root(); self._parse_tables(); self._build_types()
    def _parse_root(self):
        d=self.data; o=self.md_off
        assert d[o:o+4]==b'BSJB'; ver_len=struct.unpack_from('<I',d,o+12)[0]; p=o+16+ver_len; p=(p+3)&~3; p+=2
        n=struct.unpack_from('<H',d,p)[0]; p+=2
        for _ in range(n):
            off,sz=struct.unpack_from('<II',d,p); p+=8; end=d.index(b'\0',p); name=d[p:end].decode('ascii','ignore'); p=(end+4)&~3
            self.streams[name]=(self.md_off+off, sz)
        self.str_off,self.str_sz=self.streams.get('#Strings',(0,0)); self.blob_off,self.blob_sz=self.streams.get('#Blob',(0,0))
    def s(self, idx:int)->str:
        if idx==0: return ''
        off=self.str_off+idx; end=self.data.find(b'\0', off, self.str_off+self.str_sz)
        return self.data[off:end].decode('utf-8','replace') if end!=-1 else ''
    def blob(self, idx:int)->bytes:
        if idx==0: return b''
        o=self.blob_off+idx; n,adv=self._cu(o); return self.data[o+adv:o+adv+n]
    def _cu(self,o:int):
        b=self.data[o]
        if b & 0x80 == 0: return b,1
        if b & 0xC0 == 0x80: return ((b&0x3f)<<8)|self.data[o+1],2
        return ((b&0x1f)<<24)|(self.data[o+1]<<16)|(self.data[o+2]<<8)|self.data[o+3],4
    def _parse_tables(self):
        off,sz=self.streams.get('#~') or self.streams.get('#-')
        d=self.data; p=off+6; self.heap_sizes=d[p]; p+=2
        valid=struct.unpack_from('<Q',d,p)[0]; p+=16
        present=[i for i in range(64) if (valid>>i)&1]
        for i in present: self.rows[i]=struct.unpack_from('<I',d,p)[0]; p+=4
        self.idx_size=lambda t: 4 if self.rows.get(TABLE_ID[t],0) >= 65536 else 2
        self.str_i=4 if self.heap_sizes&1 else 2; self.guid_i=4 if self.heap_sizes&2 else 2; self.blob_i=4 if self.heap_sizes&4 else 2
        for i in present:
            self.table_offsets[i]=p; p += self._row_size(i)*self.rows[i]
    def coded_size(self,name):
        bits,tabs=CODED[name]; maxrows=max(self.rows.get(TABLE_ID[t],0) for t in tabs if t)
        return 4 if maxrows >= (1 << (16-bits)) else 2
    def _sz(self, kind):
        if kind=='str': return self.str_i
        if kind=='guid': return self.guid_i
        if kind=='blob': return self.blob_i
        if kind in TABLE_ID: return self.idx_size(kind)
        if kind in CODED: return self.coded_size(kind)
        return kind
    def _cols(self, tid):
        return {
            0:[2,'str','guid','guid','guid'], 1:['ResolutionScope','str','str'], 2:[4,'str','str','TypeDefOrRef','Field','MethodDef'],
            4:[2,'str','blob'], 6:[4,2,2,'str','blob','Param'], 8:[2,2,'str'], 9:['TypeDef','TypeDefOrRef'],
            10:['MemberRefParent','str','blob'], 11:[2,'HasConstant','blob'], 12:['HasCustomAttribute','CustomAttributeType','blob'],
            13:['HasFieldMarshal','blob'],14:[2,'HasDeclSecurity','blob'],15:[2,4,'TypeDef'],16:[4,'Field'],17:['blob'],
            18:['TypeDef','Event'],20:[2,'str','TypeDefOrRef'],21:['TypeDef','Property'],23:[2,'str','blob'],24:[2,'MethodDef','HasSemantics'],
            25:['TypeDef','MethodDefOrRef','MethodDefOrRef'],26:['str'],27:['blob'],28:[2,'MemberForwarded','str','ModuleRef'],29:[4,'Field'],
            32:[4,2,2,2,2,4,'blob','str','str'],35:[2,2,2,2,4,'blob','str','str','blob'],38:[4,'str','blob'],
            39:[4,4,'str','str','Implementation'],40:[4,4,'str','Implementation'],41:['TypeDef','TypeDef'],42:[2,2,'TypeOrMethodDef','str'],43:['MethodDefOrRef','blob'],44:['GenericParam','TypeDefOrRef']
        }.get(tid, [])
    def _row_size(self,tid): return sum(self._sz(c) for c in self._cols(tid))
    def row(self, tid, rid):
        if rid<1 or rid>self.rows.get(tid,0): return None
        p=self.table_offsets[tid]+(rid-1)*self._row_size(tid); vals=[]
        for c in self._cols(tid):
            s=self._sz(c); vals.append(int.from_bytes(self.data[p:p+s],'little')); p+=s
        return vals
    def decode_coded(self, name, val):
        bits,tabs=CODED[name]; tag=val & ((1<<bits)-1); rid=val>>bits
        if tag>=len(tabs) or not tabs[tag]: return None
        return tabs[tag], rid
    def type_ref_name(self, table, rid):
        if table=='TypeDef':
            r=self.row(2,rid); return (self.s(r[2])+'.' if self.s(r[2]) else '')+self.s(r[1]) if r else None
        if table=='TypeRef':
            r=self.row(1,rid); return (self.s(r[2])+'.' if self.s(r[2]) else '')+self.s(r[1]) if r else None
        if table=='TypeSpec': return 'TypeSpec'
        return None
    def parse_type_sig(self,b:bytes,pos=0):
        if pos>=len(b): return None,pos
        et=b[pos]; pos+=1
        if et in ELEM: return ELEM[et],pos
        if et in (0x11,0x12):
            val,adv=self._cu_from(b,pos); pos+=adv; dec=self.decode_coded('TypeDefOrRef', val); return (self.type_ref_name(*dec) if dec else 'type'),pos
        if et==0x1d:
            inner,pos=self.parse_type_sig(b,pos); return f'{inner}[]',pos
        if et==0x0f:
            inner,pos=self.parse_type_sig(b,pos); return f'{inner}&',pos
        if et==0x1f:
            inner,pos=self.parse_type_sig(b,pos); return f'{inner}*',pos
        if et==0x1b:
            base,pos=self.parse_type_sig(b,pos); argc,adv=self._cu_from(b,pos); pos+=adv
            args=[]
            for _ in range(argc):
                a,pos=self.parse_type_sig(b,pos); args.append(a or '?')
            return f'{base}<'+','.join(args)+'>',pos
        if et in (0x13,0x1e):
            num,adv=self._cu_from(b,pos); return f'!{num}',pos+adv
        return f'elem_0x{et:x}',pos
    def _cu_from(self,b,o):
        x=b[o]
        if x&0x80==0: return x,1
        if x&0xC0==0x80: return ((x&0x3f)<<8)|b[o+1],2
        return ((x&0x1f)<<24)|(b[o+1]<<16)|(b[o+2]<<8)|b[o+3],4
    def field_type(self, sig_idx):
        b=self.blob(sig_idx)
        if not b or b[0]!=0x06: return None
        t,_=self.parse_type_sig(b,1); return t
    def method_sig(self, sig_idx):
        b=self.blob(sig_idx)
        if not b: return None, []
        p=1
        if b[0] & 0x10: # generic
            _,adv=self._cu_from(b,p); p+=adv
        try:
            argc,adv=self._cu_from(b,p); p+=adv; ret,p=self.parse_type_sig(b,p); params=[]
            for _ in range(argc):
                t,p=self.parse_type_sig(b,p); params.append(t or '?')
            return ret,params
        except Exception:
            return None,[]
    def _build_types(self):
        n=self.rows.get(2,0); methods_n=self.rows.get(6,0); fields_n=self.rows.get(4,0)
        for rid in range(1,n+1):
            r=self.row(2,rid); next_r=self.row(2,rid+1) if rid<n else None
            f_start=r[4]; f_end=(next_r[4] if next_r else fields_n+1)
            m_start=r[5]; m_end=(next_r[5] if next_r else methods_n+1)
            ext_dec=self.decode_coded('TypeDefOrRef', r[3]); ext=self.type_ref_name(*ext_dec) if ext_dec else None
            fs=[]; ms=[]
            for frid in range(f_start, f_end):
                fr=self.row(4,frid); fs.append(FieldInfo(self.s(fr[1]), fr[2], self.field_type(fr[2])))
            for mrid in range(m_start, m_end):
                mr=self.row(6,mrid); ret,params=self.method_sig(mr[4]); ms.append(Method(self.s(mr[3]), mr[0], mr[2], mr[4], params, ret))
            self.types.append(TypeInfo(0x02000000|rid, self.s(r[2]), self.s(r[1]), ext, fs, ms))
        # nested class owners
        for rid in range(1,self.rows.get(41,0)+1):
            nested,enclosing=self.row(41,rid); 
            if 1 <= nested <= len(self.types) and 1 <= enclosing <= len(self.types): self.types[nested-1].nested_in=self.types[enclosing-1].full

def score_type(t: TypeInfo):
    blob=' '.join([t.full, t.extends or '', ' '.join(f.name+' '+(f.type_name or '') for f in t.fields), ' '.join(m.name for m in t.methods)]).lower()
    return sum(1 for term in INTEREST_TERMS if term in blob) + sum(3 for term in FOCUS_TERMS if term.lower() in blob)

def probable_role(t: TypeInfo):
    n=t.full.lower(); methods=' '.join(m.name.lower() for m in t.methods); fields=' '.join(f.name.lower() for f in t.fields)
    text=' '.join([n,methods,fields])
    roles=[]
    if 'monobehaviour' in (t.extends or '').lower(): roles.append('Unity MonoBehaviour component')
    if 'gamedatareader' in n or 'config' in text or 'probab' in text: roles.append('data/config reader or balancing table')
    if 'timingmeter' in text or 'meter' in n: roles.append('timing meter/UI parameter system')
    if 'battiming' in text or 'battiming' in n or 'battimingmanipulation' in text: roles.append('bat timing adjustment/model data')
    if 'perfecttiming' in text: roles.append('perfect timing data/model reference')
    if 'shot' in text: roles.append('shot selection/evaluation/animation')
    if 'input' in text or 'touch' in text or 'swipe' in text or 'joystick' in text: roles.append('input handling or control mapping')
    if 'anim' in text or 'animation' in text: roles.append('animation orchestration/timing')
    if 'ai' in text or 'batsman_ai' in text: roles.append('AI timing/shot probability')
    return '; '.join(dict.fromkeys(roles)) or 'name-correlated gameplay/support type'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('assembly', nargs='?', default='Assembly-CSharp.dll'); ap.add_argument('--out-dir', default='reports')
    args=ap.parse_args(); out=Path(args.out_dir); out.mkdir(exist_ok=True)
    md=Metadata(Path(args.assembly))
    interesting=[t for t in md.types if score_type(t)>0]
    focus=[t for t in md.types if any(term.lower() in (t.full+' '+' '.join(m.name for m in t.methods)+' '+' '.join(f.name for f in t.fields)).lower() for term in FOCUS_TERMS)]
    obscured=[]
    for t in md.types:
        hits=[{'field':f.name,'type':f.type_name} for f in t.fields if f.type_name and ('Obscured' in f.type_name or 'CodeStage' in f.type_name)]
        if hits: obscured.append({'type':t.full,'fields':hits})
    data={'assembly':args.assembly,'type_count':len(md.types),'interesting_count':len(interesting),
          'focus_types':[t.full for t in focus],
          'types':[{'name':t.name,'namespace':t.namespace,'full':t.full,'extends':t.extends,'nested_in':t.nested_in,'role':probable_role(t),
                    'fields':[{'name':f.name,'type':f.type_name} for f in t.fields if any(x in (f.name+' '+str(f.type_name)).lower() for x in INTEREST_TERMS) or (f.type_name and 'Obscured' in f.type_name)],
                    'methods':[{'name':m.name,'rva':hex(m.rva),'return':m.ret,'params':m.params} for m in t.methods if any(x in m.name.lower() for x in INTEREST_TERMS)]} for t in interesting],
          'obscured_fields':obscured}
    (out/'timing_scan.json').write_text(json.dumps(data,indent=2), encoding='utf-8')
    lines=['# IL2CPP Gameplay Timing Static Scan','',f'- Assembly: `{args.assembly}`',f'- Metadata TypeDef rows parsed: {len(md.types)}',f'- Timing/input/shot-correlated types: {len(interesting)}','','## Focus Type Matches']
    for t in focus: lines.append(f'- `{t.full}` extends `{t.extends}` — {probable_role(t)}')
    lines += ['', '## Correlated Types']
    for t in interesting[:500]:
        lines.append(f'### `{t.full}`')
        lines.append(f'- Extends: `{t.extends}`')
        if t.nested_in: lines.append(f'- Nested in: `{t.nested_in}`')
        lines.append(f'- Probable role: {probable_role(t)}')
        ms=[m for m in t.methods if any(x in m.name.lower() for x in INTEREST_TERMS)]
        fs=[f for f in t.fields if any(x in (f.name+" "+str(f.type_name)).lower() for x in INTEREST_TERMS) or (f.type_name and 'Obscured' in f.type_name)]
        if fs: lines.append('- Fields: '+', '.join(f'`{f.name}: {f.type_name}`' for f in fs[:30]))
        if ms: lines.append('- Methods: '+', '.join(f'`{m.name}` @ `{hex(m.rva)}`' for m in ms[:40]))
        lines.append('')
    lines += ['## ACTk / Obscured Field Uses']
    for item in obscured[:300]: lines.append(f'- `{item["type"]}`: '+', '.join(f'`{h["field"]}: {h["type"]}`' for h in item['fields']))
    (out/'timing_scan.md').write_text('\n'.join(lines), encoding='utf-8')
    # DOT graph based on extends, nested, and field type references among interesting types
    interesting_names={t.full for t in interesting}
    dot=['digraph GameplayTiming {','  rankdir=LR;','  node [shape=box, fontsize=10];']
    for t in interesting:
        dot.append(f'  "{t.full}" [label="{t.name}\n{probable_role(t)[:40]}"];')
        if t.extends and (any(x in t.extends.lower() for x in INTEREST_TERMS) or t.extends in interesting_names): dot.append(f'  "{t.full}" -> "{t.extends}" [label="extends"];')
        if t.nested_in: dot.append(f'  "{t.full}" -> "{t.nested_in}" [label="nested in"];')
        for f in t.fields:
            if f.type_name and (f.type_name in interesting_names or any(x in f.type_name.lower() for x in INTEREST_TERMS)):
                dot.append(f'  "{t.full}" -> "{f.type_name}" [label="field {f.name}"];')
    dot.append('}')
    (out/'timing_dependency_graph.dot').write_text('\n'.join(dot), encoding='utf-8')
    print(f'Wrote {out}/timing_scan.md, {out}/timing_scan.json, {out}/timing_dependency_graph.dot')

if __name__ == '__main__': main()
