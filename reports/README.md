# Generated analysis reports

These reports are produced by `scripts/il2cpp_static_scan.py` from the reconstructed `Assembly-CSharp.dll` dummy assembly.

- `timing_scan.md`: broad static scan of timing/input/shot/animation-correlated classes, fields, methods, and RVAs.
- `timing_scan.json`: machine-readable version of the scan for notebooks, dashboards, and graph tools.
- `timing_dependency_graph.dot`: Graphviz dependency graph based on inheritance, nesting, and field-type references.
- `architecture_findings.md`: curated research summary and hypotheses for the gameplay timing pipeline.

Regenerate with:

```bash
./scripts/il2cpp_static_scan.py Assembly-CSharp.dll --out-dir reports
```
