# IL2CPP Gameplay Timing Static Scan

- Assembly: `Assembly-CSharp.dll`
- Metadata TypeDef rows parsed: 6520
- Timing/input/shot-correlated types: 2490

## Focus Type Matches
- `PlayerSelectionBase` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component; AI timing/shot probability
- `InGamePanels` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component; timing meter/UI parameter system; shot selection/evaluation/animation; AI timing/shot probability
- `PlayerInAuction` extends `System.Object` — AI timing/shot probability
- `Ball` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component; data/config reader or balancing table; timing meter/UI parameter system; shot selection/evaluation/animation; animation orchestration/timing; AI timing/shot probability
- `ShotTiming` extends `System.Enum` — shot selection/evaluation/animation
- `BatsmanStats` extends `System.Object` — shot selection/evaluation/animation
- `FielderController` extends `FielderControllerBase` — animation orchestration/timing
- `PlayerDetails` extends `System.ValueType` — AI timing/shot probability
- `GameDataReader` extends `TypeSpec` — data/config reader or balancing table; timing meter/UI parameter system; shot selection/evaluation/animation; input handling or control mapping; animation orchestration/timing; AI timing/shot probability
- `GameDifficulty` extends `System.Object` — bat timing adjustment/model data; perfect timing data/model reference; AI timing/shot probability
- `GameDifficulty_New` extends `System.Object` — bat timing adjustment/model data; perfect timing data/model reference; AI timing/shot probability
- `GameDifficulty_New_Test` extends `System.Object` — bat timing adjustment/model data; perfect timing data/model reference; AI timing/shot probability
- `TimingMeter_ML` extends `System.Object` — timing meter/UI parameter system
- `TimingMeterMod_ML` extends `System.Object` — timing meter/UI parameter system; shot selection/evaluation/animation
- `<>c__DisplayClass445_0` extends `System.Object` — shot selection/evaluation/animation; AI timing/shot probability
- `<>c__DisplayClass446_0` extends `System.Object` — shot selection/evaluation/animation; AI timing/shot probability
- `<>c__DisplayClass464_0` extends `System.Object` — timing meter/UI parameter system; shot selection/evaluation/animation
- `BowlingTutorialData` extends `System.Object` — shot selection/evaluation/animation
- `TutorialState` extends `System.Enum` — shot selection/evaluation/animation; AI timing/shot probability
- `BattingTutorialUIHandler` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component; timing meter/UI parameter system; shot selection/evaluation/animation; input handling or control mapping; AI timing/shot probability
- `FielderThrowControls` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component; timing meter/UI parameter system
- `TimingMeterPercentages` extends `System.Object` — timing meter/UI parameter system
- `BattingSFXData` extends `System.Object` — shot selection/evaluation/animation
- `UIGameSetting` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component; timing meter/UI parameter system; AI timing/shot probability
- `SetFieldingType` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component
- `ButtonName` extends `System.Enum` — timing meter/UI parameter system; AI timing/shot probability
- `UISettings` extends `UnityEngine.MonoBehaviour` — Unity MonoBehaviour component; timing meter/UI parameter system; AI timing/shot probability
- `RC19.Utils.RankedProgressCalculator` extends `System.Object` — name-correlated gameplay/support type
- `RC19.UI.RankedPlayerDatum` extends `System.Object` — data/config reader or balancing table; AI timing/shot probability

## Correlated Types
### `<>f__AnonymousType2`4`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `<timing_meter>i__Field: !0`, `<ball_trail>i__Field: !2`, `<ball_type>i__Field: !3`
- Methods: `get_timing_meter` @ `0x2050`, `get_ball_trail` @ `0x2050`, `get_ball_type` @ `0x2050`

### `<>f__AnonymousType10`9`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `<bowler_type>i__Field: !7`, `<ball_type>i__Field: !8`
- Methods: `get_bowler_type` @ `0x2050`, `get_ball_type` @ `0x2050`

### `<>f__AnonymousType11`5`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `<bat_id>i__Field: !1`, `<ball_id>i__Field: !2`
- Methods: `get_bat_id` @ `0x2050`, `get_ball_id` @ `0x2050`

### `AnimatorDisablerForSmoothQuality`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing

### `CheatLoadGameplay`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Methods: `LoadGameplay` @ `0x2053`

### `CheatsDailyStrike`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability

### `CheatsGameplay`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `AddDotBall: UnityEngine.UI.Button`, `ForceDeadBall: UnityEngine.UI.Button`
- Methods: `OnClickAddDotBall` @ `0x2053`

### `AlphaNumericSpaceValidator`
- Extends: `System.Object`
- Probable role: input handling or control mapping
- Fields: `inputField: TMPro.TMP_InputField`

### `AbstractAnimController`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Methods: `StartPhase2Anim` @ `0x2053`, `AnimationEndEvent` @ `0x2053`

### `DefaultAnimController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing

### `AnimatorState`1`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_anim: UnityEngine.Animator`, `OnAnimStarted: elem_0x15`, `OnAnimEnded: elem_0x15`, `IsAnimating: bool`, `_onAnimEnded: elem_0x15`
- Methods: `get_Anim` @ `0x2050`, `PlayAnimation` @ `0x2053`, `waitForTransition` @ `0x2053`, `onAnimationEnd` @ `0x2053`

### `BatUIPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `_ballImage: UnityEngine.UI.Image`, `_ballsprites: UnityEngine.Sprite[]`

### `AuctionSummaryTeamData`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_fundsRemainingText: TMPro.TextMeshProUGUI`

### `PlayerPoolInfo`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_batRatingText: TMPro.TextMeshProUGUI`, `_batHandText: TMPro.TextMeshProUGUI`, `_batTypeText: TMPro.TextMeshProUGUI`
- Methods: `UpdateSoldPlayerDetail` @ `0x2053`

### `StadiumOptionItem`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `IsLocked: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`

### `RC23_UI_Data`
- Extends: `UnityEngine.ScriptableObject`
- Probable role: name-correlated gameplay/support type
- Fields: `playerCategoryBatsman: PlayerCategorySprites`, `playerCategoryBowler: PlayerCategorySprites`

### `PlayerSelectionBase`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_playerDetails: PlayerDetails`
- Methods: `get_PlayerDetails` @ `0x2640`, `get_PlayerBattingType` @ `0x2670`, `get_PlayerBattingTiming` @ `0x2688`, `get_PlayerBattingTechnique` @ `0x26a0`, `get_PlayerBattingPercentage` @ `0x26b8`

### `PlayerSelectionItem`
- Extends: `PlayerSelectionBase`
- Probable role: name-correlated gameplay/support type
- Fields: `_battingTypeText: TMPro.TextMeshProUGUI`, `_timingText: TMPro.TextMeshProUGUI`

### `Playing11SelectionItem`
- Extends: `PlayerSelectionBase`
- Probable role: AI timing/shot probability
- Fields: `_captainIndicator: UnityEngine.GameObject`
- Methods: `get_CaptainIndicator` @ `0x2050`

### `TeamDetailsBase`
- Extends: `System.Object`
- Probable role: AI timing/shot probability

### `TeamDetailsTournament`
- Extends: `TeamDetailsBase`
- Probable role: AI timing/shot probability

### `TeamDetails`
- Extends: `TeamDetailsBase`
- Probable role: AI timing/shot probability
- Fields: `_teamBattingPercent: TMPro.TextMeshProUGUI`, `_teamBattingSlider: UnityEngine.UI.Slider`

### `TourSelectedSquadElement`
- Extends: `PlayerDataBase`
- Probable role: AI timing/shot probability
- Fields: `details: PlayerDetails`

### `ClickShrinkController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_isAnimating: bool`

### `JoystickController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Fields: `_joystickBG: UnityEngine.UI.Image`, `_joystick: UnityEngine.UI.Image`, `_joystickAngleText: TMPro.TextMeshProUGUI`, `OnJoystickAngleUpdated: elem_0x15`, `_posInput: UnityEngine.Vector2`

### `PopupQueue`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `showOnMainMenuActive: bool`

### `PanelController`
- Extends: `TypeSpec`
- Probable role: animation orchestration/timing
- Methods: `OnPanelRevealAnimationFinish` @ `0x2053`, `PlayNavigationButtonAnimation` @ `0x2053`, `PlayNavigationButtonAnimation` @ `0x2053`, `playNavigationButtonAnimation` @ `0x2053`

### `UIController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Methods: `DisableInput` @ `0x2053`, `EnableInput` @ `0x2053`

### `UIStateName`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: shot selection/evaluation/animation; AI timing/shot probability
- Fields: `MAIN_MENU: UIStateName`, `SHOT_MAP: UIStateName`, `AI_SQUAD_SELECTION: UIStateName`, `MAINMENU_CUSTOM_TOURNAMENT: UIStateName`, `QUEST_MAIN: UIStateName`, `DAILY_REWARDS: UIStateName`, `BATTLEPASS: UIStateName`, `MULTIPLAYER_RANKED_MAINMENU: UIStateName`, `BAT_STICKER_SHOP_VIEW: UIStateName`, `TOURNAMENT_MAIN_MENU: UIStateName`, `TOUR_MAIN_MENU: UIStateName`, `AUCTION_MAIN_MENU: UIStateName`, `TOURNAMENT_ASHES_MAIN_MENU: UIStateName`, `TOURNAMENT_CRUSADE_MAIN_MENU: UIStateName`, `TOURNAMENT_WTC_MAIN_MENU: UIStateName`, `STORE_MAIN_MENU: UIStateName`, `TOURNAMENT_CONQUERORS_MAIN_MENU: UIStateName`, `DAILY_STRIKE_PANEL: UIStateName`

### `MainMenuTabs`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: AI timing/shot probability
- Fields: `NONE: MainMenuTabs`, `HOME: MainMenuTabs`, `MULTIPLAYER: MainMenuTabs`, `TOURNAMENT: MainMenuTabs`, `MODES: MainMenuTabs`, `STORE: MainMenuTabs`, `LENGTH: MainMenuTabs`

### `PlayerCategory`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: name-correlated gameplay/support type
- Fields: `BATSMAN: PlayerCategory`, `BOWLER: PlayerCategory`

### `BatsmanType`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: name-correlated gameplay/support type
- Fields: `DEFENSIVE: BatsmanType`, `BALANCED: BatsmanType`, `RADICAL: BatsmanType`, `BRUTE: BatsmanType`

### `BatsmanShotType`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: shot selection/evaluation/animation
- Fields: `PUSH: BatsmanShotType`, `STROKE: BatsmanShotType`, `LOFT: BatsmanShotType`

### `BatsmanProShotType`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: shot selection/evaluation/animation
- Fields: `BACK_FOOT: BatsmanProShotType`, `FRONT_FOOT: BatsmanProShotType`, `ADVANCED: BatsmanProShotType`

### `JoystickDirection`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: input handling or control mapping
- Fields: `CENTER: JoystickDirection`, `NORTH: JoystickDirection`, `NORTH_EAST_1: JoystickDirection`, `NORTH_EAST_2: JoystickDirection`, `SOUTH_EAST_1: JoystickDirection`, `SOUTH_EAST_2: JoystickDirection`, `SOUTH: JoystickDirection`, `SOUTH_WEST_2: JoystickDirection`, `SOUTH_WEST_1: JoystickDirection`, `NORTH_WEST_2: JoystickDirection`, `NORTH_WEST_1: JoystickDirection`

### `InGameUIState`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: AI timing/shot probability
- Fields: `MATCHDETAILS: InGameUIState`, `COMMENTATORDETAILS: InGameUIState`, `TWOBATSMANENTRY: InGameUIState`, `BOWLERINTRO: InGameUIState`, `BATSMANINTRO: InGameUIState`, `BATSMANWALKOUTOUT: InGameUIState`, `BATSMANCELEBRATION: InGameUIState`, `BATSMANBOWLERSELECTIONSELECTION: InGameUIState`

### `RCPL_BattingOrBowling`
- Extends: `System.Enum`
- Nested in: `UI_Defines`
- Probable role: name-correlated gameplay/support type
- Fields: `BATTING: RCPL_BattingOrBowling`, `BOWLING: RCPL_BattingOrBowling`

### `GraphicClass`
- Extends: `System.Enum`
- Probable role: AI timing/shot probability
- Fields: `MATCH_DETAILS_PANEL: GraphicClass`, `BATSMEN_ENTRY_PANEL: GraphicClass`, `BATSMAN_CENTURY: GraphicClass`, `RAIN_INTERRUPTION_PANEL: GraphicClass`, `BATSMAN_OUT: GraphicClass`, `DRS_BALL_TRACKING: GraphicClass`

### `GraphicTypeUnique`
- Extends: `System.Enum`
- Probable role: shot selection/evaluation/animation; AI timing/shot probability
- Fields: `MS_SHOT_ASSIST_BG: GraphicTypeUnique`, `MS_SHOT_ASSIST_TEXT: GraphicTypeUnique`, `SS_SUB_HEADING_BATSMAN_TYPE_LABEL: GraphicTypeUnique`, `MD_CAPTAIN_DISPLAY_BG: GraphicTypeUnique`, `MD_STADIUM_DETAIL_BG: GraphicTypeUnique`, `MD_STADIUM_DETAIL_TEXT: GraphicTypeUnique`, `MD_CAPTAIN_DISPLAY_V_1: GraphicTypeUnique`, `MD_CAPTAIN_DISPLAY_V_2: GraphicTypeUnique`, `PrB_DETAILS_BG: GraphicTypeUnique`, `PrB_DETAILS_ALPHABETIC_TEXT: GraphicTypeUnique`, `PrB_DETAILS_NUMERIC_TEXT: GraphicTypeUnique`, `PrB_DETAILS_CONTRIBUTION_TEXT: GraphicTypeUnique`, `BME_DETAILS_BG: GraphicTypeUnique`, `BME_DETAILS_TEXT: GraphicTypeUnique`, `BME_DETAILS_DIVIDER: GraphicTypeUnique`, `BME_DETAILS_OUTLINE_BG: GraphicTypeUnique`, `BME_DETAILS_DOT: GraphicTypeUnique`, `PI_DETAILS_BG_1: GraphicTypeUnique`, `PI_DETAILS_ALTERNATING_TEXT: GraphicTypeUnique`, `PI_DETAILS_VALUE_TEXT: GraphicTypeUnique`, `PI_DETAILS_BG_2: GraphicTypeUnique`, `PI_DETAILS_STRIKE_TEXT: GraphicTypeUnique`, `PI_DETAILS_BEST_TEXT: GraphicTypeUnique`, `FM_Details_Alternative_BG_2: GraphicTypeUnique`, `FM_DETAILS_HEADER_TEXT: GraphicTypeUnique`, `FM_DETAILS_VALUE_TEXT: GraphicTypeUnique`, `FM_DETAILS_ALTERNATING_BG_1: GraphicTypeUnique`, `BC_DETAILS_BG_1: GraphicTypeUnique`, `BC_DETAILS_BG_2: GraphicTypeUnique`, `BC_DETAILS_OUTLINE_BG: GraphicTypeUnique`

### `AuctionDataHolder`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `IsOpponentRetaining: bool`, `IsUserRetaining: bool`

### `AuctionHubPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `AuctionInstructionsPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `AuctionPausePanel`
- Extends: `PanelController`
- Probable role: name-correlated gameplay/support type
- Fields: `_batsmanCountText: TMPro.TextMeshProUGUI`, `_batsmanOverseasCountText: TMPro.TextMeshProUGUI`, `_bowlerCountText: TMPro.TextMeshProUGUI`, `_bowlerOverseasCountText: TMPro.TextMeshProUGUI`

### `AuctionRulesPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `AuctionSquadTeamData`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `BatsmanIDs: elem_0x15`, `SpinBowlerIDs: elem_0x15`, `BowlerIDs: elem_0x15`

### `AuctionSquadPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_batsmanContent: UnityEngine.Transform`, `_spinBowlerContent: UnityEngine.Transform`, `_bowlerContent: UnityEngine.Transform`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `AuctionSummaryPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `InAuctionPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_batRatingText: TMPro.TextMeshProUGUI`, `_playerImageContainer: UnityEngine.GameObject`, `_rtmAvailablePanel: UnityEngine.GameObject`, `_rtmAvailedPanel: UnityEngine.GameObject`, `_raiseBidRTMPanel: UnityEngine.GameObject`, `_raiseBidByAmountPanelRoot: UnityEngine.GameObject`, `_raiseBidAmountText: TMPro.TextMeshProUGUI`, `_raiseRtmBidAcceptButton: UnityEngine.UI.Button`, `_raiseRtmBidDeclineButton: UnityEngine.UI.Button`, `_raiseBidAmountAddButton: UnityEngine.UI.Button`, `_raiseBidAmountSubtractButton: UnityEngine.UI.Button`, `_raiseBidAmountAcceptButton: UnityEngine.UI.Button`
- Methods: `onClickAddAmountRaisingBid` @ `0x2053`, `onClickSubtractAmountRaisingBid` @ `0x2053`, `onClickAcceptAmountOnRaisingBid` @ `0x2053`, `OnRaiseBidRtmAcceptedByUser` @ `0x2053`, `OnRaiseBidRtmRejectedByUser` @ `0x2053`, `SetRaiseBidRtmPanelActive` @ `0x2053`, `showRtmAvailedPanel` @ `0x2053`, `OnAnimationFinished` @ `0x2053`, `<onClickAcceptAmountOnRaisingBid>b__59_0` @ `0x2053`

### `<>c`
- Extends: `System.Object`
- Nested in: `InAuctionPanel`
- Probable role: AI timing/shot probability
- Methods: `<OnRaiseBidRtmRejectedByUser>b__61_0` @ `0x2053`

### `IncreaseWalletPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_remainingAmountText: TMPro.TextMeshProUGUI`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `<CountText>d__28`
- Extends: `System.Object`
- Nested in: `IncreaseWalletPanel`
- Probable role: AI timing/shot probability
- Fields: `<Wait>5__2: UnityEngine.WaitForSecondsRealtime`

### `OpponentRetentionPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_retainButtonToggle: UnityEngine.UI.ButtonToggle`, `_doNotRetainButtonToggle: UnityEngine.UI.ButtonToggle`, `_navButtonAnim: UnityEngine.Animator[]`, `_isOpponentRetaining: bool`
- Methods: `onClickDoNotRetainButton` @ `0x2053`, `onClickRetainButton` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `PlayerPoolListPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `setPlayerDetails` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `PlayerRetentionPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`, `_playersSetToRetain: elem_0x15`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `UserRetentionPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`, `_isUserRetaining: bool`
- Methods: `get_IsUserRetaining` @ `0x2a30`, `set_IsUserRetaining` @ `0x2053`, `confirmAiRetention` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `PlayerProfileWSC`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; bat timing adjustment/model data; AI timing/shot probability
- Fields: `_batTiming: TMPro.TextMeshProUGUI`, `_batTech: TMPro.TextMeshProUGUI`
- Methods: `ShowPlayerDetails` @ `0x2053`

### `RCPass_FTUPScreen`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: name-correlated gameplay/support type
- Fields: `scrollItem: BattlePassFtueScrollItem`

### `BatCardTemplate`
- Extends: `RC19.UI.BaseCardTemplate`
- Probable role: name-correlated gameplay/support type

### `BattlepassCurrencyCardTemplate`
- Extends: `RC19.UI.BaseCardTemplate`
- Probable role: name-correlated gameplay/support type
- Fields: `uiData: BattlepassUIDataSO`

### `BattlepassKitbagItemCardTemplate`
- Extends: `RC19.UI.BaseCardTemplate`
- Probable role: name-correlated gameplay/support type
- Fields: `kitbagItemBall: KitbagItemBall`, `kitbagItemBat: KitbagItemBat`

### `BattlepassPackCardTemplate`
- Extends: `RC19.UI.BaseCardTemplate`
- Probable role: name-correlated gameplay/support type
- Fields: `uiData: BattlepassUIDataSO`

### `BattlepassTabView`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component

### `StadiumCardTemplate`
- Extends: `RC19.UI.BaseCardTemplate`
- Probable role: name-correlated gameplay/support type
- Fields: `StadiumFrame: UnityEngine.UI.Image`

### `CreditsPanel`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `DailyStrikeEntryButton`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability

### `DailyStrikeMainMenuButton`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability

### `DailyStrikePanel`
- Extends: `PanelController`
- Probable role: input handling or control mapping; AI timing/shot probability
- Fields: `iconsData: DailyStrikeUIIconsSO`, `cheatsContainer: UnityEngine.GameObject`, `addPaidEntry: UnityEngine.UI.Button`, `forcedDayInputField: TMPro.TMP_InputField`
- Methods: `get_userDailyStrikePrefs` @ `0x2050`, `StartDailyStrike` @ `0x2053`, `ShowFetchDataFailedAndGoBack` @ `0x2053`, `WaitForRankedModelThenRetryLoadUserModel` @ `0x2050`, `<StartDailyStrike>b__27_0` @ `0x2053`, `<ShowFetchDataFailedAndGoBack>b__32_0` @ `0x2053`

### `<WaitForRankedModelThenRetryLoadUserModel>d__33`
- Extends: `System.Object`
- Nested in: `DailyStrikePanel`
- Probable role: AI timing/shot probability
- Fields: `<>4__this: DailyStrikePanel`

### `DailyStrikePanelReusable`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: input handling or control mapping; AI timing/shot probability
- Fields: `iconsData: DailyStrikeUIIconsSO`, `cheatsContainer: UnityEngine.GameObject`, `addPaidEntry: UnityEngine.UI.Button`, `forcedDayInputField: TMPro.TMP_InputField`
- Methods: `get_userDailyStrikePrefs` @ `0x2050`, `StartDailyStrike` @ `0x2053`, `ShowFetchDataFailedAndGoBack` @ `0x2053`, `WaitForRankedModelThenRetryLoadUserModel` @ `0x2050`, `<StartDailyStrike>b__28_0` @ `0x2053`, `<ShowFetchDataFailedAndGoBack>b__33_0` @ `0x2053`

### `<WaitForRankedModelThenRetryLoadUserModel>d__34`
- Extends: `System.Object`
- Nested in: `DailyStrikePanelReusable`
- Probable role: AI timing/shot probability
- Fields: `<>4__this: DailyStrikePanelReusable`

### `DisclaimerPanel`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_disclaimerText: TMPro.TextMeshProUGUI`, `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `DisclaimerData`
- Extends: `System.Object`
- Nested in: `DisclaimerPanel`
- Probable role: AI timing/shot probability
- Fields: `disclaimerText: string`

### `FlashSaleChecker`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Methods: `WaitAndExecute` @ `0x2050`

### `<>c`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability
- Methods: `<WaitAndExecute>b__21_0` @ `0x2cb8`, `<WaitAndExecute>b__21_1` @ `0x2cd0`, `<WaitAndExecute>b__21_2` @ `0x2ce8`

### `<>c__DisplayClass21_0`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability
- Methods: `<WaitAndExecute>b__3` @ `0x2d00`

### `<>c__DisplayClass21_1`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability
- Methods: `<WaitAndExecute>b__4` @ `0x2d18`

### `<>c__DisplayClass21_2`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability
- Methods: `<WaitAndExecute>b__5` @ `0x2d30`

### `<>c__DisplayClass21_3`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability
- Methods: `<WaitAndExecute>b__6` @ `0x2d48`

### `<>c__DisplayClass21_4`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability
- Methods: `<WaitAndExecute>b__7` @ `0x2d60`

### `<>c__DisplayClass21_5`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability
- Methods: `<WaitAndExecute>b__8` @ `0x2d78`, `<WaitAndExecute>b__9` @ `0x2d90`

### `<WaitAndExecute>d__21`
- Extends: `System.Object`
- Nested in: `FlashSaleChecker`
- Probable role: AI timing/shot probability

### `FlashSale`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `<Id>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ProductInfo>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ProductDesc>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Header>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Prefab>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Price>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IapID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<DependentOnID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RepeatSaleAfterDays>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<DurationHrs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RepeatRewardForDays>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`

### `SaleRewardItems`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`

### `SaleUnlockCondition`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `<ItemDetails>k__BackingField: Currency`
- Methods: `get_ItemDetails` @ `0x2050`, `set_ItemDetails` @ `0x2053`

### `ActiveFlashSale`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `<Id>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsBought>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`

### `ActiveFlashSaleData`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `<Id>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsBought>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`

### `ActiveFlashSalesData`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`

### `HelpPanel`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `BatsmanCenturyPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`
- Methods: `ShowBatsmanScore` @ `0x2053`

### `BatsmanIntroPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_anim: UnityEngine.Animator`, `_batsmanNameText: TMPro.TextMeshProUGUI`, `_batsmanHandText: TMPro.TextMeshProUGUI`, `_batsmanTypeText: TMPro.TextMeshProUGUI`, `_batsmanTotalMatchesText: TMPro.TextMeshProUGUI`, `_batsmanTotalRunsText: TMPro.TextMeshProUGUI`, `_batsmanAverageText: TMPro.TextMeshProUGUI`, `_batsmanStrikeRateText: TMPro.TextMeshProUGUI`, `_batsmanFiftysText: TMPro.TextMeshProUGUI`, `_batsmanHundredsText: TMPro.TextMeshProUGUI`, `_batsmanBestText: TMPro.TextMeshProUGUI`, `nextButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`, `ShowBatsmanDetailsIntroPanel` @ `0x2053`, `setBatsmanIntroData` @ `0x2053`, `DisableBatsmanIntroPanel` @ `0x2053`, `disableBatsmanIntroPanel` @ `0x2050`, `disableBatsmanIntroPanelForSkip` @ `0x2050`

### `<>c`
- Extends: `System.Object`
- Nested in: `BatsmanIntroPanel`
- Probable role: name-correlated gameplay/support type
- Methods: `<setBatsmanIntroData>b__23_0` @ `0x3048`, `<setBatsmanIntroData>b__23_1` @ `0x3060`

### `<disableBatsmanIntroPanel>d__25`
- Extends: `System.Object`
- Nested in: `BatsmanIntroPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BatsmanIntroPanel`

### `<disableBatsmanIntroPanelForSkip>d__27`
- Extends: `System.Object`
- Nested in: `BatsmanIntroPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BatsmanIntroPanel`

### `BatsmanSelectionPanel`
- Extends: `AbstractPlayerSelection`
- Probable role: AI timing/shot probability
- Fields: `_lastBatsmanDetails: BatsmanSelectionRowInfo`, `battingTeamInfo: TeamInfo`
- Methods: `InitializePlayerDetails` @ `0x2053`, `OnBatsmanSelection` @ `0x2053`, `OnBatsmanSelectedCoop_ML` @ `0x2053`, `<OnBatsmanSelection>b__10_0` @ `0x2053`

### `<>c__DisplayClass7_0`
- Extends: `System.Object`
- Nested in: `BatsmanSelectionPanel`
- Probable role: AI timing/shot probability
- Fields: `playerDetails: PlayerDetails`, `<>4__this: BatsmanSelectionPanel`
- Methods: `<InitializePlayerDetails>b__1` @ `0x30d8`

### `<>c__DisplayClass7_1`
- Extends: `System.Object`
- Nested in: `BatsmanSelectionPanel`
- Probable role: AI timing/shot probability
- Fields: `batsmanDetails: BatsmanSelectionRowInfo`
- Methods: `<InitializePlayerDetails>b__0` @ `0x2053`

### `BatsmanSelectionRowInfo`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `timing: TMPro.TMP_Text`, `batsmanType: TMPro.TMP_Text`

### `BatsmanWalkoutPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_runAndBalls: TMPro.TMP_Text`, `_outDetail: TMPro.TMP_Text`, `_duckAnimation: UnityEngine.GameObject`, `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`
- Methods: `UpdateOutPlayerDetails` @ `0x2053`

### `<>c__DisplayClass12_0`
- Extends: `System.Object`
- Nested in: `BatsmanWalkoutPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `curBowlerID: int`

### `BowlerIntroPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_anim: UnityEngine.Animator`, `_bowlerNameText: TMPro.TextMeshProUGUI`, `_bowlerHandText: TMPro.TextMeshProUGUI`, `_bowlerTotalMatchesText: TMPro.TextMeshProUGUI`, `_bowlerTotalWicketsText: TMPro.TextMeshProUGUI`, `_bowlerAverageText: TMPro.TextMeshProUGUI`, `_bowlerStrikeRateText: TMPro.TextMeshProUGUI`, `_bowlerEconomyText: TMPro.TextMeshProUGUI`, `_bowlerBestText: TMPro.TextMeshProUGUI`, `nextButtonAnim: UnityEngine.Animator`
- Methods: `ShowBowlerDetailsIntroPanel` @ `0x2053`, `setBowlerIntroData` @ `0x2053`, `DisableBowlerIntroPanel` @ `0x2053`, `disableBowlerIntroPanel` @ `0x2050`, `disableBowlerIntroPanelForSkip` @ `0x2050`

### `<>c`
- Extends: `System.Object`
- Nested in: `BowlerIntroPanel`
- Probable role: name-correlated gameplay/support type
- Methods: `<setBowlerIntroData>b__20_0` @ `0x3258`, `<setBowlerIntroData>b__20_1` @ `0x3270`

### `<disableBowlerIntroPanel>d__22`
- Extends: `System.Object`
- Nested in: `BowlerIntroPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BowlerIntroPanel`

### `<disableBowlerIntroPanelForSkip>d__24`
- Extends: `System.Object`
- Nested in: `BowlerIntroPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BowlerIntroPanel`

### `BowlerSelectionPanel`
- Extends: `AbstractPlayerSelection`
- Probable role: AI timing/shot probability
- Fields: `_lastBowlerDetails: BowlerSelectionRowInfo`
- Methods: `InitializePlayerDetails` @ `0x2053`

### `<>c`
- Extends: `System.Object`
- Nested in: `BowlerSelectionPanel`
- Probable role: AI timing/shot probability
- Methods: `<InitializePlayerDetails>b__7_4` @ `0x3300`, `<InitializePlayerDetails>b__7_0` @ `0x3318`, `<InitializePlayerDetails>b__7_1` @ `0x3330`, `<InitializePlayerDetails>b__7_2` @ `0x3348`

### `<>c__DisplayClass7_0`
- Extends: `System.Object`
- Nested in: `BowlerSelectionPanel`
- Probable role: AI timing/shot probability
- Methods: `<InitializePlayerDetails>b__3` @ `0x3360`

### `<>c__DisplayClass7_1`
- Extends: `System.Object`
- Nested in: `BowlerSelectionPanel`
- Probable role: AI timing/shot probability
- Fields: `newDetails: PlayerDetails`
- Methods: `<InitializePlayerDetails>b__5` @ `0x3378`

### `<>c__DisplayClass7_2`
- Extends: `System.Object`
- Nested in: `BowlerSelectionPanel`
- Probable role: AI timing/shot probability
- Fields: `bowlerDetails: BowlerSelectionRowInfo`, `<>4__this: BowlerSelectionPanel`
- Methods: `<InitializePlayerDetails>b__6` @ `0x2053`, `<InitializePlayerDetails>b__7` @ `0x3390`

### `BowlerSelectionRowInfo`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `bowlerType: TMPro.TMP_Text`

### `DRSPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_snickoAnimator: UnityEngine.Animator`, `ReviewDecision_TimeRemaining: TMPro.TMP_Text`, `ReviewDecision_ReviewsRemainingText: TMPro.TMP_Text`, `_WaitingForOpponentsResponseML: TMPro.TMP_Text`, `mi_TriggerAIDRSTime: float`, `m_SnickoCurrentAnimation: SnickoAnimations`
- Methods: `get_SnickoCurrentAnimation` @ `0x33c0`, `set_SnickoCurrentAnimation` @ `0x2053`, `SetSnickoAnimation` @ `0x2053`, `UpdateDetailReviewUI` @ `0x2053`

### `DRSScreenType`
- Extends: `System.Enum`
- Nested in: `DRSPanel`
- Probable role: shot selection/evaluation/animation
- Fields: `kDRSHotspot: DRSScreenType`

### `DRSInDetailReviewEvents`
- Extends: `System.Enum`
- Nested in: `DRSPanel`
- Probable role: AI timing/shot probability
- Fields: `kOriginalCall: DRSInDetailReviewEvents`, `kPitch: DRSInDetailReviewEvents`, `kImpact: DRSInDetailReviewEvents`, `kHittingWicket: DRSInDetailReviewEvents`, `kReviewRetainOrLost: DRSInDetailReviewEvents`

### `SnickoAnimations`
- Extends: `System.Enum`
- Nested in: `DRSPanel`
- Probable role: animation orchestration/timing
- Fields: `kIdle: SnickoAnimations`, `kLow: SnickoAnimations`, `kMed: SnickoAnimations`, `kHigh: SnickoAnimations`

### `EndOfInningsPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_anim: UnityEngine.Animator`, `_navButtonAnim: UnityEngine.Animator[]`, `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`, `_playerDetailPrefabToDisable: UnityEngine.GameObject[]`, `_firstInningPlayerDetailsContainer: UnityEngine.Transform`, `_secondInningPlayerDetailsContainer: UnityEngine.Transform`, `_firstInningPlayerDetailsContainer_Test: UnityEngine.Transform`, `_secondInningPlayerDetailsContainer_Test: UnityEngine.Transform`, `_thirdInningPlayerDetailsContainer_Test: UnityEngine.Transform`, `_fourthInningPlayerDetailsContainer_Test: UnityEngine.Transform`, `_HasBattingTeamWon: bool`, `_bowlerRow: int`, `batsmanStatsSorted: elem_0x15`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `FieldSetupPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `FielderDetailsPrefab: UnityEngine.GameObject`

### `FillerMatchInfoPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `matchinfo_Batsman1Name: TMPro.TMP_Text`, `matchinfo_Batsman1Score: TMPro.TMP_Text`, `matchinfo_Batsman2Name: TMPro.TMP_Text`, `matchinfo_Batsman2Score: TMPro.TMP_Text`

### `GamePausePanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; data/config reader or balancing table; shot selection/evaluation/animation; animation orchestration/timing
- Fields: `_anim: UnityEngine.Animator`, `_generalAnim: UnityEngine.Animator`, `ShotsMapToggle: UnityEngine.UI.Button`, `m_battingShotsPresetSelection: ShotmapPanel`
- Methods: `OnShotsMapButtonClicked` @ `0x2053`

### `PauseHeaderButton`
- Extends: `System.Enum`
- Nested in: `GamePausePanel`
- Probable role: shot selection/evaluation/animation
- Fields: `Button_ShotsMap: PauseHeaderButton`

### `GameplayController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; AI timing/shot probability
- Fields: `mBattingSpecificShotTesting: BattingSpecificShotTesting`, `m_Instance: GameplayController`, `_batsmanController: BatsmanController`, `_bowlerController: BowlerController`, `_ballController: Ball`, `_bowlerAIGridOverlay: VirtualGridOverlay`, `_stumpAtBatsman: Stumps`, `_stumpAtBowler: Stumps`, `_dailyStrikeResult: UIDailyStrikeResultScreen`, `_extraInningsCanvas: UnityEngine.GameObject`, `_battingTeamJerseyMaterial: UnityEngine.Material`, `_battingTeamJerseyMaterial0: UnityEngine.Material`, `_battingTeamNetsJerseyMaterial: UnityEngine.Material`, `_battingTeamJerseyStickerMaterial: UnityEngine.Material`, `m_BattingTeamJerseyMaterial: UnityEngine.Material`, `m_BattingTeamJerseyMaterial0: UnityEngine.Material`, `m_BatsmanHelmetTransperantMaterial: UnityEngine.Material`, `m_BatsmanBatMaterial: UnityEngine.Material`, `m_BatsmanShoeMaterial: UnityEngine.Material`, `m_BatsmanGloveMaterial: UnityEngine.Material`, `m_BatsmanOutEvent: BattingStatus`, `m_BatsmanJerseyTextMaterial: UnityEngine.Material`, `m_BowlerJerseyTextMaterial: UnityEngine.Material`, `isInningsCompleted: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `BowlerMiniScreen: UnityEngine.UI.Image`, `m_RainController: RainController`, `mb_IsDeadBall_ML: bool`, `ballsPlayedInCurrentAdSession: int`, `<aiWicketGiveConditions>k__BackingField: AiWicketGiveConditions`, `DifficultyLevelSpriteArray: UnityEngine.Sprite[]`
- Methods: `get_BatsmanController` @ `0x2050`, `get_BowlerController` @ `0x2050`, `get_BallController` @ `0x2050`, `get_BowlerAIGridOverlay` @ `0x2050`, `get_StumpsAtBatsman` @ `0x2050`, `get_StumpsAtBowler` @ `0x2050`, `get_DailyStrikeResult` @ `0x2050`, `get_BattingTeamJerseyStickerMaterial` @ `0x2050`, `get_BattingTeamJerseyMaterial` @ `0x2050`, `get_BattingTeamJerseyMaterial0` @ `0x2050`, `get_BatsmanHelmetTransperantMaterial` @ `0x2050`, `get_BatsmanBatMaterial` @ `0x2050`, `get_BatsmanShoeMaterial` @ `0x2050`, `get_BatsmanGloveMaterial` @ `0x2050`, `get_BatsmanJerseyTextMaterial` @ `0x2050`, `get_BowlerJerseyTextMaterial` @ `0x2050`, `get_RainController` @ `0x2050`, `get_IsDeadBall_ML` @ `0x3618`, `get_aiWicketGiveConditions` @ `0x2050`, `set_aiWicketGiveConditions` @ `0x2053`, `WaitUntilOpponentSquadIsCreated` @ `0x2050`, `ResetGamePlayCycleWithDelay` @ `0x2053`, `ResetGamePlayCycle` @ `0x2050`, `ResetGamePlayCycle` @ `0x2053`, `ToogleBatUIPanel` @ `0x2053`, `SetBatsmanProperties` @ `0x2053`, `OnBattingTeamWon` @ `0x2053`, `ShowUmpireSignalOnBallCollection` @ `0x2053`, `SetImpactPlayerForAIBatting` @ `0x2053`, `OnBallCollection` @ `0x2050`, `HideBatsmans` @ `0x2053`, `HideBowler` @ `0x2053`, `ResetGamePlayCycleForNets` @ `0x2053`, `ShowPlayerDifficultyStars` @ `0x2053`, `UpdateMatchonRainInterruption` @ `0x2053`, `GetIsUserBatting` @ `0x36c0`, `setDeadBall_Ml` @ `0x2053`, `ForceDeadBallWithDelay` @ `0x2050`, `OnDeadball_Ml` @ `0x2053`, `<WaitUntilOpponentSquadIsCreated>b__254_0` @ `0x3738`

### `<>c__DisplayClass258_0`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<>c__DisplayClass261_0`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<>c__DisplayClass266_0`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<>c__DisplayClass266_1`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<>c__DisplayClass290_0`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<>c__DisplayClass341_0`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<>c__DisplayClass341_1`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `selectBowlerID: int`

### `<CapturePlayersScorebarUI>d__274`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<ForceDeadBallWithDelay>d__345`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<OnBallCollection>d__296`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`, `isBowlerFielding: bool`, `<isBatsmanRunning>5__2: bool`

### `<OnGameRestrart_ML>d__354`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<OnRestartMatch>d__290`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<ResetGamePlayCycle>d__269`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<ShowChallengeUI>d__266`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<StartHighlights>d__264`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<StartMatch>d__265`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: GameplayController`

### `<WaitUntilOpponentSquadIsCreated>d__254`
- Extends: `System.Object`
- Nested in: `GameplayController`
- Probable role: AI timing/shot probability
- Fields: `<>4__this: GameplayController`

### `InGamePanels`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; timing meter/UI parameter system; shot selection/evaluation/animation; AI timing/shot probability
- Fields: `_matchDetailsPanel: UnityEngine.GameObject`, `_batsmanSelectionPanel: UnityEngine.GameObject`, `_bowlerSelectionPanel: UnityEngine.GameObject`, `_openingBatsmenWalkInIntro: UnityEngine.GameObject`, `_batsmanWalkoutPanel: UnityEngine.GameObject`, `_bowlerIntroPanel: UnityEngine.GameObject`, `_batsmanIntroPanel: UnityEngine.GameObject`, `_batsmanCenturyPanel: UnityEngine.GameObject`, `_rainInterruptionPanel: UnityEngine.GameObject`, `_dailyStrikeProgressBar: UnityEngine.GameObject`, `_dailyStrikeTrackerUI: DailyStrikeTrackerUI`, `_mainPanelHUD: UnityEngine.Transform`, `_inGameScreens_GamePlay: UnityEngine.Transform`, `_timingMeter: UnityEngine.GameObject`, `TimingMeter_PerfectImage: UnityEngine.UI.Image`, `TimingMeter_EarlyPerfectImage: UnityEngine.UI.Image`, `TimingMeter_EarlyImage: UnityEngine.UI.Image`, `TimingMeter_LatePerfectImage: UnityEngine.UI.Image`, `TimingMeter_LateImage: UnityEngine.UI.Image`, `_shotmapPresetText: TMPro.TMP_Text`, `dailyStrikeModePauseView: UnityEngine.GameObject`, `ShotIDText: TMPro.TMP_Text`, `BowlerGridID: TMPro.TMP_Text`, `ShotDetails: TMPro.TMP_Text`, `_canvasGamePlay: UnityEngine.GameObject`
- Methods: `get_MatchDetailsPanel` @ `0x2050`, `get_BatsmanSelectionPanel` @ `0x2050`, `get_BowlerSelectionPanel` @ `0x2050`, `get_OpeningBatsmenWalkInIntro` @ `0x2050`, `get_BatsmanWalkoutPanel` @ `0x2050`, `get_BowlerIntroPanel` @ `0x2050`, `get_BatsmanIntroPanel` @ `0x2050`, `get_BatsmanCenturyPanel` @ `0x2050`, `get_RainInterruptionPanel` @ `0x2050`, `get_DailyStrikeProgressBar` @ `0x2050`, `get_DailyStrikeTrackerUI` @ `0x2050`, `get_MainPanelHUD` @ `0x2050`, `get_InGameScreens_GamePlay` @ `0x2050`, `get_TimingMeter` @ `0x2050`, `InitBatsmanPresetObj` @ `0x2053`, `SetDailyStrikeScreen` @ `0x2053`, `<InitBatsmanPresetObj>b__220_0` @ `0x2053`, `<InitBatsmanPresetObj>b__220_1` @ `0x2053`

### `ManOfTheMatchPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_nextButtonAnimator: UnityEngine.Animator`
- Methods: `PlayNavButtonAnimations` @ `0x2053`

### `MatchDetailsPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; data/config reader or balancing table; animation orchestration/timing; AI timing/shot probability
- Fields: `_animator: UnityEngine.Animator`, `_opponentCaptainImage: UnityEngine.UI.Image`, `_userCaptainImage: UnityEngine.UI.Image`, `_rainProbabilityText: TMPro.TMP_Text`, `navButtonAnim: UnityEngine.Animator[]`, `_matchDetailsPanel: UnityEngine.GameObject`, `_commentatorDetailsPanel: UnityEngine.GameObject`, `_playerPoseAnim: UnityEngine.Animator`, `commentatorDetails: SOCommentatorDetails`
- Methods: `SetMatchDetailsEntryState_ML` @ `0x2050`, `PlayNavButtonsAnimation` @ `0x2053`

### `TemperatureData`
- Extends: `System.Object`
- Nested in: `MatchDetailsPanel`
- Probable role: AI timing/shot probability
- Fields: `<RainProb_0>k__BackingField: float`, `<RainProb_25>k__BackingField: float`, `<RainProb_50>k__BackingField: float`, `<RainProb_75>k__BackingField: float`, `<RainProb_100>k__BackingField: float`
- Methods: `get_RainProb_0` @ `0x3af8`, `set_RainProb_0` @ `0x2053`, `get_RainProb_25` @ `0x3b10`, `set_RainProb_25` @ `0x2053`, `get_RainProb_50` @ `0x3b28`, `set_RainProb_50` @ `0x2053`, `get_RainProb_75` @ `0x3b40`, `set_RainProb_75` @ `0x2053`, `get_RainProb_100` @ `0x3b58`, `set_RainProb_100` @ `0x2053`

### `<>c`
- Extends: `System.Object`
- Nested in: `MatchDetailsPanel`
- Probable role: AI timing/shot probability
- Methods: `<SetMatchDetailsEntryState_ML>b__36_0` @ `0x3b70`

### `<LoadPlayerTexture>d__40`
- Extends: `System.Object`
- Nested in: `MatchDetailsPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MatchDetailsPanel`, `<player>5__4: PlayerDetails`

### `<SetMatchDetailsEntryState_ML>d__36`
- Extends: `System.Object`
- Nested in: `MatchDetailsPanel`
- Probable role: AI timing/shot probability
- Fields: `<>4__this: MatchDetailsPanel`

### `MatchResultPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_abstractEntryAnimator: UnityEngine.Animator`, `_MatchResultPanelAnimator: UnityEngine.Animator`, `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`, `_battlepassXpView: UnityEngine.GameObject`, `_battlepassRP_view: UnityEngine.GameObject`, `_battlepassSP_view: UnityEngine.GameObject`, `_battlepassText: TMPro.TMP_Text`, `_battlepassRPValueText: TMPro.TMP_Text`, `_battlepassSPValueText: TMPro.TMP_Text`
- Methods: `AnimatePanel` @ `0x2053`, `HandleBattlepass` @ `0x2053`

### `<>c__DisplayClass42_0`
- Extends: `System.Object`
- Nested in: `MatchResultPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `prevXP_BattlePass: int`
- Methods: `<HandleBattlepass>b__0` @ `0x2053`

### `MatchRewardPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`, `mb_IsDoubleReward: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`

### `MatchWinLoseInfoPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`

### `PartnershipPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_batsmanANameText: TMPro.TextMeshProUGUI`, `_batsmanARunsText: TMPro.TextMeshProUGUI`, `_batsmanBNameText: TMPro.TextMeshProUGUI`, `_batsmanBRunsText: TMPro.TextMeshProUGUI`, `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`, `navButtonAnim: UnityEngine.Animator`, `_anim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `PlayerIntroGeneric`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `batsman: UnityEngine.Transform`, `bowler: UnityEngine.Transform`, `batsmanTechnique: UnityEngine.UI.Slider`, `batsmanTiming: UnityEngine.UI.Slider`, `batsmanAggression: UnityEngine.UI.Slider`, `batsmanTechniqueValue: TMPro.TMP_Text`, `batsmanTimingValue: TMPro.TMP_Text`, `batsmanAggressionValue: TMPro.TMP_Text`, `batsmanCatagory: TMPro.TMP_Text`, `batsmanType: TMPro.TMP_Text`, `bowlerSkill: UnityEngine.UI.Slider`, `bowlerMovement: UnityEngine.UI.Slider`, `bowlerFieldRating: UnityEngine.UI.Slider`, `bowlerSkillValue: TMPro.TMP_Text`, `bowlerMovementValue: TMPro.TMP_Text`, `bowlerFieldRatingValue: TMPro.TMP_Text`, `bowlerCatagory: TMPro.TMP_Text`

### `RainInterruptionPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Methods: `showRainInterruption` @ `0x2053`, `hideRainInterruption` @ `0x2053`

### `ScoreBarUI`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_battingTeamInfo: TeamInfo`, `_animator: UnityEngine.Animator`, `_battingSideColourCodeImage: UnityEngine.UI.Image`, `_battingSideColourCodeImage2: UnityEngine.UI.Image`, `_battingSideColourCodeImage3: UnityEngine.UI.Image`, `_battingSideLogoImage: UnityEngine.UI.Image`, `_battingSideTeamNameText: TMPro.TMP_Text`, `_batsmanStrikeNameText: TMPro.TMP_Text`, `_batsmanStrikeScoreText: TMPro.TMP_Text`, `_batsmanStrikeBallsFacedText: TMPro.TMP_Text`, `_batsmanNonStrikeNameText: TMPro.TMP_Text`, `_batsmanNonStrikeScoreText: TMPro.TMP_Text`, `_batsmanNonStrikeBallsFacedText: TMPro.TMP_Text`, `BatsmanRenderTexture: UnityEngine.RenderTexture[]`, `_battingSideInfo: TMPro.TMP_Text`, `_bowlerNameText: TMPro.TMP_Text`, `_bowlerStatsText: TMPro.TMP_Text`, `_battingSideTeamNameScoreBarText: TMPro.TMP_Text`, `_battingScoreText: TMPro.TMP_Text`, `_battingSideInfoTextAlpha: float`, `_runsInBallText: TMPro.TMP_Text`, `_superOverRemainingballsText: TMPro.TMP_Text`, `GOBowlerImpactArrow: UnityEngine.GameObject`, `AnimationImages: UnityEngine.RectTransform`, `_bowlerRenderTexture: UnityEngine.RenderTexture`, `BowlerRenderTexture: UnityEngine.GameObject`, `Batsman1RenderTexture: UnityEngine.GameObject`, `Batsman2RenderTexture: UnityEngine.GameObject`
- Methods: `AnimateScorebar` @ `0x2053`, `AnimateMoveUp` @ `0x2050`, `AnimateMoveDown` @ `0x2050`, `<AnimateMoveDown>b__83_0` @ `0x2053`, `<AnimateMoveDown>b__83_1` @ `0x2053`, `<AnimateMoveDown>b__83_2` @ `0x2053`

### `<>c__DisplayClass81_0`
- Extends: `System.Object`
- Nested in: `ScoreBarUI`
- Probable role: animation orchestration/timing
- Methods: `<AnimateMoveUp>b__0` @ `0x2053`, `<AnimateMoveUp>b__1` @ `0x2053`, `<AnimateMoveUp>b__2` @ `0x2053`

### `ScorecardPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_panelRootAnimator: UnityEngine.Animator`, `_navButtonAnim: UnityEngine.Animator[]`, `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`, `_currentInnBattingScorecard: UnityEngine.Transform`, `_currentInnBattingContainer: UnityEngine.Transform`, `_currentInnBowlingContainer: UnityEngine.Transform`, `_firstInnBattingScorecard: UnityEngine.Transform`, `_firstInnBattingContainer: UnityEngine.Transform`, `_firstInnBowlingContainer: UnityEngine.Transform`, `_secondInnBattingScorecard: UnityEngine.Transform`, `_secondInnBattingContainer: UnityEngine.Transform`, `_secondInnBowlingContainer: UnityEngine.Transform`, `_thirdInnBattingScorecard: UnityEngine.Transform`, `_thirdInnBattingContainer: UnityEngine.Transform`, `_thirdInnBowlingContainer: UnityEngine.Transform`, `_battingItems: elem_0x15`, `_battingTeamPlayerDetails: elem_0x15`, `_bowlingTeamPlayerDetails: elem_0x15`, `_inningsContainer: UnityEngine.Transform[]`, `battingPlayerDetails: elem_0x15`, `bowlingPlayerDetails: elem_0x15`, `bowlingDetails: elem_0x15`
- Methods: `get_CurrentInnBattingScorecard` @ `0x2050`, `get_CurrentInnBattingContainer` @ `0x2050`, `get_CurrentInnBowlingContainer` @ `0x2050`, `get_FirstInnBattingScorecard` @ `0x2050`, `get_FirstInnBattingContainer` @ `0x2050`, `get_FirstInnBowlingContainer` @ `0x2050`, `get_SecondInnBattingScorecard` @ `0x2050`, `get_SecondInnBattingContainer` @ `0x2050`, `get_SecondInnBowlingContainer` @ `0x2050`, `get_ThirdInnBattingScorecard` @ `0x2050`, `get_ThirdInnBattingContainer` @ `0x2050`, `get_ThirdInnBowlingContainer` @ `0x2050`, `UpdateScoreCardBatting` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `ScoreCardEvent`
- Extends: `System.Enum`
- Nested in: `ScorecardPanel`
- Probable role: AI timing/shot probability
- Fields: `kRainInterruption: ScoreCardEvent`

### `<>c__DisplayClass100_0`
- Extends: `System.Object`
- Nested in: `ScorecardPanel`
- Probable role: AI timing/shot probability
- Fields: `battingStatDetails: elem_0x15`

### `<>c__DisplayClass101_0`
- Extends: `System.Object`
- Nested in: `ScorecardPanel`
- Probable role: AI timing/shot probability
- Fields: `battingStatDetails: BatsmanStats[]`

### `<>c__DisplayClass105_0`
- Extends: `System.Object`
- Nested in: `ScorecardPanel`
- Probable role: AI timing/shot probability
- Fields: `battingStatDetails: BatsmanStats[]`

### `<>c__DisplayClass105_1`
- Extends: `System.Object`
- Nested in: `ScorecardPanel`
- Probable role: name-correlated gameplay/support type
- Methods: `<UpdateScoreCardBatting>b__0` @ `0x3e70`, `<UpdateScoreCardBatting>b__1` @ `0x3e88`, `<UpdateScoreCardBatting>b__2` @ `0x3ea0`, `<UpdateScoreCardBatting>b__3` @ `0x3eb8`, `<UpdateScoreCardBatting>b__4` @ `0x3ed0`

### `SquadOverviewPanel`
- Extends: `PlayerDataBase`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `navButtonAnim: UnityEngine.Animator`, `_panelAnimator: UnityEngine.Animator`, `_opponentPlayerMainPanel: UnityEngine.GameObject`, `_userPlayerMainPanel: UnityEngine.GameObject`, `_playerPoseAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `PlayerCategoryShort`
- Extends: `System.Enum`
- Nested in: `SquadOverviewPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `Bat: PlayerCategoryShort`

### `<>c__DisplayClass48_0`
- Extends: `System.Object`
- Nested in: `SquadOverviewPanel`
- Probable role: AI timing/shot probability
- Fields: `savedCaptainID: int`

### `<>c__DisplayClass49_0`
- Extends: `System.Object`
- Nested in: `SquadOverviewPanel`
- Probable role: AI timing/shot probability
- Fields: `savedCaptainID: int`

### `<showOpponentTeamSquad>d__48`
- Extends: `System.Object`
- Nested in: `SquadOverviewPanel`
- Probable role: AI timing/shot probability
- Fields: `<captain>5__7: PlayerDetails`

### `<showUserTeamSquad>d__49`
- Extends: `System.Object`
- Nested in: `SquadOverviewPanel`
- Probable role: AI timing/shot probability
- Fields: `<captain>5__7: PlayerDetails`

### `HawkeyeStatisticsPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `m_MainPanel: UnityEngine.GameObject`, `BallHawkEyePrefab: BallHawkEye`, `m_BallObjects: elem_0x15`
- Methods: `addHawkEyeBAll` @ `0x2050`

### `<addHawkEyeBAll>d__21`
- Extends: `System.Object`
- Nested in: `HawkeyeStatisticsPanel`
- Probable role: name-correlated gameplay/support type

### `PartnershipCell`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `_totalBalls: TMPro.TMP_Text`
- Methods: `get_TotalBalls` @ `0x2050`

### `PartnershipStatisticsPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_backButtonAnim: UnityEngine.Animator`, `_nextButtonAnim: UnityEngine.Animator`

### `WagonWheelStatisticsPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_mainPanel: UnityEngine.GameObject`, `mainPanel: UnityEngine.GameObject`, `m_BallObjects: elem_0x15`

### `<drawLines>d__37`
- Extends: `System.Object`
- Nested in: `WagonWheelStatisticsPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<distBall>5__5: float`

### `StatisticsPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`

### `SuperOverIntro`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `userCaptainImages: elem_0x15`, `oppCaptainImages: elem_0x15`, `playerPoseAnim: UnityEngine.Animator`

### `TossPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_animator: UnityEngine.Animator`, `_TailsButton: UnityEngine.UI.Button`, `_BattingButton: UnityEngine.UI.Button`, `bWonTossSelectBatFirst: bool`, `bWonTossSelectBallFirst: bool`
- Methods: `OnTailsButtonClick` @ `0x2053`, `OnBattingButtonClick` @ `0x2053`

### `ButtonTags`
- Extends: `System.Enum`
- Nested in: `TossPanel`
- Probable role: AI timing/shot probability
- Fields: `kTails: ButtonTags`, `kBatting: ButtonTags`

### `TossScreenSequence`
- Extends: `System.Enum`
- Nested in: `TossPanel`
- Probable role: animation orchestration/timing
- Fields: `KShowHandShakeAnim: TossScreenSequence`

### `TournamentWinPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_nextButtonAnimator: UnityEngine.Animator`, `DifficultyStarsPanel: UnityEngine.UI.Image`, `DifficultyText: TMPro.TMP_Text`
- Methods: `PlayNavButtonAnimations` @ `0x2053`

### `TwoBatsmenEntryPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_anim: UnityEngine.Animator`, `_batsmanAName: TMPro.TextMeshProUGUI`, `_batsmanAHand: TMPro.TextMeshProUGUI`, `_batsmanATiming: TMPro.TextMeshProUGUI`, `_batsmanATechnique: TMPro.TextMeshProUGUI`, `_batsmanAType: TMPro.TextMeshProUGUI`, `_batsmanATeamIcon: UnityEngine.UI.Image`, `_batsmanATeamIconBG: UnityEngine.UI.Image`, `_batsmanBName: TMPro.TextMeshProUGUI`, `_batsmanBHand: TMPro.TextMeshProUGUI`, `_batsmanBTiming: TMPro.TextMeshProUGUI`, `_batsmanBTechnique: TMPro.TextMeshProUGUI`, `_batsmanBType: TMPro.TextMeshProUGUI`, `_batsmanBTeamIcon: UnityEngine.UI.Image`, `_batsmanBTeamIconBG: UnityEngine.UI.Image`, `navButtonAnim: UnityEngine.Animator`
- Methods: `get_Anim` @ `0x2050`, `ShowOpeningBatsmenDetails` @ `0x2053`, `playExitAnim` @ `0x2050`, `disableTwoBatsmanEntryPanelForSkip` @ `0x2050`

### `<disableTwoBatsmanEntryPanelForSkip>d__21`
- Extends: `System.Object`
- Nested in: `TwoBatsmenEntryPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: TwoBatsmenEntryPanel`

### `<playExitAnim>d__20`
- Extends: `System.Object`
- Nested in: `TwoBatsmenEntryPanel`
- Probable role: animation orchestration/timing
- Fields: `<>4__this: TwoBatsmenEntryPanel`

### `MainMenuPanel`
- Extends: `PanelController`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing; AI timing/shot probability
- Fields: `_shotBook: UnityEngine.UI.Button`, `_dailyRewards: UnityEngine.UI.Button`, `_contentAnim: UnityEngine.Animator`, `_mainMenuExtendedMenu: UnityEngine.GameObject`, `_mainMenuTabs: UnityEngine.GameObject`, `_mainMenuTabButtons: MainMenuTabButton[]`, `FAILED_TO_JOIN_FIREND: string`, `FAILED_TO_SYNC: string`, `ANIM_FOOTER_BUTTONS: string`, `isDailyRewardsSeen: bool`
- Methods: `onShotBookClicked` @ `0x2053`, `onDailyRewardClicked` @ `0x2053`, `isDownloadSquadAvailable` @ `0x41e8`, `OnPanelRevealAnimationFinish` @ `0x2053`, `CheckAndDisplayDailyStrikePanel` @ `0x4278`, `ShowDailyRewardPopup` @ `0x2053`, `GetDaysPassedInDailyReward` @ `0x42c0`, `PlaySubPanelViewAnimEntry` @ `0x2053`, `PlaySubPanelViewAnimReturn` @ `0x2053`, `InstantiateMainMenuRaycastBlocker` @ `0x2050`, `<onDailyRewardClicked>b__81_0` @ `0x2053`

### `MainMenuTabButton`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: AI timing/shot probability
- Fields: `_buttonTab: MainMenuTabs`

### `<>c`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: shot selection/evaluation/animation
- Methods: `<onShotBookClicked>b__73_0` @ `0x2053`

### `<<CheckAndDisplayCommunityEventFirebasePopup>b__118_0>d`
- Extends: `System.ValueType`
- Nested in: `<>c`
- Probable role: name-correlated gameplay/support type
- Fields: `<>u__1: System.Runtime.CompilerServices.TaskAwaiter`

### `<<CheckAndDisplayRCPLFirebasePopup>b__119_0>d`
- Extends: `System.ValueType`
- Nested in: `<>c`
- Probable role: name-correlated gameplay/support type
- Fields: `<>u__1: System.Runtime.CompilerServices.TaskAwaiter`

### `<>c__DisplayClass127_0`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenuPanel`

### `<>c__DisplayClass131_0`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenuPanel`

### `<>c__DisplayClass156_0`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenuPanel`, `tab: MainMenuTabs`

### `<>c__DisplayClass71_0`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenuPanel`

### `<OnFetchNotRecieved>d__129`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenuPanel`

### `<UpdatePromoEventTimer>d__93`
- Extends: `System.Object`
- Nested in: `MainMenuPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenuPanel`

### `MainMenuTab`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_mmPanel: MainMenuPanel`

### `Tab_Home`
- Extends: `MainMenuTab`
- Probable role: AI timing/shot probability
- Fields: `_dailyStrikeBtn: UnityEngine.UI.Button`, `_dailyStrikeTutorialHandle: MEC.CoroutineHandle`
- Methods: `onDailyStrikeClicked` @ `0x2053`, `SetDailyStrikeMode` @ `0x2053`, `<onDailyStrikeClicked>b__19_0` @ `0x2053`, `<onDailyStrikeClicked>b__19_1` @ `0x2053`

### `Tab_Modes`
- Extends: `MainMenuTab`
- Probable role: name-correlated gameplay/support type

### `Tab_Tournament`
- Extends: `MainMenuTab`
- Probable role: name-correlated gameplay/support type

### `TournamentButton`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `extraImages: UnityEngine.GameObject[]`, `isDiscountProduct: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `_IsTournamentActive: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `_TournamentTier: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_UnlocksAtLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_StoreProductID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_IsTournamentUnlockedThroughTutorialDailyRewards: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`

### `AISquadSelectionContent`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_aiSquadSelectionPanel: AISquadSelectionPanel`, `_appointCaptainButton: UnityEngine.UI.ButtonToggle`, `_isAppointCaptainActive: bool`, `_isCaptainClicked: bool`, `_currentOpponentCaptainUID: int`, `_selectedFinal11PlayerDetails: PlayerSelectionBase`, `_selectedAllSquadPlayerDetails: PlayerSelectionBase`, `_tempPlayerDetails: PlayerSelectionBase`, `_cachedCaptainDetails: PlayerSelectionBase`
- Methods: `onClickAppointCaptain` @ `0x2053`, `setCurrentOpponentCaptainID` @ `0x2053`, `resetCaptainDataInFinal11` @ `0x2053`, `LoadGamePlayScene` @ `0x2053`, `LoadGamePlay` @ `0x2053`, `<resetCaptainDataInFinal11>b__42_1` @ `0x2053`, `<LoadGamePlay>b__56_0` @ `0x2053`, `<LoadGamePlay>b__56_3` @ `0x2053`, `<LoadGamePlay>b__56_4` @ `0x2053`, `<LoadGamePlay>b__56_5` @ `0x2053`, `<LoadGamePlay>b__56_1` @ `0x2053`, `<LoadGamePlay>b__56_6` @ `0x2053`, `<LoadGamePlay>b__56_2` @ `0x2053`

### `<>c`
- Extends: `System.Object`
- Nested in: `AISquadSelectionContent`
- Probable role: AI timing/shot probability
- Methods: `<resetCaptainDataInFinal11>b__42_0` @ `0x45d8`

### `AISquadSelectionPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_selectedPlayerBattingPercentageText: TMPro.TextMeshProUGUI`, `redBlockAnim: UnityEngine.Animator`, `navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayCharacterAnimation` @ `0x2053`, `PlayRedBlocksAnimation` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`, `OnClickAppointCaptain` @ `0x2053`

### `MatchSettingPanel`
- Extends: `PanelController`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing; AI timing/shot probability
- Fields: `_settingDifficulty: SettingElement`, `_settingChanceOfRain: SettingElement`, `_shotAssist: UnityEngine.UI.ButtonToggle`, `_shotAssistInfo: UnityEngine.UI.Button`, `_customDifficultyPanel: UnityEngine.RectTransform`, `_navButtonCustomDifficultyNext: UnityEngine.UI.Button`, `_difficultyCustomBatEasy: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatMedium: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatHard: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatExpert: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatHardcore: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlEasy: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlMedium: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlHard: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlExpert: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlHardcore: UnityEngine.UI.ButtonToggle`, `_navButtonAnim: UnityEngine.Animator[]`, `_difficultyIndexBatting: int`, `_difficultyIndexBowling: int`, `_maxOversPerBowler: int[]`, `_bowlerOverPerMatch: int`, `_useShotAssist: bool`, `_buttonToggleDifficulty: UnityEngine.UI.ButtonToggle`, `_buttonToggleChanceOfRain: UnityEngine.UI.ButtonToggle`, `customDifficultyPanelDisabled: bool`
- Methods: `onDifficultyUpdated` @ `0x2053`, `onDifficultyIntractableUpdated` @ `0x2053`, `onChanceOfRainIntractableUpdated` @ `0x2053`, `onClickCustomDifficultyNext` @ `0x2053`, `onDifficultyCustomBatChanged` @ `0x2053`, `onDifficultyCustomBowlChanged` @ `0x2053`, `setMaxOverPerBowler` @ `0x2053`, `toggleCustomDifficultyPanel` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `SquadSelectionContent`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_appointCaptainButton: UnityEngine.UI.ButtonToggle`, `_isAppointCaptainActive: bool`, `_isCaptainClicked: bool`, `_currentUserCaptainUID: int`, `_selectedFinal11PlayerDetails: PlayerSelectionBase`, `_selectedAllSquadPlayerDetails: PlayerSelectionBase`, `_tempPlayerDetails: PlayerSelectionBase`, `_cachedCaptainDetails: PlayerSelectionBase`
- Methods: `get_AppointCaptainButton` @ `0x2050`, `get_IsAppointCaptainActive` @ `0x46c8`, `onClickAppointCaptain` @ `0x2053`, `setCurrentUserCaptainID` @ `0x2053`, `resetCaptainDataInFinal11` @ `0x2053`, `<resetCaptainDataInFinal11>b__63_1` @ `0x2053`

### `<>c`
- Extends: `System.Object`
- Nested in: `SquadSelectionContent`
- Probable role: AI timing/shot probability
- Methods: `<resetCaptainDataInFinal11>b__63_0` @ `0x4770`

### `SquadSelectionPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_selectedPlayerBattingPercentageText: TMPro.TextMeshProUGUI`, `_rcplBatting1: UnityEngine.UI.ButtonToggle`, `_rcplBatting2: UnityEngine.UI.ButtonToggle`, `_currentRcplPanelType: RCPL_BattingOrBowling`, `redBlockAnim: UnityEngine.Animator`, `navButtonAnim: UnityEngine.Animator[]`
- Methods: `PlayCharacterAnimation` @ `0x2053`, `PlayRedBlocksAnimation` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`, `OnClickAppointCaptain` @ `0x2053`

### `TeamSelectionPanel`
- Extends: `PanelController`
- Probable role: input handling or control mapping; animation orchestration/timing; AI timing/shot probability
- Fields: `_userTeam: TeamDetails`, `_opponentTeam: TeamDetails`, `_navButtonAnim: UnityEngine.Animator[]`, `_userBatsmanJerseyMat: UnityEngine.Material`, `_opponentBatsmanJerseyMat: UnityEngine.Material`, `_batsmanBatMaterial: UnityEngine.Material`, `_statBarAnimDuration: float`, `_userStatBarAnimCoroutine: UnityEngine.Coroutine`, `_opponentStatBarAnimCoroutine: UnityEngine.Coroutine`, `isRankedTeamAvailable: bool`
- Methods: `updateUserTeamDetail` @ `0x2053`, `updateOpponentTeamDetail` @ `0x2053`, `animateStats` @ `0x2053`, `AnimateSliderValues` @ `0x2050`, `checkRankedTeamAvailableFor` @ `0x2053`, `animateOpponentTeamStats` @ `0x2053`, `animateUserTeamStats` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`, `EnableTeamInputs_ML` @ `0x2053`, `DisableTeamInputs_ML` @ `0x2053`

### `<>c__DisplayClass49_0`
- Extends: `System.Object`
- Nested in: `TeamSelectionPanel`
- Probable role: AI timing/shot probability
- Methods: `<updateUserTeamDetail>b__0` @ `0x4860`

### `<>c__DisplayClass50_0`
- Extends: `System.Object`
- Nested in: `TeamSelectionPanel`
- Probable role: AI timing/shot probability
- Methods: `<updateOpponentTeamDetail>b__0` @ `0x4878`

### `<AnimateSliderValues>d__52`
- Extends: `System.Object`
- Nested in: `TeamSelectionPanel`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `teamDetails: TeamDetails`, `ratingBat: int`

### `ChallengerModePanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `navButtonAnim: UnityEngine.Animator`
- Methods: `HideMainMenu` @ `0x2053`, `JoinMatchAfterTutorialOrCaptainAppoiment` @ `0x2050`, `PlayNavButtonsAnimation` @ `0x2053`

### `<>c__DisplayClass41_0`
- Extends: `System.Object`
- Nested in: `ChallengerModePanel`
- Probable role: AI timing/shot probability
- Methods: `<JoinMatchAfterTutorialOrCaptainAppoiment>b__0` @ `0x2053`, `<JoinMatchAfterTutorialOrCaptainAppoiment>b__1` @ `0x2053`

### `<JoinMatchAfterTutorialOrCaptainAppoiment>d__41`
- Extends: `System.Object`
- Nested in: `ChallengerModePanel`
- Probable role: AI timing/shot probability

### `PlayWithFriendsViewNew`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `friendsCode: TMPro.TMP_InputField`, `WAITING_FOR_FRIEND_TO_ACCEPT: string`, `navButtonAnim: UnityEngine.Animator`
- Methods: `OnFriendRankDataFetchFailed` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `RankedPremierLeagueConfig`
- Extends: `System.Object`
- Probable role: data/config reader or balancing table
- Fields: `<LeagueID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`

### `MultiplayerSquadSelectioContent`
- Extends: `SquadSelectionContent`
- Probable role: AI timing/shot probability
- Fields: `MIN_BOWLER_COUNT: int`
- Methods: `showWaitForMLSyncingText` @ `0x2053`, `loadGamePlay` @ `0x2053`, `<showWaitForMLSyncingText>b__37_0` @ `0x2053`

### `NetsMenuPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `_settingBatsman: SettingElement`, `_settingBatsmanHand: SettingElement`, `_settingBowlerType: SettingElement`, `_settingBowlerHand: SettingElement`, `_battingToggle: UnityEngine.UI.ButtonToggle`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `onBatsmanTypeUpdated` @ `0x2053`, `onBatsmanHandUpdated` @ `0x2053`, `onBowlerTypeUpdated` @ `0x2053`, `onBowlerHandUpdated` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `QualityPanel`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `QuestBaseCommonData`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator`, `CachedContainerData: QuestContainer`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `QuestMenuPanel`
- Extends: `PanelController`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing
- Fields: `_shotoftheWeekWidget: RC19.UI.QuestShotoftheWeekWidget`, `_shotGalleryPreviewPrefab: UnityEngine.GameObject`, `_shotGalleryBtn: UnityEngine.UI.Button`, `_navButtonAnim: UnityEngine.Animator`, `_shotGalleryPreviewObj: UnityEngine.GameObject`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `ButtonTag`
- Extends: `System.Enum`
- Nested in: `QuestMenuPanel`
- Probable role: shot selection/evaluation/animation
- Fields: `ShotGallery: ButtonTag`

### `<>c__DisplayClass39_0`
- Extends: `System.Object`
- Nested in: `QuestMenuPanel`
- Probable role: AI timing/shot probability
- Fields: `questContainers: elem_0x15`

### `<>c__DisplayClass39_1`
- Extends: `System.Object`
- Nested in: `QuestMenuPanel`
- Probable role: AI timing/shot probability
- Fields: `container: QuestContainer`

### `QuestPurchasePanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator`, `_batCardtemplate: BatCardTemplate`, `_kitbagItemBall: KitbagItemBall`, `_kitbagItemBat: KitbagItemBat`, `_scratchAndWinContainer: QuestContainer`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `<>c__DisplayClass69_0`
- Extends: `System.Object`
- Nested in: `QuestPurchasePanel`
- Probable role: name-correlated gameplay/support type
- Fields: `batStickerList: elem_0x15`

### `QuestScratchAndWinPanel`
- Extends: `QuestBaseCommonData`
- Probable role: animation orchestration/timing
- Fields: `_radialLayoutGroup: AillieoUtils.UI.RadialLayoutGroup`, `_transitionAnimator: UnityEngine.Animator`
- Methods: `OnAnimationFinished` @ `0x2053`

### `QuestSlotMachinePanel`
- Extends: `QuestBaseCommonData`
- Probable role: data/config reader or balancing table; animation orchestration/timing; AI timing/shot probability
- Fields: `_spinRemainingText: UnityEngine.UI.Text`, `_spinAvailableOnCloudText: UnityEngine.UI.Text`, `_availableFreeSpinsText: UnityEngine.UI.Text`, `_isRevealAnimationFinished: bool`, `_itemsAlloted: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_transitionAnimator: UnityEngine.Animator`, `MAX_REWARD_ITEMS_IN_GRID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- Methods: `OnPanelRevealAnimationFinish` @ `0x2053`, `updateSpinRemainingUI` @ `0x2053`, `onAnimationFinished` @ `0x2053`, `<OnPanelRevealAnimationFinish>b__54_0` @ `0x2053`

### `SlotMachineActiveState`
- Extends: `System.Enum`
- Nested in: `QuestSlotMachinePanel`
- Probable role: animation orchestration/timing
- Fields: `SkipSpinWheelAnimation: SlotMachineActiveState`

### `<>c`
- Extends: `System.Object`
- Nested in: `QuestSlotMachinePanel`
- Probable role: data/config reader or balancing table; animation orchestration/timing
- Methods: `<OnPanelRevealAnimationFinish>b__54_1` @ `0x2053`

### `SettingsPanel`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing; AI timing/shot probability
- Fields: `_shotMap: UnityEngine.UI.Button`, `_disclaimer: UnityEngine.UI.Button`, `_navButtonAnim: UnityEngine.Animator[]`, `CUSTOMSHOT_DEFENSIVE: string`, `CUSTOMSHOT_RADICAL: string`, `CUSTOMSHOT_BRUTE: string`, `CUSTOMSHOT_BALANCED: string`, `m_ShotMatrix_Defensive_User: elem_0x15`, `m_ShotMatrix_Radical_User: elem_0x15`, `m_ShotMatrix_Brute_User: elem_0x15`, `m_ShotMatrix_Balanced_User: elem_0x15`, `_shotMatrixDict: elem_0x15`
- Methods: `onClickDisclaimer` @ `0x2053`, `onShotMapClicked` @ `0x2053`, `GetShotMapValues` @ `0x2050`, `initUsersShotMatrix` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `ShotMatrixExporter`
- Extends: `System.Object`
- Nested in: `SettingsPanel`
- Probable role: shot selection/evaluation/animation
- Fields: `shotTypes: string[]`
- Methods: `ExportAllShotMatrices` @ `0x2050`

### `<>c__DisplayClass1_0`
- Extends: `System.Object`
- Nested in: `ShotMatrixExporter`
- Probable role: shot selection/evaluation/animation
- Methods: `<ExportAllShotMatrices>b__0` @ `0x4ed8`

### `CloudShotmapPresetController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; animation orchestration/timing; AI timing/shot probability
- Fields: `_presetItem: CloudShotmapPresetItem[]`, `navButtonAnim: UnityEngine.Animator[]`, `_mainPanel: UnityEngine.GameObject`, `_currentBatsmanType: BatsmanType`, `_shotMatrixDict: elem_0x15`, `_initBatsmanMatrixCallback: elem_0x15`
- Methods: `onBatsmanTypeChanged` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `<>c__DisplayClass27_0`
- Extends: `System.Object`
- Nested in: `CloudShotmapPresetController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: CloudShotmapPresetController`, `presetData: BattingPresetData`

### `CloudShotmapPresetItem`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation

### `DirectionArrows`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Fields: `ArrowJoystickDirection: JoystickDirection`

### `ShotmapPanel`
- Extends: `BatsmanAnimationData`
- Probable role: shot selection/evaluation/animation; input handling or control mapping; animation orchestration/timing
- Fields: `_joystickData: JoystickController`, `_shotTypeImage: UnityEngine.UI.Image`, `_ffShotParent: UnityEngine.RectTransform`, `_bfShotParent: UnityEngine.RectTransform`, `_advanceShotParent: UnityEngine.RectTransform`, `_ffProShot: UnityEngine.UI.ButtonToggle`, `_bfProShot: UnityEngine.UI.ButtonToggle`, `_advanceProShot: UnityEngine.UI.ButtonToggle`, `_defensivePreset: ShotmapPresetController`, `_radicalPreset: ShotmapPresetController`, `_brutePreset: ShotmapPresetController`, `_balancedPreset: ShotmapPresetController`, `_shotItemPrefab: ShotmapProShotItem`, `_shotData: BattingSpecificShotTesting`, `_cloudShotmapPreset: CloudShotmapPresetController`, `_currentBatsmanType: BatsmanType`, `_currentShotType: BatsmanShotType`, `_currentJoystickDirection: JoystickDirection`, `_currentActivePresetController: ShotmapPresetController`, `_currentAnimationIndex: AnimationIndex`, `_playerAnim: UnityEngine.Animator`, `_playerAnimOverride: UnityEngine.AnimatorOverrideController`, `_animationCR: UnityEngine.Coroutine`, `_shotDataForDefensive: elem_0x15`, `_shotDataForBalanced: elem_0x15`, `_shotDataForBrute: elem_0x15`, `_shotDataForRadical: elem_0x15`, `_shotDataForDefensiveF: elem_0x15`, `_shotDataForBalancedF: elem_0x15`, `_shotDataForBruteF: elem_0x15`
- Methods: `onJoystickAngleUpdated` @ `0x2053`, `onBatsmanTypeChanged` @ `0x2053`, `batsmanTypeChanged` @ `0x2053`, `onShotTypeChanged` @ `0x2053`, `shotTypeChanged` @ `0x2053`, `onLeftProShotArrowClicked` @ `0x2053`, `onRightProShotArrowClicked` @ `0x2053`, `onCurrentProShotChanged` @ `0x2053`, `initBatsmanTypePresets` @ `0x2053`, `copyUserPresetShotData` @ `0x2053`, `updateShotTypeImage` @ `0x2053`, `copyUserShotData` @ `0x2053`, `initUsersShotMatrix` @ `0x2053`, `saveUsersShotMatrix` @ `0x2053`, `updateUserShotMatrix` @ `0x2053`, `updateProShotUI` @ `0x2053`, `loadAnimFromPool` @ `0x2053`, `updateDefaultShotList` @ `0x2053`, `updateDefaultAndAddOtherShots` @ `0x2053`, `showShotData` @ `0x2053`, `clearPrevShotData` @ `0x2053`, `highlightShotData` @ `0x2053`, `playAnim` @ `0x2053`, `PlayShot` @ `0x2050`, `afterAnimation` @ `0x2053`

### `<>c`
- Extends: `System.Object`
- Nested in: `ShotmapPanel`
- Probable role: shot selection/evaluation/animation
- Methods: `<copyUserPresetShotData>b__118_0` @ `0x4f08`, `<copyUserPresetShotData>b__118_1` @ `0x4f20`

### `<>c__DisplayClass111_0`
- Extends: `System.Object`
- Nested in: `ShotmapPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: ShotmapPanel`

### `<>c__DisplayClass118_0`
- Extends: `System.Object`
- Nested in: `ShotmapPanel`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing
- Fields: `anim: AnimationIndex`
- Methods: `<copyUserPresetShotData>b__2` @ `0x4f50`

### `<>c__DisplayClass136_0`
- Extends: `System.Object`
- Nested in: `ShotmapPanel`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing
- Fields: `animClipName: string`
- Methods: `<PlayShot>b__0` @ `0x4f68`

### `<PlayShot>d__136`
- Extends: `System.Object`
- Nested in: `ShotmapPanel`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing
- Fields: `<>4__this: ShotmapPanel`, `displayAnim: AnimationIndex`

### `ShotmapPreset`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation
- Methods: `SetBatsmanPresetData` @ `0x2053`

### `ShotmapPresetController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation
- Fields: `_presetToggles: ShotmapPreset[]`, `_batsmanType: BatsmanType`
- Methods: `get_BatsmanType` @ `0x4fb0`, `ForceClickBatsmanPresetButton` @ `0x2053`, `onClickBatsmanPresetBtn` @ `0x2053`

### `<>c__DisplayClass8_0`
- Extends: `System.Object`
- Nested in: `ShotmapPresetController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: ShotmapPresetController`

### `ShotmapProShotItem`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; animation orchestration/timing
- Fields: `_shotName: TMPro.TextMeshProUGUI`, `_shotPreview: UnityEngine.UI.Button`, `_animIndex: AnimationIndex`, `_onShotPreviewButtonClicked: elem_0x15`
- Methods: `get_AnimIndex` @ `0x4fe0`, `SetProShotData` @ `0x2053`

### `ShotSearchHandler`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; input handling or control mapping
- Fields: `searchInputField: TMPro.TMP_InputField`
- Methods: `OnSearchInputFieldValueChanged` @ `0x2053`

### `<>c__DisplayClass11_0`
- Extends: `System.Object`
- Nested in: `ShotSearchHandler`
- Probable role: input handling or control mapping
- Fields: `<>4__this: ShotSearchHandler`
- Methods: `<OnSearchInputFieldValueChanged>b__0` @ `0x5010`

### `<>c__DisplayClass11_1`
- Extends: `System.Object`
- Nested in: `ShotSearchHandler`
- Probable role: shot selection/evaluation/animation; input handling or control mapping
- Fields: `shot: ShotConfig`
- Methods: `<OnSearchInputFieldValueChanged>b__1` @ `0x2053`

### `AshesMainMenu`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `AuctionMainMenu`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `batsmanTag: string`, `bowlerTag: string`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `MainMenuCustomTournamentPanel`
- Extends: `PanelController`
- Probable role: data/config reader or balancing table; animation orchestration/timing; AI timing/shot probability
- Fields: `_backButtonAnim: UnityEngine.Animator`, `_nextButtonAnim: UnityEngine.Animator`, `isDiscountProduct: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `_TournamentTier: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_StoreProductID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `<>c__DisplayClass30_0`
- Extends: `System.Object`
- Nested in: `MainMenuCustomTournamentPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenuCustomTournamentPanel`

### `TournamentCreatorTransition`
- Extends: `TC_TransitionData`
- Probable role: input handling or control mapping
- Fields: `tournamentNameIP: TMPro.TMP_InputField`
- Methods: `OnTournamentNameInputFieldEndEdit` @ `0x2053`

### `LicenseTournaments`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_backButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `OngoingTournaments`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_backButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `RcplSquadSelectionContent`
- Extends: `SquadSelectionContent`
- Probable role: AI timing/shot probability
- Fields: `_rcplPanelType: RCPL_BattingOrBowling`, `_selectedSubstitutePlayerDetails: PlayerSelectionBase`, `RCPL_BATTING_TEAM_CAPTAIN_KEY: string`, `RCPL_BOWLING_TEAM_CAPTAIN_KEY: string`

### `RcplSquadSelectionPanel`
- Extends: `SquadSelectionPanel`
- Probable role: AI timing/shot probability
- Fields: `_rcplBattingContent: RcplSquadSelectionContent`, `_rcplBattingAllSquadScrollRect: UnityEngine.UI.ScrollRect`, `_rcplBattingFinal11ScrollRect: UnityEngine.UI.ScrollRect`, `_rcplBattingRaycastBlocker: UnityEngine.GameObject`, `_battingVSS: UnityEngine.UI.Extensions.VerticalScrollSnap`
- Methods: `onClickBatting` @ `0x2053`, `OnClickAppointCaptain` @ `0x2053`

### `RoadTo2020WCSubPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `RoadToRCPLSubPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `RoadToWorldCupSubPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `CampaignModeSelection`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `StadiumDetailsData`
- Extends: `System.Object`
- Nested in: `CampaignModeSelection`
- Probable role: AI timing/shot probability

### `<>c__DisplayClass46_0`
- Extends: `System.Object`
- Nested in: `CampaignModeSelection`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: CampaignModeSelection`

### `<>c__DisplayClass58_0`
- Extends: `System.Object`
- Nested in: `CampaignModeSelection`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: CampaignModeSelection`

### `<>c__DisplayClass59_0`
- Extends: `System.Object`
- Nested in: `CampaignModeSelection`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: CampaignModeSelection`

### `<>c__DisplayClass60_0`
- Extends: `System.Object`
- Nested in: `CampaignModeSelection`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: CampaignModeSelection`

### `RealCricketNews`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TourFixture`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TourHomeMenu`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `m_TourDetailtext: TMPro.TextMeshProUGUI`, `m_TestDetailsHeader: TMPro.TextMeshProUGUI`, `m_TestDetails: TMPro.TextMeshProUGUI`, `m_ODIDetailsHeader: TMPro.TextMeshProUGUI`, `m_ODIDetails: TMPro.TextMeshProUGUI`, `m_T20DetailsHeader: TMPro.TextMeshProUGUI`, `m_T20Details: TMPro.TextMeshProUGUI`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TourPlaying16Selection`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `m_iBattingSkills: int[]`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`, `GetBatsmanType` @ `0x2050`

### `PlayerCategory`
- Extends: `System.Enum`
- Nested in: `TourPlaying16Selection`
- Probable role: name-correlated gameplay/support type
- Fields: `kBatsman: PlayerCategory`, `kBowler: PlayerCategory`

### `<>c__DisplayClass35_0`
- Extends: `System.Object`
- Nested in: `TourPlaying16Selection`
- Probable role: AI timing/shot probability
- Fields: `playerDetails: PlayerDetails`

### `<>c__DisplayClass36_0`
- Extends: `System.Object`
- Nested in: `TourPlaying16Selection`
- Probable role: AI timing/shot probability
- Fields: `playerDetails: PlayerDetails`

### `<InitializeNewItemOfFinal11>d__39`
- Extends: `System.Object`
- Nested in: `TourPlaying16Selection`
- Probable role: AI timing/shot probability
- Fields: `playerDetails: PlayerDetails`

### `TourResult`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TourSquadDetails`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `<InitializeNewItemOfFinal11>d__19`
- Extends: `System.Object`
- Nested in: `TourSquadDetails`
- Probable role: AI timing/shot probability
- Fields: `<>4__this: TourSquadDetails`, `playerDetails: PlayerDetails`

### `TourStatistics`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `battingButton: UnityEngine.UI.ButtonToggle`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`, `SetBattingState` @ `0x2053`

### `TourTeamSelection`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping; AI timing/shot probability
- Methods: `UpdateUserTeamDetail` @ `0x2053`, `OnNavigationInputEvent` @ `0x2053`

### `TournamentMatchSettings`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `_customDifficultyPanel: UnityEngine.RectTransform`, `_difficultyEasy: UnityEngine.UI.ButtonToggle`, `_difficultyMedium: UnityEngine.UI.ButtonToggle`, `_difficultyHard: UnityEngine.UI.ButtonToggle`, `_difficultyExpert: UnityEngine.UI.ButtonToggle`, `_difficultyHardcore: UnityEngine.UI.ButtonToggle`, `_difficultyCustom: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatEasy: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatMedium: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatHard: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatExpert: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBatHardcore: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlEasy: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlMedium: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlHard: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlExpert: UnityEngine.UI.ButtonToggle`, `_difficultyCustomBowlHardcore: UnityEngine.UI.ButtonToggle`, `_difficulty: GameDifficulty[]`, `_maxOversPerBowler: int[]`, `_currentDifficultyIndex: int`, `_currentDifficultyBattingIndex: int`, `_currentDifficultyBowlingIndex: int`
- Methods: `onDifficultyChanged` @ `0x2053`, `onDifficultyCustomBatChanged` @ `0x2053`, `onDifficultyCustomBowlChanged` @ `0x2053`, `onClickCustomDifficultyNext` @ `0x2053`, `showCustomDifficultyPanel` @ `0x2053`

### `TournamentDomesticPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `TournamentFixture`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TournamentInternationalPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `TournamentLevels`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TournamentMainMenu`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_statsAnim: UnityEngine.Animator`, `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `TournamentMainMenu_Conquerors`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_statsAnim: UnityEngine.Animator`, `_navButtonAnim: UnityEngine.Animator`
- Methods: `PlayNavButtonsAnimation` @ `0x2053`

### `TournamentMainMenu_Crusade`
- Extends: `PanelController`
- Probable role: input handling or control mapping; animation orchestration/timing; AI timing/shot probability
- Fields: `_teamAIcon: UnityEngine.UI.Image`, `_teamIconDetail: UnityEngine.UI.Image`, `_wonBarDetail: UnityEngine.UI.Image`, `_lostBarDetail: UnityEngine.UI.Image`, `_totalMatchesDetailText: TMPro.TextMeshProUGUI`, `_wonMatchesDetailText: TMPro.TextMeshProUGUI`, `_lostMatchesDetailText: TMPro.TextMeshProUGUI`, `_remainingMatchesDetailText: TMPro.TextMeshProUGUI`, `_navButtonAnim: UnityEngine.Animator`
- Methods: `cbOnSwipe` @ `0x2053`, `updateDetails` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `TournamentResult`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TournamentResultPanel`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `TournamentResume`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`, `UpdateMatchDetails` @ `0x2053`

### `TournamentStanding`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`, `InitializeNewItemOfTeamDetail` @ `0x2053`

### `TournamentStatistics`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `mainCategory: StatsMainCategories`, `_battingButton: UnityEngine.UI.ButtonToggle`, `_noStatsAvailableText: TMPro.TextMeshProUGUI`, `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`, `onArrowMainCategories` @ `0x2053`

### `StatsMainCategories`
- Extends: `System.Enum`
- Nested in: `TournamentStatistics`
- Probable role: AI timing/shot probability
- Fields: `BATTING: StatsMainCategories`, `BOWLING: StatsMainCategories`

### `StatsSubCategories`
- Extends: `System.Enum`
- Nested in: `TournamentStatistics`
- Probable role: name-correlated gameplay/support type
- Fields: `HIGHEST_BATTING_AVERAGE: StatsSubCategories`

### `TournamentTeamSelection`
- Extends: `PanelController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_userTeamTour: TeamDetailsTournament`, `_opponentTeamTour: TeamDetailsTournament`, `_userTeamTriSeries: TeamDetailsTournament`, `_opponent1TeamTriSeries: TeamDetailsTournament`, `_opponent2TeamTriSeries: TeamDetailsTournament`, `_navButtonAnim: UnityEngine.Animator[]`, `_userBatsmanJerseyMat: UnityEngine.Material`, `_opponent1BatsmanJerseyMat: UnityEngine.Material`, `_opponent2BatsmanJerseyMat: UnityEngine.Material`
- Methods: `OnPanelRevealAnimationFinish` @ `0x2053`, `updateOpponent2TeamDetailForTriSeries` @ `0x2053`, `updateOpponent1TeamDetailForTriSeries` @ `0x2053`, `updateUserTeamDetailForTriSeries` @ `0x2053`, `updateOpponentTeamDetail` @ `0x2053`, `updateUserTeamDetail` @ `0x2053`, `PlayNavButtonsAnimation` @ `0x2053`

### `WTCMainMenu`
- Extends: `PanelController`
- Probable role: AI timing/shot probability

### `WTCPointSystem`
- Extends: `PanelController`
- Probable role: animation orchestration/timing
- Fields: `_navButtonAnim: UnityEngine.Animator[]`
- Methods: `playNavButtonsAnimation` @ `0x2053`

### `Auction_UIController`
- Extends: `UIController`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_isBidAnimBeingPlayed: bool`, `_teamcanRetainCurrentPlayer: int`, `_aiTeams: elem_0x15`, `_aiTeamsMaxBudgetForCurplayer: elem_0x15`
- Methods: `get_TeamcanRetainCurrentPlayer` @ `0x6480`, `decideAiMaxPrices` @ `0x2053`, `EnableFastSpeedGamePlay` @ `0x2053`, `setBidByAi` @ `0x2053`, `setAiBid` @ `0x2050`, `getStraightBackBid` @ `0x2050`, `getRaiseBid` @ `0x2050`, `AskForRaisingBidPostRTM` @ `0x2053`, `OnRichardAskForRaisingBidFinished` @ `0x2053`, `<OnRichardAskForRaisingBidFinished>b__118_0` @ `0x2053`, `<OnRichardAskForRaisingBidFinished>b__118_1` @ `0x2053`, `<OnRichardAskForRaisingBidFinished>b__118_2` @ `0x2053`

### `<>c`
- Extends: `System.Object`
- Nested in: `Auction_UIController`
- Probable role: AI timing/shot probability
- Methods: `<setBidByAi>b__72_0` @ `0x64c8`, `<setBidByAi>b__72_1` @ `0x64e0`

### `<>c__DisplayClass118_0`
- Extends: `System.Object`
- Nested in: `Auction_UIController`
- Probable role: AI timing/shot probability
- Methods: `<OnRichardAskForRaisingBidFinished>b__3` @ `0x64f8`

### `<setAiBid>d__73`
- Extends: `System.Object`
- Nested in: `Auction_UIController`
- Probable role: AI timing/shot probability

### `MainMenu_UIController`
- Extends: `UIController`
- Probable role: AI timing/shot probability
- Fields: `_rankedMainMenuView: RC19.UI.RankedMainMenuView`, `_battStickerShopView: RC19.UI.BatStickerShopView`, `_questContainerData: elem_0x15`
- Methods: `get_RankedMainMenuView` @ `0x2050`, `get_BatStickerShopView` @ `0x2050`, `get_QuestContainerData` @ `0x2050`, `set_QuestContainerData` @ `0x2053`

### `<>c__DisplayClass78_0`
- Extends: `System.Object`
- Nested in: `MainMenu_UIController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: MainMenu_UIController`

### `ZZ_TestBed`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `anim: UnityEngine.Animator`, `ANIM_FOOTER_BUTTONS: string`

### `SquadPanelViewerTool`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_playerMainPanel: UnityEngine.GameObject`, `_playerPoseAnim: UnityEngine.Animator`

### `ShadowHelper`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_MainLight: UnityEngine.Light`

### `DynamicHandshakeIK`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `firstCharacterAnimator: UnityEngine.Animator`, `secondCharacterAnimator: UnityEngine.Animator`
- Methods: `OnAnimatorIK` @ `0x2053`

### `BindingDataHolder`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `OnHandleAnimationPaused: UnityEngine.Events.UnityAction`, `OnHandleAnimationDestroy: UnityEngine.Events.UnityAction`
- Methods: `PlayAnimation` @ `0x2053`, `TriggerAnimationPaused` @ `0x2053`, `TriggerAnimationDestory` @ `0x2053`, `RegisterAnimationPausedEvent` @ `0x2053`, `UnRegisterAnimationPausedEvent` @ `0x2053`, `RegisterAnimationDestroyEvent` @ `0x2053`, `UnRegisterAnimationDestroyEvent` @ `0x2053`

### `BINDING_NAME`
- Extends: `System.Enum`
- Nested in: `BindingDataHolder`
- Probable role: AI timing/shot probability
- Fields: `eBowler: BINDING_NAME`, `eCaptainUser: BINDING_NAME`, `eCaptainOpponent: BINDING_NAME`, `extraBatsman1: BINDING_NAME`, `extraBatsman2: BINDING_NAME`

### `PlayerAppearanceData`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `playerDetails: PlayerDetails`, `enableBall: bool`, `isBatsman: bool`

### `TimeLineManager`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; animation orchestration/timing; AI timing/shot probability
- Fields: `battingTextMaterial: UnityEngine.Material`, `battingTeamJersey: UnityEngine.Material`, `battingTeamJersey0: UnityEngine.Material`, `mIsAnimationIsRunning: bool`, `_IsShotCinematicPlaying: bool`, `mCinemachineBrain: Cinemachine.CinemachineBrain`, `mCinemachineBrains: Cinemachine.CinemachineBrain[]`, `mCinemachineBrainList: elem_0x15`, `OnAnimationFinished: System.Action`, `OnAnimationFinishedWithParam: elem_0x15`, `batsman: UnityEngine.GameObject`
- Methods: `PlayTimeLineAnimation` @ `0x2053`, `OnHandleAnimationPause` @ `0x2053`, `OnHandleAnimationDestroy` @ `0x2053`, `DisableCMBrain_ML` @ `0x2053`, `ForceSkipAnimation` @ `0x2053`, `GetTimelineAnimationRunningStatus` @ `0x6750`

### `<>c`
- Extends: `System.Object`
- Nested in: `TimeLineManager`
- Probable role: animation orchestration/timing
- Methods: `<PlayTimeLineAnimation>b__49_2` @ `0x6798`

### `<>c__DisplayClass49_0`
- Extends: `System.Object`
- Nested in: `TimeLineManager`
- Probable role: animation orchestration/timing
- Methods: `<PlayTimeLineAnimation>b__0` @ `0x67b0`, `<PlayTimeLineAnimation>b__1` @ `0x67c8`

### `TimelineSignals`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Methods: `ShowBatCall` @ `0x2053`, `BattingDRSTaken` @ `0x2053`, `BattingDRSCancled` @ `0x2053`, `DisableBatsmanStat` @ `0x2053`, `EnableBatsmanStat` @ `0x2053`, `EnableStrikerLeftBat` @ `0x2053`, `EnableStrikerRightBat` @ `0x2053`, `EnableNonStrikerLeftBat` @ `0x2053`, `EnableNonStrikerRightBat` @ `0x2053`

### `TimelineType`
- Extends: `System.Enum`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `Sachin_Celebration_Raise_Bat: TimelineType`, `BowlerEntry: TimelineType`, `OtherBatsMan_Out: TimelineType`, `Two_Batsman_Entry: TimelineType`, `Batsman_Win_Reaction: TimelineType`, `Batsman_Lose_Reaction: TimelineType`, `Batsman_50_100_Celebration: TimelineType`, `Batsman_Celebration_Boundary: TimelineType`, `Batsman_Lose_Exit: TimelineType`, `Two_Batsman_Entry_Without_Fielder: TimelineType`, `Static_Cam_Anim: TimelineType`

### `TimelineTool`
- Extends: `System.Object`
- Probable role: animation orchestration/timing
- Methods: `SetAnimationClip` @ `0x2053`, `SetAnimationClips` @ `0x2053`

### `BatsmanAnimInfo`
- Extends: `System.Object`
- Probable role: animation orchestration/timing
- Fields: `AnimIndex: AnimationIndex`, `PerfectFrameTime: float`, `PerfectFrameTimeFixed: float`, `AnimationSpeed: float`, `BatPositionWorldRight: UnityEngine.Vector3`, `BatPositionWorldLeft: UnityEngine.Vector3`

### `BattingShotDataGenerator`
- Extends: `BatsmanAnimationData`
- Probable role: shot selection/evaluation/animation; input handling or control mapping; animation orchestration/timing
- Fields: `mBattingSpecificShotTesting: BattingSpecificShotTesting`, `mShotNameText: UnityEngine.UI.Text`, `mSpecificText: UnityEngine.UI.InputField`, `_AnimSpeedInputField: UnityEngine.UI.InputField`, `mAnimator: UnityEngine.Animator`, `overrideController: UnityEngine.AnimatorOverrideController`, `shotClips: elem_0x15`, `mCurrentAnimIndex: int`, `holderList: BattingShotDataHolder[]`, `_AnimMultiplier: float`, `LBatSweetSpot: UnityEngine.Transform`, `RBatSweetSpot: UnityEngine.Transform`, `index: AnimationIndex`, `advanceSettleClips: UnityEngine.AnimationClip[]`, `advanceSettleClips_L: UnityEngine.AnimationClip[]`, `afterAdvanceSettleClips: UnityEngine.AnimationClip[]`, `afterAdvanceSettleClips_L: UnityEngine.AnimationClip[]`, `L_Bat: UnityEngine.GameObject`, `R_Bat: UnityEngine.GameObject`, `mf_BatsmanMoveTimeCounter: float`
- Methods: `PlayAnim` @ `0x2053`, `OnAnimationFinished` @ `0x2053`, `GetAnimFromPool` @ `0x2053`, `OnAnimationFinishedWithParam` @ `0x2053`, `ControlShot` @ `0x2050`, `SetBatsman` @ `0x2053`, `OnBatsmanMovePositionChange` @ `0x2053`, `<ControlShot>b__47_0` @ `0x68e8`

### `<>c__DisplayClass35_0`
- Extends: `System.Object`
- Nested in: `BattingShotDataGenerator`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattingShotDataGenerator`

### `<ControlShot>d__47`
- Extends: `System.Object`
- Nested in: `BattingShotDataGenerator`
- Probable role: shot selection/evaluation/animation; AI timing/shot probability
- Fields: `<>4__this: BattingShotDataGenerator`, `aIncrement: int`

### `<StartProcessForRecord>d__35`
- Extends: `System.Object`
- Nested in: `BattingShotDataGenerator`
- Probable role: animation orchestration/timing
- Fields: `<>4__this: BattingShotDataGenerator`, `<animCount>5__3: int`

### `BattingSpecificShotTesting`
- Extends: `UnityEngine.ScriptableObject`
- Probable role: shot selection/evaluation/animation
- Fields: `ShotIndexInBottomList: int`, `mSpecificTiming: SpecificTiming`, `mBattingShotDataHolder: elem_0x15`
- Methods: `GetSelectedShotData` @ `0x2050`

### `SpecificTiming`
- Extends: `System.Enum`
- Nested in: `BattingSpecificShotTesting`
- Probable role: name-correlated gameplay/support type
- Fields: `eNone: SpecificTiming`, `eEarly: SpecificTiming`, `eEarlyPerfect: SpecificTiming`, `ePerfect: SpecificTiming`, `eLatePerfect: SpecificTiming`, `eLate: SpecificTiming`, `eOutsideEdge: SpecificTiming`, `eInsideEdge: SpecificTiming`

### `BattingShotDataHolder`
- Extends: `System.Object`
- Probable role: shot selection/evaluation/animation; animation orchestration/timing
- Fields: `ShotName: string`, `ShotIndex: int`, `_AnimationIndex: AnimationIndex`, `perfectFrameTime: float`, `perfectFrameTimeFixed: float`, `shotType: ShotType`, `batsmanType: string`, `proShotType: string`, `isPremiumShot: int`, `animationSpeed: float`, `BatPositionWorldRight: UnityEngine.Vector3`, `BatPositionWorldLeft: UnityEngine.Vector3`

### `FillShotData`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation
- Fields: `shotTesting: BattingSpecificShotTesting`

### `JsonTestScript`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Methods: `DisplayFail` @ `0x2053`

### `KeychainPluginPath`
- Extends: `UnityEngine.ScriptableObject`
- Probable role: AI timing/shot probability

### `FxPro`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `FilmGrainIntensity: float`, `FilmGrainTiling: float`, `_filmGrainTextures: elem_0x15`
- Methods: `UpdateFilmGrain` @ `0x2053`

### `WMG_Axis_Graph`
- Extends: `WMG_Graph_Manager`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `tooltipAnimationsEnabled: bool`, `tooltipAnimationsEasetype: DG.Tweening.Ease`, `tooltipAnimationsDuration: float`, `autoAnimationsEasetype: DG.Tweening.Ease`, `autoAnimationsDuration: float`, `_autoAnimationsEnabled: bool`, `cachedContainerWidth: float`, `cachedContainerHeight: float`, `autoAnim: WMG_Graph_Auto_Anim`, `autoAnimEnabledC: WMG_Change_Obj`
- Methods: `get_autoAnimationsEnabled` @ `0x6c78`, `set_autoAnimationsEnabled` @ `0x2053`, `AutoAnimationsEnabledChanged` @ `0x2053`, `UpdateAutoAnimEvents` @ `0x2053`, `animScaleAllAtOnce` @ `0x2053`, `animScaleBySeries` @ `0x2053`, `animScaleOneByOne` @ `0x2053`, `UpdateFromContainer` @ `0x2053`

### `WMG_Hierarchical_Tree`
- Extends: `WMG_Graph_Manager`
- Probable role: AI timing/shot probability
- Fields: `cachedContainerWidth: float`, `cachedContainerHeight: float`
- Methods: `UpdateFromContainer` @ `0x2053`

### `WMG_Pie_Graph`
- Extends: `WMG_Graph_Manager`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `_animationDuration: float`, `_sortAnimationDuration: float`, `cachedContainerWidth: float`, `cachedContainerHeight: float`, `animSortSwap: bool`, `isAnimating: bool`
- Methods: `get_animationDuration` @ `0x7158`, `set_animationDuration` @ `0x2053`, `get_sortAnimationDuration` @ `0x7170`, `set_sortAnimationDuration` @ `0x2053`, `UpdateFromContainer` @ `0x2053`, `endSortAnimating` @ `0x2053`

### `WMG_Ring_Graph`
- Extends: `WMG_Graph_Manager`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `animateData: bool`, `animDuration: float`, `animEaseType: DG.Tweening.Ease`, `containerWidthCached: float`, `containerHeightCached: float`

### `WMG_Anim`
- Extends: `System.Object`
- Probable role: animation orchestration/timing
- Methods: `animFill` @ `0x2053`, `animColor` @ `0x2053`, `animRotation` @ `0x2053`, `animRotationCallbackC` @ `0x2053`, `animRotationCallbackU` @ `0x2053`, `animRotationCallbacks` @ `0x2053`, `animPositionCallbackC` @ `0x2053`, `animPosition` @ `0x2053`, `animSize` @ `0x2053`, `animPositionCallbacks` @ `0x2053`, `animScale` @ `0x2053`, `animScaleCallbackC` @ `0x2053`, `animScaleSeqInsert` @ `0x2053`, `animScaleSeqAppend` @ `0x2053`, `animInt` @ `0x2053`, `animFloat` @ `0x2053`, `animFloatCallbackU` @ `0x2053`, `animFloatCallbacks` @ `0x2053`, `animVec2` @ `0x2053`, `animVec2CallbackU` @ `0x2053`

### `<>c__DisplayClass0_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animFill>b__0` @ `0x7860`, `<animFill>b__1` @ `0x2053`

### `<>c__DisplayClass10_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animScale>b__0` @ `0x7878`, `<animScale>b__1` @ `0x2053`

### `<>c__DisplayClass11_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animScaleCallbackC>b__0` @ `0x7890`, `<animScaleCallbackC>b__1` @ `0x2053`

### `<>c__DisplayClass12_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animScaleSeqInsert>b__0` @ `0x78a8`, `<animScaleSeqInsert>b__1` @ `0x2053`

### `<>c__DisplayClass13_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animScaleSeqAppend>b__0` @ `0x78c0`, `<animScaleSeqAppend>b__1` @ `0x2053`

### `<>c__DisplayClass1_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animColor>b__0` @ `0x78d8`, `<animColor>b__1` @ `0x2053`

### `<>c__DisplayClass6_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animPositionCallbackC>b__0` @ `0x78f0`, `<animPositionCallbackC>b__1` @ `0x2053`

### `<>c__DisplayClass7_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animPosition>b__0` @ `0x7908`, `<animPosition>b__1` @ `0x2053`

### `<>c__DisplayClass8_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animSize>b__0` @ `0x7920`, `<animSize>b__1` @ `0x2053`

### `<>c__DisplayClass9_0`
- Extends: `System.Object`
- Nested in: `WMG_Anim`
- Probable role: animation orchestration/timing
- Methods: `<animPositionCallbacks>b__0` @ `0x7938`, `<animPositionCallbacks>b__1` @ `0x2053`

### `WMG_Graph_Tooltip`
- Extends: `WMG_GUI_Functions`
- Probable role: animation orchestration/timing
- Methods: `performTooltipAnimation` @ `0x2053`

### `WMG_Graph_Auto_Anim`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Methods: `addSeriesForAutoAnim` @ `0x2053`, `SeriesAutoAnimStartedMethod` @ `0x2053`, `onAutoAnimUpdate` @ `0x2053`, `onAutoAnimComplete` @ `0x2053`

### `<>c__DisplayClass3_0`
- Extends: `System.Object`
- Nested in: `WMG_Graph_Auto_Anim`
- Probable role: animation orchestration/timing
- Fields: `<>4__this: WMG_Graph_Auto_Anim`
- Methods: `<SeriesAutoAnimStartedMethod>b__0` @ `0x2053`, `<SeriesAutoAnimStartedMethod>b__1` @ `0x2053`, `<SeriesAutoAnimStartedMethod>b__2` @ `0x2053`

### `WMG_Ring`
- Extends: `WMG_GUI_Functions`
- Probable role: animation orchestration/timing
- Fields: `animTimeline: float`
- Methods: `animBandFill` @ `0x2053`, `onUpdateAnimateBandFill` @ `0x2053`

### `<>c__DisplayClass31_0`
- Extends: `System.Object`
- Nested in: `WMG_Ring`
- Probable role: animation orchestration/timing
- Methods: `<animBandFill>b__0` @ `0x84d8`, `<animBandFill>b__1` @ `0x2053`, `<animBandFill>b__2` @ `0x2053`

### `WMG_Series`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `beginningToAutoAnimate: bool`, `<currentlyAnimating>k__BackingField: bool`, `<autoAnimationTimeline>k__BackingField: float`, `tooltipPointAnimator: TooltipPointAnimator`, `SeriesAutoAnimStarted: SeriesAutoAnimStartedHandler`
- Methods: `get_autoAnimTweenId` @ `0x2050`, `get_currentlyAnimating` @ `0x8868`, `set_currentlyAnimating` @ `0x2053`, `get_autoAnimationTimeline` @ `0x8880`, `set_autoAnimationTimeline` @ `0x2053`, `defaultTooltipPointAnimator` @ `0x2053`, `add_SeriesAutoAnimStarted` @ `0x2053`, `remove_SeriesAutoAnimStarted` @ `0x2053`, `OnSeriesAutoAnimStarted` @ `0x2053`, `setAnimatingFromPreviousData` @ `0x2053`

### `TooltipPointAnimator`
- Extends: `System.MulticastDelegate`
- Nested in: `WMG_Series`
- Probable role: animation orchestration/timing

### `SeriesAutoAnimStartedHandler`
- Extends: `System.MulticastDelegate`
- Nested in: `WMG_Series`
- Probable role: animation orchestration/timing

### `SkeletonIRVExample`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Methods: `waitForNetwork` @ `0x2050`

### `<waitForNetwork>d__4`
- Extends: `System.Object`
- Nested in: `SkeletonIRVExample`
- Probable role: AI timing/shot probability

### `InternetReachabilityVerifier`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_yieldWaitStart: float`
- Methods: `waitForNetVerifiedStatus` @ `0x2050`, `internal_yieldWait` @ `0x89d0`, `IsNetworkAvailable` @ `0x89e8`

### `<waitForNetVerifiedStatus>d__35`
- Extends: `System.Object`
- Nested in: `InternetReachabilityVerifier`
- Probable role: AI timing/shot probability

### `ChatGui`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Fields: `InputFieldChat: UnityEngine.UI.InputField`

### `NamePickGui`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Fields: `idInput: UnityEngine.UI.InputField`

### `DemoControls`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `batchLeft: ProFlareBatch`, `batchRight: ProFlareBatch`

### `MultiCameraDemo`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `batch: ProFlareBatch`

### `PresetViewer`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `MainCamera: UnityEngine.Camera`

### `SwitchCameraDemo`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `flareBatch: ProFlareBatch`

### `ProFlareElement`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `ScaleCurve: UnityEngine.AnimationCurve`

### `ProFlare`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `FlareBatches: ProFlareBatch[]`, `AngleCurve: UnityEngine.AnimationCurve`, `DynamicEdgeCurve: UnityEngine.AnimationCurve`
- Methods: `PopulateFlareBatches` @ `0x2053`

### `ProFlareBatch`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component

### `DemoScene1`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `rainControllers: elem_0x15`, `rainAlpha: float`

### `PlayMode`
- Extends: `System.Enum`
- Nested in: `DemoScene1`
- Probable role: AI timing/shot probability
- Fields: `Rain: PlayMode`

### `DemoScene2`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `bloodRainController: BloodRainCameraController`, `splashInRain: RainCameraController`, `splashOutRain: RainCameraController`, `frozenRain: RainCameraController`, `rainAlpha: float`

### `RainCameraController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `_rainBehaviours: elem_0x15`, `ShaderType: RainDropShaderType`
- Methods: `get_rainBehaviours` @ `0x2050`

### `DropTrail`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `widthCurve: UnityEngine.AnimationCurve`, `_trail: UnityEngine.GameObject`
- Methods: `UpdateTrail` @ `0x2053`, `<UpdateTrail>b__25_0` @ `0x8bc8`

### `RainBehaviourBase`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `ShaderType: RainDropShaderType`
- Methods: `StartRain` @ `0x2053`, `StopRain` @ `0x2053`, `StopRainImmidiate` @ `0x2053`

### `RainDrawerContainer`1`
- Extends: `System.Object`
- Probable role: AI timing/shot probability

### `RainDropTools`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Methods: `CreateRainMaterial` @ `0x2050`, `ApplyRainMaterialValue` @ `0x2053`

### `RainDropShaderType`
- Extends: `System.Enum`
- Nested in: `RainDropTools`
- Probable role: AI timing/shot probability
- Fields: `Expensive: RainDropShaderType`, `Cheap: RainDropShaderType`, `NoDistortion: RainDropShaderType`

### `BloodRainCameraController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `FrameBloodCamera: RainCameraController`, `SplatterBloodCamera: RainCameraController`, `FrameEffectInterval: float`, `hpHigh: UnityEngine.AnimationCurve`, `hpMid: UnityEngine.AnimationCurve`, `hpLow: UnityEngine.AnimationCurve`

### `FlowRainBehaviour`
- Extends: `RainBehaviourBase`
- Probable role: AI timing/shot probability
- Fields: `<rainController>k__BackingField: FlowRainController`, `Variables: FlowRainVariables`
- Methods: `get_rainController` @ `0x2050`, `set_rainController` @ `0x2053`, `StartRain` @ `0x2053`, `StopRain` @ `0x2053`, `StopRainImmidiate` @ `0x2053`

### `FlowRainController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; AI timing/shot probability
- Fields: `<Variables>k__BackingField: FlowRainVariables`, `<NoMoreRain>k__BackingField: bool`, `<ShaderType>k__BackingField: RainDropShaderType`, `isOneShot: bool`, `isWaitingDelay: bool`, `oneShotTimeleft: float`
- Methods: `get_NoMoreRain` @ `0x8df0`, `set_NoMoreRain` @ `0x2053`, `Wait` @ `0x2050`

### `FlowRainDrawerContainer`
- Extends: `TypeSpec`
- Nested in: `FlowRainController`
- Probable role: AI timing/shot probability

### `<>c__DisplayClass56_0`
- Extends: `System.Object`
- Nested in: `FlowRainController`
- Probable role: name-correlated gameplay/support type
- Fields: `dc: FlowRainDrawerContainer`, `<>4__this: FlowRainController`

### `<PlayDelay>d__49`
- Extends: `System.Object`
- Nested in: `FlowRainController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: FlowRainController`

### `<Wait>d__59`
- Extends: `System.Object`
- Nested in: `FlowRainController`
- Probable role: AI timing/shot probability

### `FlowRainVariables`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `MaxRainSpawnCount: int`, `AlphaOverLifetime: UnityEngine.AnimationCurve`, `TrailWidth: UnityEngine.AnimationCurve`, `DistortionOverLifetime: UnityEngine.AnimationCurve`, `ReliefOverLifetime: UnityEngine.AnimationCurve`, `BlurOverLifetime: UnityEngine.AnimationCurve`

### `FrictionFlowRainBehaviour`
- Extends: `RainBehaviourBase`
- Probable role: AI timing/shot probability
- Fields: `<rainController>k__BackingField: FrictionFlowRainController`, `Variables: FrictionFlowRainVariables`
- Methods: `get_rainController` @ `0x2050`, `set_rainController` @ `0x2053`, `StartRain` @ `0x2053`, `StopRain` @ `0x2053`, `StopRainImmidiate` @ `0x2053`

### `FrictionFlowRainController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; AI timing/shot probability
- Fields: `<Variables>k__BackingField: FrictionFlowRainVariables`, `<NoMoreRain>k__BackingField: bool`, `<ShaderType>k__BackingField: RainDropShaderType`, `isOneShot: bool`, `isWaitingDelay: bool`, `oneShotTimeleft: float`
- Methods: `get_NoMoreRain` @ `0x9030`, `set_NoMoreRain` @ `0x2053`

### `FrictionFlowRainDrawerContainer`
- Extends: `TypeSpec`
- Nested in: `FrictionFlowRainController`
- Probable role: AI timing/shot probability

### `<PlayDelay>d__52`
- Extends: `System.Object`
- Nested in: `FrictionFlowRainController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: FrictionFlowRainController`

### `FrictionFlowRainVariables`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `MaxRainSpawnCount: int`, `AlphaOverLifetime: UnityEngine.AnimationCurve`, `TrailWidth: UnityEngine.AnimationCurve`, `DistortionOverLifetime: UnityEngine.AnimationCurve`, `ReliefOverLifetime: UnityEngine.AnimationCurve`, `BlurOverLifetime: UnityEngine.AnimationCurve`

### `SimpleRainBehaviour`
- Extends: `RainBehaviourBase`
- Probable role: AI timing/shot probability
- Fields: `<rainController>k__BackingField: SimpleRainController`, `Variables: SimpleRainVariables`
- Methods: `get_rainController` @ `0x2050`, `set_rainController` @ `0x2053`, `StartRain` @ `0x2053`, `StopRain` @ `0x2053`, `StopRainImmidiate` @ `0x2053`

### `SimpleRainController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; shot selection/evaluation/animation; AI timing/shot probability
- Fields: `<Variables>k__BackingField: SimpleRainVariables`, `<NoMoreRain>k__BackingField: bool`, `<ShaderType>k__BackingField: RainDropShaderType`, `isOneShot: bool`, `oneShotTimeleft: float`, `isWaitingDelay: bool`
- Methods: `get_NoMoreRain` @ `0x92d0`, `set_NoMoreRain` @ `0x2053`

### `SimpleRainDrawerContainer`
- Extends: `TypeSpec`
- Nested in: `SimpleRainController`
- Probable role: AI timing/shot probability

### `<PlayDelay>d__45`
- Extends: `System.Object`
- Nested in: `SimpleRainController`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: SimpleRainController`

### `SimpleRainVariables`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `MaxRainSpawnCount: int`, `AlphaOverLifetime: UnityEngine.AnimationCurve`, `SizeOverLifetime: UnityEngine.AnimationCurve`, `DistortionOverLifetime: UnityEngine.AnimationCurve`, `ReliefOverLifetime: UnityEngine.AnimationCurve`, `BlurOverLifetime: UnityEngine.AnimationCurve`, `PosYOverLifetime: UnityEngine.AnimationCurve`

### `StaticRainBehaviour`
- Extends: `RainBehaviourBase`
- Probable role: AI timing/shot probability
- Fields: `<rainController>k__BackingField: StaticRainController`, `Variables: StaticRainVariables`
- Methods: `get_rainController` @ `0x2050`, `set_rainController` @ `0x2053`, `StartRain` @ `0x2053`, `StopRain` @ `0x2053`, `StopRainImmidiate` @ `0x2053`

### `StaticRainController`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `<Variables>k__BackingField: StaticRainVariables`, `<NoMoreRain>k__BackingField: bool`, `<ShaderType>k__BackingField: RainDropShaderType`, `staticDrawer: StaticRainDrawerContainer`
- Methods: `get_NoMoreRain` @ `0x9480`, `set_NoMoreRain` @ `0x2053`

### `StaticRainDrawerContainer`
- Extends: `TypeSpec`
- Nested in: `StaticRainController`
- Probable role: AI timing/shot probability

### `StaticRainVariables`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `FadeinCurve: UnityEngine.AnimationCurve`

### `FTUEPopUp`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `_LoadingAnimation: UnityEngine.GameObject`, `RankedTeam_AssignCaptain: string`
- Methods: `LoadingAnimation` @ `0x2053`

### `SpriteContainer`
- Extends: `TypeSpec`
- Probable role: AI timing/shot probability

### `StringExtensions`
- Extends: `System.Object`
- Probable role: animation orchestration/timing
- Methods: `FormatForEllipsisAnimation` @ `0x2050`

### `EventManager`
- Extends: `System.Object`
- Probable role: name-correlated gameplay/support type
- Fields: `parameterizedEventDictionary: elem_0x15`

### `SelectionChars`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `animator: UnityEngine.Animator`
- Methods: `playAnim` @ `0x2053`

### `AnimTag`
- Extends: `System.Enum`
- Nested in: `SelectionChars`
- Probable role: animation orchestration/timing
- Fields: `StartConversation: AnimTag`, `AnswerYes: AnimTag`, `AnswerNo: AnimTag`

### `CharacterType`
- Extends: `System.Enum`
- Nested in: `SelectionChars`
- Probable role: AI timing/shot probability
- Fields: `Captain: CharacterType`

### `AddFriendPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Methods: `RaiseRequestStateChange` @ `0x9540`

### `AiroplaneBehaviour`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `AirplaneSound: UnityEngine.AudioSource`, `AirplaneSoundClip: UnityEngine.AudioClip`, `IsAirplaneSoundPlayed: bool`

### `<FadeOut>d__31`
- Extends: `System.Object`
- Nested in: `AiroplaneBehaviour`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: AiroplaneBehaviour`

### `<MoveAndZoomCamera>d__40`
- Extends: `System.Object`
- Nested in: `AiroplaneBehaviour`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: AiroplaneBehaviour`

### `<ZoomCamera>d__41`
- Extends: `System.Object`
- Nested in: `AiroplaneBehaviour`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: AiroplaneBehaviour`

### `<ZoomSequence>d__36`
- Extends: `System.Object`
- Nested in: `AiroplaneBehaviour`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: AiroplaneBehaviour`

### `<ZoomSequenceSameSpot>d__37`
- Extends: `System.Object`
- Nested in: `AiroplaneBehaviour`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: AiroplaneBehaviour`

### `<scalePlane>d__42`
- Extends: `System.Object`
- Nested in: `AiroplaneBehaviour`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: AiroplaneBehaviour`

### `BusBehaviour`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `animator: UnityEngine.Animator`

### `CoopPlayWithFriendsView`
- Extends: `RC19.UI.AnimatableState`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `WAITING_FOR_FRIEND_TO_ACCEPT: string`, `m_AIDetailsRoot: UnityEngine.Transform`, `m_UserDetailsRoot: UnityEngine.Transform`, `m_CoUserDetailsRoot: UnityEngine.Transform`
- Methods: `OnFriendRankDataFetchFailed` @ `0x2053`, `OnHideAnimationFinish` @ `0x2053`

### `FriendProfilePanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `FAILED_RECIVE_RESPONSE: string`, `MAX_REMOVEFRIEND_WAIT_TIME: int`

### `Mode2Pvs2PListContainer`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `HasChildConstraint: bool`

### `Mode2PVs2PPlayerGroupView`
- Extends: `RC19.UI.AnimatableState`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `userDetails: Mode2PVs2PUserDetails[]`, `Team1GroupingContainer: UnityEngine.Transform`, `Team2GroupingContainer: UnityEngine.Transform`
- Methods: `OnHideAnimationFinish` @ `0x2053`

### `Mode2PVs2PPlayWithFriendsView`
- Extends: `RC19.UI.AnimatableState`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `WAITING_FOR_FRIEND_TO_ACCEPT: string`
- Methods: `UpdateInvitedUserDetails` @ `0x2053`, `OnHideAnimationFinish` @ `0x2053`, `SwitchToMainMenu` @ `0x2053`, `WaitForMasterIDData` @ `0x2050`

### `<>c`
- Extends: `System.Object`
- Nested in: `Mode2PVs2PPlayWithFriendsView`
- Probable role: AI timing/shot probability
- Methods: `<WaitForMasterIDData>b__76_0` @ `0x97f8`

### `<WaitForMasterIDData>d__76`
- Extends: `System.Object`
- Nested in: `Mode2PVs2PPlayWithFriendsView`
- Probable role: AI timing/shot probability

### `Mode2PVs2PUserDetails`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `originalContainer: UnityEngine.Transform`

### `<>c__DisplayClass16_0`
- Extends: `System.Object`
- Nested in: `Mode2PVs2PUserDetails`
- Probable role: AI timing/shot probability
- Fields: `mode2Pvs2PContainer1: Mode2Pvs2PListContainer`, `<>4__this: Mode2PVs2PUserDetails`

### `PlayWithFriendsView`
- Extends: `RC19.UI.AnimatableState`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `friendsCode: UnityEngine.UI.InputField`, `WAITING_FOR_FRIEND_TO_ACCEPT: string`
- Methods: `OnFriendRankDataFetchFailed` @ `0x2053`, `OnHideAnimationFinish` @ `0x2053`

### `HighlightsMenuView`
- Extends: `RC19.UI.AnimatableState`
- Probable role: name-correlated gameplay/support type

### `IAirplaneBehaviour`
- Extends: `None`
- Probable role: AI timing/shot probability

### `JoinRoomPanel`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Fields: `roomIDInput: TMPro.TMP_InputField`

### `JoinRoomPanelCoop`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Fields: `roomIDInput: UnityEngine.UI.InputField`

### `PingStatusView`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: name-correlated gameplay/support type

### `StadiumPOI`
- Extends: `System.Object`
- Probable role: animation orchestration/timing
- Fields: `animator: UnityEngine.Animator`

### `RCPLTeams`
- Extends: `System.Enum`
- Nested in: `StadiumPOI`
- Probable role: AI timing/shot probability
- Fields: `CHENNAI: RCPLTeams`, `MUMBAI: RCPLTeams`

### `ThumbToggleAnimator`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing

### `TravelToStadiumView`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `airRouteStadiums: elem_0x15`

### `CurrencyEditor`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; input handling or control mapping
- Fields: `inputField: UnityEngine.UI.InputField`

### `MultiplayerSimulator`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `stats_runs: UnityEngine.UI.InputField`, `stats_wickets: UnityEngine.UI.InputField`, `result_stats: UnityEngine.UI.InputField`

### `JailbreakCheckerDemo`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; AI timing/shot probability
- Fields: `IsNotJailbroken: string`

### `JailbreakChecker`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Methods: `IsJailbroken` @ `0x9d08`

### `RootJailbreakChecker`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Methods: `IsDeviceRootedOrJailbroken` @ `0x9d20`

### `AIBattingBalancingData`
- Extends: `UnityEngine.ScriptableObject`
- Probable role: AI timing/shot probability

### `EconomyHandler`
- Extends: `TypeSpec`
- Probable role: AI timing/shot probability
- Methods: `IsTournamentUnlockedThroughTutorialDailyRewards` @ `0x9dc8`, `GetSelectedBatItem` @ `0x9e58`, `GetSelectedBallItem` @ `0x9e70`

### `Items`
- Extends: `System.Object`
- Nested in: `EconomyHandler`
- Probable role: name-correlated gameplay/support type
- Fields: `bat_stickers: int`, `bat: int`, `ball: int`

### `<>c__DisplayClass33_0`
- Extends: `System.Object`
- Nested in: `EconomyHandler`
- Probable role: AI timing/shot probability
- Methods: `<IsTournamentUnlockedThroughTutorialDailyRewards>b__0` @ `0xa290`

### `GameEconomyAnalytics`
- Extends: `TypeSpec`
- Probable role: AI timing/shot probability
- Fields: `m_Exp: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<RewardMultiplier>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- Methods: `get_ExpGained` @ `0xa3c8`

### `AnalyticsType`
- Extends: `System.Enum`
- Nested in: `GameEconomyAnalytics`
- Probable role: name-correlated gameplay/support type
- Fields: `UserBallsFaced: AnalyticsType`

### `MatchGoalStatsType`
- Extends: `System.Enum`
- Probable role: AI timing/shot probability
- Fields: `MaidenOvers: MatchGoalStatsType`, `BatsmanBowled: MatchGoalStatsType`, `BatsmanLBW: MatchGoalStatsType`, `BatsmanEdgeOut: MatchGoalStatsType`, `MaidenWicket: MatchGoalStatsType`, `BallsBowled: MatchGoalStatsType`, `BallsFaced: MatchGoalStatsType`, `FastestCenturyBalls: MatchGoalStatsType`, `FastestDoubleCenturyBalls: MatchGoalStatsType`, `ScoredSixOnFirstBall: MatchGoalStatsType`, `TakenWicketOnFirstBall: MatchGoalStatsType`

### `GameGoals`
- Extends: `TypeSpec`
- Probable role: AI timing/shot probability
- Methods: `GetGoalDetails` @ `0x2050`

### `MatchGoal`
- Extends: `System.Enum`
- Nested in: `GameGoals`
- Probable role: AI timing/shot probability
- Fields: `Test_Bowl8Maidens: MatchGoal`, `BatFirstAndPlayEntire10Overs: MatchGoal`, `Test_Bowl10Maidens: MatchGoal`, `BatFirstAndPlayEntire20Overs: MatchGoal`, `BowlAMaidenIn50Overs: MatchGoal`, `Test_Bowl3WicketMaidens: MatchGoal`, `Test_Bowl5WicketMaidens: MatchGoal`, `BowlAMaidenIn20Overs: MatchGoal`, `Bowl8MaidensIn50Overs: MatchGoal`, `BowlAMaidenIn10Overs: MatchGoal`, `Bowl2MaidensIn10Overs: MatchGoal`, `Bowl4MaidensIn20Overs: MatchGoal`, `BatFirstAndPlayEntire50Overs: MatchGoal`, `Bowl15MaidensIn50Overs: MatchGoal`, `Bowl8MaidensIn20Overs: MatchGoal`, `Bowl5MaidensIn10Overs: MatchGoal`

### `TournamentGoal`
- Extends: `System.Enum`
- Nested in: `GameGoals`
- Probable role: AI timing/shot probability
- Fields: `Score500RunsWithOneBatsmanInTournamentX: TournamentGoal`, `Score1CenturyWithOneBatsmanInTournamentX: TournamentGoal`, `MaintainAverage50RunsOpeningPartnershipInTournamentX: TournamentGoal`, `GetThree5WicketHaulsWithOneBowlerInTournamentX: TournamentGoal`

### `Params`
- Extends: `System.Object`
- Nested in: `GameGoals`
- Probable role: AI timing/shot probability
- Fields: `<Maidens>k__BackingField: int`
- Methods: `get_Maidens` @ `0xa410`, `set_Maidens` @ `0x2053`

### `MatchGoalStatsPrefs`
- Extends: `System.Object`
- Nested in: `GameGoals`
- Probable role: AI timing/shot probability
- Fields: `MaidenOvers: int`, `BatsmanBowled: int`, `BatsmanLBW: int`, `BatsmanEdgeOut: int`, `MaidenWickets: int`, `BallsBowled: int`, `BallsFaced: int`, `fastestCenturyBalls: int`, `fastestDoubleCenturyBalls: int`, `hasScoredSixOnFirstBall: bool`, `partnershipBalls: int`, `bestBatsmanRunsScored: int`, `bestBatsmanBallsFaced: int`, `hasTakenWicketOnFirstBall: bool`

### `GoalsConfig`
- Extends: `System.Object`
- Nested in: `GameGoals`
- Probable role: data/config reader or balancing table; AI timing/shot probability
- Fields: `matchGoalTimeRemaining: double`, `milestoneGoalTimeRemaining: double`, `tournamentGoalTimeRemaining: double`

### `MissionGoal`
- Extends: `System.Enum`
- Nested in: `MissionsGoalHandler`
- Probable role: AI timing/shot probability
- Fields: `BatFirstAndPlayEntire10Overs: MissionGoal`, `BatFirstAndPlayEntire20Overs: MissionGoal`, `BowlAMaidenIn50Overs: MissionGoal`, `BowlAMaidenIn20Overs: MissionGoal`, `Bowl8MaidensIn50Overs: MissionGoal`, `BowlAMaidenIn10Overs: MissionGoal`, `Bowl2MaidensIn10Overs: MissionGoal`, `Bowl4MaidensIn20Overs: MissionGoal`, `BatFirstAndPlayEntire50Overs: MissionGoal`, `Bowl15MaidensIn50Overs: MissionGoal`, `Bowl8MaidensIn20Overs: MissionGoal`, `Bowl5MaidensIn10Overs: MissionGoal`

### `Params`
- Extends: `System.Object`
- Nested in: `MissionsGoalHandler`
- Probable role: AI timing/shot probability
- Fields: `<Maidens>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MatchOvers>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RunRate>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<OpponentWickets>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TargetOvers>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TargetRuns>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Wickets>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MatchesToBeWon>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Centuries>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Fivers>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<isSessionGoal>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<isInningGoal>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- Methods: `get_Maidens` @ `0xa968`, `set_Maidens` @ `0x2053`

### `MissionGoalsData`
- Extends: `System.Object`
- Nested in: `MissionsGoalHandler`
- Probable role: name-correlated gameplay/support type
- Fields: `<ID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<GameMode>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`

### `MatchGoalStatsPrefs`
- Extends: `System.Object`
- Nested in: `MissionsGoalHandler`
- Probable role: AI timing/shot probability
- Fields: `MaidenOvers: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BatsmanBowled: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BatsmanLBW: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BatsmanEdgeOut: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaidenWickets: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HatTrick: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `RunsScored: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `RunsGiven: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `WicketsTaken: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `WicketsLost: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BallsBowled: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BallsFaced: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `fastestCenturyBalls: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `hasFastestCenturyBeaten: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `fastestDoubleCenturyBalls: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `hasFastestDoubleCenturyBeaten: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `hasScoredSixOnFirstBall: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `partnershipRuns: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `partnershipBalls: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBowlingRunsGiven: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBowlingWicketsTaken: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBatsmanRunsScored: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBatsmanBallsFaced: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `longestSixDistance: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `hasBeatenLongestSixRecord: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `hasTakenWicketOnFirstBall: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `hasTakenWicketInFirstOver: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`

### `MissionGoalsPrefs`
- Extends: `System.Object`
- Nested in: `MissionsGoalHandler`
- Probable role: data/config reader or balancing table
- Fields: `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `MissionConfigId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `MissionId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `IsAchieved: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsRewardCollected: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`

### `PlayerAnalyticsPrefs`
- Extends: `System.Object`
- Nested in: `PlayerAnalytics`
- Probable role: name-correlated gameplay/support type
- Fields: `HighestIndividualBallsFaced: int`, `HighestPartnershipBalls: int`, `PlayerBatsmanLevel: int`, `PlayerBowlerLevel: int`

### `PlayerAnalyticsType`
- Extends: `System.Enum`
- Nested in: `PlayerAnalytics`
- Probable role: name-correlated gameplay/support type
- Fields: `BatsmanLevel: PlayerAnalyticsType`, `BowlerLevel: PlayerAnalyticsType`

### `PlayerLevelUpgradeType`
- Extends: `System.Enum`
- Nested in: `PlayerAnalytics`
- Probable role: name-correlated gameplay/support type
- Fields: `Batsman: PlayerLevelUpgradeType`, `Bowler: PlayerLevelUpgradeType`

### `AnimationData`
- Extends: `UnityEngine.ScriptableObject`
- Probable role: animation orchestration/timing

### `GooglePlayDownloader`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Methods: `GetMainOBBPath` @ `0x2050`

### `AppleAuthData`
- Extends: `System.Object`
- Probable role: AI timing/shot probability
- Fields: `emailId: string`

### `<>c__DisplayClass5_0`
- Extends: `System.Object`
- Nested in: `AppleSignInManager`
- Probable role: AI timing/shot probability
- Fields: `failCallback: System.Action`

### `BatsmanAnimationChunkData`
- Extends: `UnityEngine.ScriptableObject`
- Probable role: animation orchestration/timing
- Fields: `AnimationClipDatas: elem_0x15`
- Methods: `getBattingAnimClip` @ `0x2050`

### `AnimationClipData`
- Extends: `System.Object`
- Nested in: `BatsmanAnimationChunkData`
- Probable role: animation orchestration/timing

### `<>c__DisplayClass2_0`
- Extends: `System.Object`
- Nested in: `BatsmanAnimationChunkData`
- Probable role: animation orchestration/timing
- Fields: `animname: string`
- Methods: `<getBattingAnimClip>b__0` @ `0xace0`, `<getBattingAnimClip>b__1` @ `0xacf8`

### `BattlepassBasePopup`
- Extends: `RC19.UI.AbstractAnimatableResuableUI`
- Probable role: name-correlated gameplay/support type

### `BattlepassEndingPopup`
- Extends: `BattlepassBasePopup`
- Probable role: name-correlated gameplay/support type

### `BattlepassEntryButton`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `uiData: BattlepassUIDataSO`, `mainText: TMPro.TMP_Text`, `seasonOverMainText: TMPro.TMP_Text`, `debugCollect_Mode: TMPro.TMP_InputField`, `debugCollect_Overs: TMPro.TMP_InputField`, `debugCollect_Played: TMPro.TMP_InputField`
- Methods: `WaitABitAndShowAnim` @ `0x2050`

### `<>c`
- Extends: `System.Object`
- Nested in: `BattlepassEntryButton`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Methods: `<WaitABitAndShowAnim>b__35_0` @ `0xad40`

### `<WaitABitAndShowAnim>d__35`
- Extends: `System.Object`
- Nested in: `BattlepassEntryButton`
- Probable role: animation orchestration/timing; AI timing/shot probability
- Fields: `<>4__this: BattlepassEntryButton`

### `BattlePassFtueScrollItem`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component

### `BattlepassHelper`
- Extends: `System.Object`
- Probable role: animation orchestration/timing
- Methods: `GetAnimCurrencySpot` @ `0x2050`

### `<>c__DisplayClass7_0`
- Extends: `System.Object`
- Nested in: `BattlepassHelper`
- Probable role: name-correlated gameplay/support type
- Fields: `xpCurrency: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`

### `<>c__DisplayClass9_0`
- Extends: `System.Object`
- Nested in: `BattlepassHelper`
- Probable role: name-correlated gameplay/support type
- Fields: `promoPopupData: RC21.AppService.BattlepassPromoPopupData`

### `BattlepassInventoryTab`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component

### `<>c__DisplayClass8_0`
- Extends: `System.Object`
- Nested in: `BattlepassInventoryTab`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassInventoryTab`

### `BattlepassPanel`
- Extends: `PanelController`
- Probable role: name-correlated gameplay/support type
- Fields: `uiData: BattlepassUIDataSO`, `xpRewardsTab: BattlepassXpRewardsTab`, `spinRewardsTab: BattlepassSpinRewardsTab`, `inventoryTab: BattlepassInventoryTab`, `normalRewardsPopup: BattlepassRewardsPopup`, `eliteRewardsPopup: BattlepassRewardsPopup`, `seasonEndedRewardsPopup: BattlepassRewardsPopup`

### `<>c__DisplayClass36_0`
- Extends: `System.Object`
- Nested in: `BattlepassPanel`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassPanel`

### `BattlepassProgressPopup`
- Extends: `BattlepassBasePopup`
- Probable role: name-correlated gameplay/support type

### `BattlepassRewardsGroupView`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `defaultRewardView: BattlepassRewardView`, `premiumRewardView: BattlepassRewardView`, `<Reward>k__BackingField: BattlepassLevelReward`, `<NextLevelReward>k__BackingField: BattlepassLevelReward`

### `BattlepassRewardView`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `uiData: BattlepassUIDataSO`, `<Reward>k__BackingField: BattlepassReward`, `levelData: BattlepassLevelReward`

### `BattlepassSingleSpinCurrencyRewardPopup`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component

### `<>c__DisplayClass3_0`
- Extends: `System.Object`
- Nested in: `BattlepassSingleSpinCurrencyRewardPopup`
- Probable role: animation orchestration/timing
- Fields: `<>4__this: BattlepassSingleSpinCurrencyRewardPopup`, `anim_icon: UnityEngine.Sprite`

### `BattlepassSpinRewardsGroupView`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `slowdownCurve: UnityEngine.AnimationCurve`
- Methods: `SpinAnimation` @ `0x2050`

### `<>c__DisplayClass12_0`
- Extends: `System.Object`
- Nested in: `BattlepassSpinRewardsGroupView`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassSpinRewardsGroupView`

### `<SpinAnimation>d__14`
- Extends: `System.Object`
- Nested in: `BattlepassSpinRewardsGroupView`
- Probable role: animation orchestration/timing
- Fields: `<>4__this: BattlepassSpinRewardsGroupView`

### `<Start10Spins>d__12`
- Extends: `System.Object`
- Nested in: `BattlepassSpinRewardsGroupView`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassSpinRewardsGroupView`

### `BattlepassSpinRewardsTab`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `spinRewardsGroupView: BattlepassSpinRewardsGroupView`, `rewardsMiddleContainer: UnityEngine.GameObject`, `singleSpinCurrencyRewardPopup: BattlepassSingleSpinCurrencyRewardPopup`, `SkipAnimationToggle: UnityEngine.UI.Toggle`, `isSkipAnimation: bool`

### `<>c__DisplayClass38_0`
- Extends: `System.Object`
- Nested in: `BattlepassSpinRewardsTab`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassSpinRewardsTab`, `rewardView: BattlepassSpinThresholdRewardView`

### `<>c__DisplayClass39_0`
- Extends: `System.Object`
- Nested in: `BattlepassSpinRewardsTab`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassSpinRewardsTab`

### `BattlepassSpinRewardView`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `uiData: BattlepassUIDataSO`

### `BattlepassSpinThresholdRewardView`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `uiData: BattlepassUIDataSO`

### `BattlepassStartedPopup`
- Extends: `BattlepassBasePopup`
- Probable role: name-correlated gameplay/support type

### `BattlepassUIDataSO`
- Extends: `UnityEngine.ScriptableObject`
- Probable role: name-correlated gameplay/support type

### `CurrencyAmountIcon`
- Extends: `System.Object`
- Nested in: `BattlepassUIDataSO`
- Probable role: animation orchestration/timing
- Fields: `Anim_Icon: UnityEngine.Sprite`

### `BattlepassXpRewardsTab`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `firstRewardTemplate: BattlepassRewardsGroupView`, `normalRewardTemplate: BattlepassRewardsGroupView`, `milestoneRewardTemplate: BattlepassRewardsGroupView`, `lastRewardTemplate: BattlepassRewardsGroupView`, `lastRewardView: BattlepassRewardsGroupView`, `premiumOrElitePurchasePopup: BattlepassPremiumPurchasePopup`

### `<>c__DisplayClass26_0`
- Extends: `System.Object`
- Nested in: `BattlepassXpRewardsTab`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassXpRewardsTab`, `rewardView: BattlepassRewardView`

### `<ScrollToLastUnlockedReward>d__31`
- Extends: `System.Object`
- Nested in: `BattlepassXpRewardsTab`
- Probable role: name-correlated gameplay/support type
- Fields: `<>4__this: BattlepassXpRewardsTab`

### `BattlepassPremiumPurchasePopup`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component

### `BattlepassRewardsPopup`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component
- Fields: `_currencyCardtemplate: BattlepassCurrencyCardTemplate`, `_packCardTemplate: BattlepassPackCardTemplate`, `_kitBagCardtemplate: BattlepassKitbagItemCardTemplate`

### `RewardFlyAnimation`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `instance: RewardFlyAnimation`, `poolSizePerBatch: int`

### `BowlerAnimTemp`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing
- Fields: `m_AnimatorController: UnityEngine.Animator`, `m_CameraAnim: UnityEngine.Animator`, `leftHandBallObject: UnityEngine.GameObject`, `rightHandBallObject: UnityEngine.GameObject`, `BowlerAnimIndex: BowlingAnimType`, `_BowlerArmAndSide: BowlerArmAndSide`, `SetBowlerArmAndSide: bool`, `TriggerBowlingAnim: bool`
- Methods: `OnAnimationFinishedWithParam` @ `0x2053`, `OnSetBowlerArmAndSide` @ `0x2053`, `TriggerBowlerAnim` @ `0x2053`

### `BowlingEvents`
- Extends: `System.Enum`
- Nested in: `BowlerAnimTemp`
- Probable role: AI timing/shot probability
- Fields: `kReleaseBall: BowlingEvents`, `kSetAIBowlingControls: BowlingEvents`, `kBallCollectionAroundStump: BowlingEvents`, `kCelebrationJumpBallUpwards: BowlingEvents`

### `BowlerArmAndSide`
- Extends: `System.Enum`
- Nested in: `BowlerAnimTemp`
- Probable role: name-correlated gameplay/support type
- Fields: `kLeftArmRoundTheWicket: BowlerArmAndSide`, `kLeftArmOverTheWicket: BowlerArmAndSide`, `kRightArmRoundTheWicket: BowlerArmAndSide`, `kRightArmOverTheWicket: BowlerArmAndSide`

### `ButtonCharacterStyle`
- Extends: `UnityEngine.MonoBehaviour`
- Probable role: Unity MonoBehaviour component; animation orchestration/timing; AI timing/shot probability
- Fields: `isDelayedAnimationStart: bool`, `waitTime: float`

## ACTk / Obscured Field Uses
- `StadiumOptionItem`: `IsLocked: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `FlashSale`: `<Id>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ProductInfo>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ProductDesc>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Header>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Prefab>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Price>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IapID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<DependentOnID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RepeatSaleAfterDays>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<DurationHrs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RepeatRewardForDays>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `SaleRewardItems`: `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `ActiveFlashSale`: `<Id>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsBought>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `ActiveFlashSaleData`: `<Id>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsBought>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `ActiveFlashSalesData`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `GameplayController`: `isInningsCompleted: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `MatchRewardPanel`: `mb_IsDoubleReward: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `TournamentButton`: `isDiscountProduct: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `_IsTournamentActive: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `_TournamentTier: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_UnlocksAtLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_StoreProductID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_IsTournamentUnlockedThroughTutorialDailyRewards: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RankedPremierLeagueConfig`: `<LeagueID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QuestSlotMachinePanel`: `_itemsAlloted: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MAX_REWARD_ITEMS_IN_GRID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `MainMenuCustomTournamentPanel`: `isDiscountProduct: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `_TournamentTier: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_StoreProductID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `GameEconomyAnalytics`: `m_Exp: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<RewardMultiplier>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `Params`: `<Maidens>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MatchOvers>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RunRate>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<OpponentWickets>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TargetOvers>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TargetRuns>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Wickets>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MatchesToBeWon>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Centuries>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Fivers>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<isSessionGoal>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<isInningGoal>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `MissionGoalsData`: `<ID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<GameMode>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `MatchGoalStatsPrefs`: `MaidenOvers: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BatsmanBowled: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BatsmanLBW: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BatsmanEdgeOut: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaidenWickets: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HatTrick: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `RunsScored: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `RunsGiven: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `WicketsTaken: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `WicketsLost: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BallsBowled: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BallsFaced: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `fastestCenturyBalls: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `hasFastestCenturyBeaten: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `fastestDoubleCenturyBalls: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `hasFastestDoubleCenturyBeaten: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `hasScoredSixOnFirstBall: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `partnershipRuns: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `partnershipBalls: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBowlingRunsGiven: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBowlingWicketsTaken: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBatsmanRunsScored: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `bestBatsmanBallsFaced: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `longestSixDistance: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `hasBeatenLongestSixRecord: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `hasTakenWicketOnFirstBall: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `hasTakenWicketInFirstOver: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `MissionGoalsPrefs`: `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `MissionConfigId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `MissionId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `IsAchieved: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsRewardCollected: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `<>c__DisplayClass7_0`: `xpCurrency: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `<>c__DisplayClass15_0`: `item: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RawReward`: `RewardId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Value: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `PlayerInAuction`: `ID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Name: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Nationality: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingHand: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingTechnique: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingTiming: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingAggression: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BatsmanType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `KeepingSkill: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingHand: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingSkill: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingMovement: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingAi: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `FieldingRating: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `JerseyNum: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingActions: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `CaptainPriority: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `WicketKeeper: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HairMeshTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HairRGB: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HairHSL: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Body_Sticker_Collar_Thickness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Face_Hair_Cap_Hat_Helmet_Sunglasses_Thickness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `FaceMesh: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `FaceTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `FaceRGB_Hex: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HandTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HandRGB_Hex: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Helmet_Value: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Sunglass_Cap_Value: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `FullName_License: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `FirstName_License: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `LicenseType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `JerseyName_License: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Strap_Value: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Hand_Blend: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Hand_Spec: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HandSpec_Smoothness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Height: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Face_Spec: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `FaceSpec_Smoothness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `playerType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `category: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `battingOrder: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `pool: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `attractivity: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `basePrice: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `minPrice: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `maxPrice: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `RTM_TeamID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `fitness: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `soldAt: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `soldTo: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ModdedJerseyName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `Ball`: `m_ShotTiming: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `mb_HitBody: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_HitBat: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_HitStumps: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `isHitFielder: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `m_ShotAngleY: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `mb_HitPad: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_LBWOutOriginalDecision: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_IsLBWAppeal: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_IsEdgeOutAppeal: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_IsEdgeOutOriginalDecision: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_IsEdgeOutFinalDecision: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `kAppealMaxDistance: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kLegStumpMaxDistance: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kStumpHeight: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kLegStumpMaxDistance_ML: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kStumpHeight_ML: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kStumpMaxY: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kStumpMaxX: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kLegStumpMaxAppealDistance: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kStumpAppealHeight: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kBallForceDampingFactor: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kPerfectShotRange: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `mb_IsGoneThroughStumps: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_HitGround: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_BouncedBallChecked: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_WideBallChecked: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_IsThinEdge: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_IsLBW: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `force: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `projectionX: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `projectionY: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `m_BatCollisionType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_BatCollisionRegion: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `BatsmanController`: `m_CurrentShotType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `kBatsmanMoveRange: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `mb_IsRBWStarted: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_IsRBWCancelled: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `m_IsBallHitBoundary: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsOverThrowBoundary>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_BallHitWicketWhileRBW: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `kRBWDistance: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `mi_BatsmanIDRBW: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `kDifficultyBatColliderMinXBound: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kDifficultyBatColliderMaxXBound: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kDifficultyBatColliderMaxXBound_ML: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kDifficultyBatColliderMaxYBound_AI: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `mb_RBWHasCrossedMidPitchDuringCatch: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `maxDistanceFromCreaseForRunOut: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `maxDistanceForSwitchingAnim: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `distanceToTargetStriker: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `distanceToTargetNonStriker: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `BowlerController`: `mi_SpeedBarDirection: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `mi_BounceBallCount: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `kPitchPointMinScale: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `kPitchPointMaxScale: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `KeeperController`: `mb_IsStumpingEvent: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `mb_DoEdgeCatch: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `isKeeperFiedling: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `InningsData`: `TotalRuns: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `TeamWickets: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `WicketsCreditedToBowler: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `TeamBallsFaced: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Extras: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `RunsInAOver: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `RunsInAOverFull: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `TotalFours: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `TotalSixes: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `isSimulationUsed: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `iBattingTeamDRSReview: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `iBowllngTeamDRSReview: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `iFieldingMode: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `iFieldingType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `iFieldingCategary: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `isAIWicketFall: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `startingProgressForCaseI: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `endingProgressForCaseI: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `executeCaseIIITillRR9: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `bounceBallCount: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `expectedScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `TeamBallsFaced_WithoutSimulation: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `TeamRunsScored_WithoutSimulation: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `teamId_Batting: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ballAtNewBallTaken: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `sillyPointOrShortLegCatches: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `compellEdgeWicets: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `compellEdgeWicets_spin: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `compulEdgesThisOver: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Dots: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `PlayerDetails`: `ID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Nationality: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PlayerCategory: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingHand: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingTechnique: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingTiming: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattingAggression: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `KeepingSkill: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingSkill: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BowlingMovement: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `FieldingRating: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `JerseyNo: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `LoadedForTeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ModdedJerseyName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `TestBattingPosition: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ODIBattingPosition: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `T20BattingPosition: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `CaptainPriority: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `WicketkeeperPriority: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HairMeshTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HairRGB: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HairHSL: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Body_Sticker_Collar_Thickness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Face_Hair_Cap_Hat_Helmet_Sunglasses_Thickness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `FaceMesh: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `FaceTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `FaceRGB_Hex: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HandTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HandRGB_Hex: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Height: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `CurrentTeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `DefaultName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `DefaultJerseyNo: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Helmet_Value: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Sunglass_Cap_Value: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Strap_Value: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Hand_Blend: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Hand_Spec: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HandSpec_Smoothness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `FullName_License: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `FirstName_License: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `LicenseType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `JerseyName_License: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Face_Spec: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `FaceSpec_Smoothness: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `TeamInfo`: `m_TeamID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_DisplayName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_DisplayCustomName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_AutoSelect: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_PackName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_Abbreviation: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_RatingBat: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_RatingBowl: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_RatingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_SquadFileName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_JerseyFileName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_LogoFileName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_TeamType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `testEligible: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_WCEventEligible: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_MainText: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_StripText: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_anthemFile: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_anthemDuration: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `m_KeeperPadFileName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_CheerleaderTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_AssetBundleName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<UserID_2pVs2P>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_PlayerBG: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_SquadBG: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `TournamentFBPoll`: `_CurrentDayIndex: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `_CurrentDayWeekIndex: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `DayData`: `<Day>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TournamentID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `WeeklyData`: `<Week>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TournamentID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `CloudConfig`: `<StartDateText>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<NextMatchDelayInMinutes>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `DailyRewardPlayerData`: `<playerId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<cycleStartDate>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<isPremiumPlayer>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<isPremiumNextCycle>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<lastCollectedRewardDate>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CurrentDay>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TutorialFinished>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<TutorialStarted>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<TutorialOfferStarted>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<TutorialOfferStartDate>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TutorialOfferIndex>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TutorialOfferEnded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RawReward`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemValue>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<IAPItemType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `TutorialReward`: `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `DayReward`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `DailyRewardsManager`: `m_CurrentDay: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `requestLimit: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `requestLimit_FailFuse: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RewardData`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IAPItemType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<Success>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Debug>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<Success>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<Success>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `CollectRewardQueryRequest`: `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `ScoreGradingID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ForcedDay: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `CollectRewardQueryResponse`: `<Success>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `EnterMatchQueryRequest`: `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `ForcedDayIndex: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `EnterMatchQueryResponse`: `<Success>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `DailyStrikeTracker`: `currentScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `belowScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `targetScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `aboveScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `HashTableObscured`: `<key>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<val>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `BatsmanShotData`: `<perfectFrameTime>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<direction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<proShotType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<batsmanType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<isPremiumShot>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ProjectionAngleY>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPoorAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPoorForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyAverageAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyAverageForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyExcellentAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyExcellentForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPerfectPoorAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPerfectPoorForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPerfectAverageAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPerfectAverageForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPerfectExcellentAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<earlyPerfectExcellentForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<perfectPoorAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<perfectPoorForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<perfectAverageAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<perfectAverageForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<perfectExcellentAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<perfectExcellentForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePerfectPoorAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePerfectPoorForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePerfectAverageAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePerfectAverageForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePerfectExcellentAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePerfectExcellentForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePoorAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<latePoorForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<lateAverageAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<lateAverageForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<lateExcellentAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<lateExcellentForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<outsideEdgeProjectionAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<outsideEdgeProjectionAngleY>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<outsideEdgeForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<outsideEdgeSpinProjectionAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<outsideEdgeSpinProjectionAngleY>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<outsideEdgeSpinForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<insideEdgeProjectionAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<insideEdgeProjectionAngleY>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<insideEdgeForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<insideEdgeSpinProjectionAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<insideEdgeSpinProjectionAngleY>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<insideEdgeSpinForce>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<isDrsShot>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<shotType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<animationSpeed>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<ShotName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<deltaPos>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<replayCameraIndex>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `UserBattingDifficulty`: `<CaseNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MinRange>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MaxRange>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<EarlyPerfect>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<Perfect>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<LatePerfect>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<ColliderSize>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<RayLength>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `GameDifficulty`: `<Type>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BatTimingManipulation>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<CollisionScaleReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<PerfectTimingManipulation>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<RangeReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<AIRunRateReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<ForceIncrement>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `GameDifficulty_New`: `<Type>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RunRate>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<BatTimingManipulation>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<CollisionScaleReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<PerfectTimingManipulation>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<RangeReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<AIRunRateReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<ForceIncrement>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `GameDifficulty_New_Test`: `<Type>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BatTimingManipulation>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<CollisionScaleReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<PerfectTimingManipulation>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<RangeReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<AIRunRateReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<ForceIncrement>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `TimingMeter_ML`: `ratingMin: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ratingMax: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Early: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `EarlyPerfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Perfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `LatePerfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Late: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `TimingMeterMod_ML`: `BatsmanCategory: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ShotType: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `Early: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `EarlyPerfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Perfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `LatePerfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Late: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Edges: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Collision: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `AiTimingProbMod`: `BatsmanCategory: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `ShotType: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Early: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `EarlyPerfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Perfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `LatePerfect: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `Late: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `KitbagItem`: `<Sr_No>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<KitType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ProdType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Precision>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Collision>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Timing>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Power>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Reduce_No_Ball_Changes>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Increase_RBW_Speed>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Spin>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Pace>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Swing>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<No_Of_Matches>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Image>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `KitbagKit`: `<Sr_No>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Kit_Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Bat>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Ball>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Shoe>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Glove>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<No_of_Matchs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Image>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `LegByeForceData`: `<bowlerType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<hitSide>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<projectionAngleX>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<projectionAngleY>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<force>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `AiRBWTest`: `<minRR>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<maxRR>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `AiRBWLimitedOvers`: `<InningStageMin>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<InningStageMax>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<TeamWickets>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `ReviveInfo`: `<ReviveCount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IAPName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<IAPUid>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `GameEntryPrefs`: `userTeam: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `opponentTeam: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `isUserBatting: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `isMatchActive: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `isTossScreenShown: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `isUserWonTheToss: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `isHighlightSaved: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsT20Jersey: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsOpponentT20Jersey: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `UserTeamIDJersey_CM: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `OpponenetTeamIDJersey_CM: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `KitBundleID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `KitBatID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `KitBallID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `KitShoeID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `KitGlovesID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `LicensedKitBatIDUser: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `LicensedKitBatIDOpponent: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `LicensedKitGloveIDUser: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `LicensedKitGloveIDOpponent: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `LicensedKitShoeIDUser: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `LicensedKitShoeIDOpponent: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `BattlepassXPRewarded: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `CommunityEventXPRewarded: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `InGameDataPrefs`: `MatchId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `userTeam: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `opponentTeam: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `currentInningsIndex: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `currentBattingOrderIndex: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `curPartnershipCelebrationLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `curPartnerShip: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `sessionCount: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `ballsAtSessionChanged: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `previousBowlerID: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `isFreehit: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `isSuperOverInProgress: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `hasAutoplayed: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `adsReviveCounter: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `purchasedReviveCounter: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `totalReviveCounter: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `TeamData`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TournamentName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TeamName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TournamentUIDs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `TournamentData`: `<ID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<DisplayName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Logo>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Abbreviation>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `SavedMods`1`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `UserModsPrefferences`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FirstTimeEntered>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<TermsAccepted>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<SubscriptionBought>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<RenewSubscriptionPopupShown>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `PlayerData`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<MUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FullName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<JerseyNo>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<HairMeshTexture>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<HairRGB>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Body_Sticker_Collar_Thickness>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Face_Hair_Cap_Hat_Helmet_Sunglasses_Thickness>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FaceMesh>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FaceTexture>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FaceRGB_Hex>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<HandTexture>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<HandRGB_Hex>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<License>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `<>c__DisplayClass157_1`: `t: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `CachedJerseyMod`: `<ThumbnailDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<AssetsDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<NewDownloadRequired>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<JerseyTextureLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<JerseyThumbnailLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Rated>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `CachedLeagueMod`: `<Activated>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<ThumbnailDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<AssetsDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<NewDownloadRequired>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<LogoThumbnailLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<LogoTextureLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Rated>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `CachedPackageMod`: `<Activated>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<AssetsDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<NewDownloadRequired>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<LeagueDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<TeamsDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PlayersDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<JerseysDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `CachedPlayerMod`: `<ThumbnailDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<AssetsDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<NewDownloadRequired>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<FacemapTextureLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FacemapThumbnailLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Rated>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `CachedTeamMod`: `<Activated>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<ThumbnailDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<AssetsDownloaded>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<NewDownloadRequired>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<LogoTextureLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<LogoThumbnailLocalPath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Rated>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `Fielder`: `mb_IsStumped: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `FieldingController`: `m_FieldingState: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `StoreTransactionHandler`: `_UnAuthroizedActivityFound: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `Attributes`: `<ShotPower>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<BatCollision>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<BatTiming>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Spin>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Pace>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Swing>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<NoBallChancesReduction>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RBWSpeedIncrement>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TicketsRequired>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CoinsReward>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `StoreData`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<SKUType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ProdType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<SKU>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<SKU_IOS>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Image>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Texture>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Brand>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<IsDiscount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<DiscountImage>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Discount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `ProductData`: `Price: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Currency: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `IsPurchased: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `PresetGUID: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `UIMatchReward`: `mb_IsDoubleReward: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `KitbagItemBall`: `_noOfMatches: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `KitbagItemBat`: `_noOfMatches: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `KitbagItemGlove`: `_noOfMatches: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `KitbagItemKit`: `m_batName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_ballName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_gloveName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `m_shoeName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `_noOfMatches: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `KitbagItemShoe`: `_noOfMatches: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `UIMatchSettings`: `kCoinsRequiredForStadium: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `UIPlayerLevelUpgrade`: `currentBatsmanLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `currentBowlerLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `currentFielderLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `m_MaxPlayerLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `PlayerProgressionConfig`: `<playerlevel>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ticketsrequired>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<fielderlevel>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `UIStadium`: `IsLocked: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `UITournamentSubGroup`: `_UnlocksAtLevel: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `IPDetail`: `<IP>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `SSOAuthRequestModel`: `AccountId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Emailid: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Username: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Platform: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `PushRegistrationId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `DeviceId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `PicUrl: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Appversion: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `IsCheatDetected: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<LegacyUserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `SSOAuthenticationHandler`: `RC19FBAPPID: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `KEY_EXISTING_SIGNIN_TYPE: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `ConfigValue`: `DefaultValue: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RemoteConfigFileVersion_`: `FileName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RemoteCachedImage`: `Version: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `CodeStage.AdvancedFPSCounter.AFPSCounter`: `fpsCounter: CodeStage.AdvancedFPSCounter.CountersData.FPSCounterData`, `memoryCounter: CodeStage.AdvancedFPSCounter.CountersData.MemoryCounterData`, `deviceInfoCounter: CodeStage.AdvancedFPSCounter.CountersData.DeviceInfoCounterData`, `labels: CodeStage.AdvancedFPSCounter.Labels.DrawableLabel[]`, `operationMode: CodeStage.AdvancedFPSCounter.OperationMode`, `<Instance>k__BackingField: CodeStage.AdvancedFPSCounter.AFPSCounter`
- `<UpdateFPSCounter>d__119`: `<>4__this: CodeStage.AdvancedFPSCounter.AFPSCounter`
- `<UpdateMemoryCounter>d__120`: `<>4__this: CodeStage.AdvancedFPSCounter.AFPSCounter`
- `CodeStage.AdvancedFPSCounter.FPSLevel`: `Normal: CodeStage.AdvancedFPSCounter.FPSLevel`, `Warning: CodeStage.AdvancedFPSCounter.FPSLevel`, `Critical: CodeStage.AdvancedFPSCounter.FPSLevel`
- `CodeStage.AdvancedFPSCounter.OperationMode`: `Disabled: CodeStage.AdvancedFPSCounter.OperationMode`, `Background: CodeStage.AdvancedFPSCounter.OperationMode`, `Normal: CodeStage.AdvancedFPSCounter.OperationMode`
- `CodeStage.AdvancedFPSCounter.Labels.DrawableLabel`: `anchor: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`
- `CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`: `UpperLeft: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`, `UpperRight: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`, `LowerLeft: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`, `LowerRight: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`, `UpperCenter: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`, `LowerCenter: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`
- `CodeStage.AdvancedFPSCounter.CountersData.BaseCounterData`: `main: CodeStage.AdvancedFPSCounter.AFPSCounter`, `anchor: CodeStage.AdvancedFPSCounter.Labels.LabelAnchor`
- `CodeStage.AdvancedFPSCounter.CountersData.FPSCounterData`: `<CurrentFpsLevel>k__BackingField: CodeStage.AdvancedFPSCounter.FPSLevel`
- `Azure.AppServices.AppServiceClient`: `_AppId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `_ApiKey: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `CommentaryCard`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Probability>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `CommentaryCloudConfig`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Probability>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `RC24.DailyStrike.DailyStrikeManager`: `eventStarted: CodeStage.AntiCheat.ObscuredTypes.ObscuredDateTime`, `eventDuration: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `currentDay: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `rewardGiven: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `lastMatchDifficulty: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `isPaidEntry: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC24.DailyStrike.DailyStrikeDayReward`: `<BelowItemID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<BelowRuns>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<BelowName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BelowAmount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<BelowItemType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<PerfectItemID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<PerfectRuns>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<PerfectName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PerfectAmount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<PerfectItemType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<AboveItemID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<AboveRuns>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<AboveName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AboveAmount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<AboveItemType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC24.DailyStrike.DailyStrikeReward`: `<ItemID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Amount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC24.DailyStrike.UserDailyStrikePrefs`: `<FreeEntryAvailable>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PaidEntriesAmount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsWelcomeScreenShown>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<Difficulty>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CurrentLossStreak>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<WasLastEntryFree>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC24.DailyStrike.DailyStrikeConfig`: `<EventDurationDays>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<FreeEntryResetHour>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<EntriesReceivedOnIAP>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsDebug>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC24.DailyStrike.ScoreData`: `belowScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `perfectScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `aboveScore: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `<APIGooglePlayIntegrity>d__128`: `token: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.AppServiceContext`: `modsUrl_fromAppConfig: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<_AppUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AWSCloudFrontBaseUri>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `AppPlatform: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `_CheatDetected: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `<>c__DisplayClass67_0`: `token: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.ApplicationConfigModel`: `Category: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Platform: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Version: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `PhotonServerIP: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `IsForceUpdateML: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsForceUpdateSP: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsMaintenanceML: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `CurrentSeasonML: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `IsWCEventActiveML: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsMinimalBuild: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `IsAppUnsupported: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `ProductionAppUrl: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CloudFrontUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<DeepLinkUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.GameDataBundle`: `<Version>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC21.AppService.CloudAssetBundle`: `<AppVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.AssetBundleCRCInfo`: `<BundleTag>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<crc>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredUInt`
- `RC21.AppService.AssetBundleInfo`: `<BundleTag>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BundleName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Version>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Size>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `GetQuery`: `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Appversion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Memory>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC21.AppService.GEPLPopupData`: `<HeaderText>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<MessageText>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BgImageUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<LinkUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.GEPLData`: `<IsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<MpButtonActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PopupsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<RulesUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BGImagesVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<SpaceId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.BattlepassPromoPopupData`: `IsActive: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `BGImagesVersion: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `BgImageUrl: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.ModsToolData`: `<CostPerMod_League>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CostPerMod_Team>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CostPerMod_Jersey>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CostPerMod_Player>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ModsAppUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.FanModeTeam`: `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<SpaceId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RegisterURL>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.FanModePopupData`: `<HeaderText>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BgImageUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<LinkUrl>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.FanModeData`: `<IsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<MpButtonActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PopupsActive>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<RulesURL>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BGImagesVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.Attachment`: `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Version>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ContentType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<StoragePath>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.AuthenticationResponseModel`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ModUId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AuthToken>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AuthTokenValidity>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<DisplayName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AccountId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PictureURL>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<WWEBrandingSeen>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsAccountBanned>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsQuestFlashSale>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<GameBundleSquadVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<GameBundleTournamentVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ProgressCleared>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<RequiresProgressCheck>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<EnableReneverse>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<EnableLicensedRCPL>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<AdsMinMatchCount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<GameIconID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<EnableMLAuth>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<SessionId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TOSLink>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PPLink>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<SupportEmail>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC21.AppService.GooglePlayIntegrityAPIRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Token>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BundleTag>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Token>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CountryCodeDevice>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<Token>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RawReward`: `<RewardId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<GUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Source>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `BattlepassReward`: `<IsCollected>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `SpinsThresholdReward`: `<SpinsToUnlock>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsCollected>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `XpPointsEntry`: `<Overs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TotalBallsToBePlayed>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Points>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `XpMultiplierEntry`: `<MinBallsToPlay>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MaxBallsToPlay>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Multiplier>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `BattlepassLevelReward`: `<BattlepassLevel>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<PointsToUnlock>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `SeasonData`: `<Season>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `BattlepassPrefs`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<IsPremium>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsElite>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<BattlepassLevel>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Overs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<PlayedBalls>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryResponse`: `<CollectedXP>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TillBattlepassLevel>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Spins>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `CommunityEventConfigs`: `<EventName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<EventDescription>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RunAddThreshold>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<EventNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `EventMatchConfig`: `<Duration>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MatchResultDescription>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `StreakConfigs`: `<IsButtonEnabled>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `StreakRewardConfig`: `<StreakNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `MileStoneRewardConfig`: `<TeamMileStoneUnlockCriteria>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsBonusMultiplierEnabled>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `IndividualMilestone`: `<ThresholdPoints>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`
- `TeamMilestone`: `<ThresholdPoints>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`
- `CommunityEventData`: `<CurrentCycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<EventNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `UserMatchStat`: `<CycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<UserTeamID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<OpponentTeamID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<UserScore>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<UserTeamScore>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<OpponentTeamScore>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<IsTeamWon>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<UserTeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<OpponentTeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `teamScore`: `<TeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Score>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<UserTeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<OpponentTeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Score>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredFloat`, `<CycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ThresholdPoints>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<CycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ThresholdPoints>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<CycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<StreakNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CycleNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TeamID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<TeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FileName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<FileName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContentType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<SquadVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TournamentVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryResponse`: `<Status>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<SquadVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<TournamentVersion>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Key>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequestMultipleItems`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<GiveRewards>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryResponse`: `<ProgressCleared>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<RequiresProgressCheck>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `SinglePlayerProgression`: `<Level>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<XP>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<MaxXP>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `SinglePlayerMatchRewards`: `<Overs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `XPReward`: `<E>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<M>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<H>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Ex>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<HC>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<AP>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `TournamentEconomyData`: `<Mode>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Card>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ForceUpdateSquad>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `GameModeProgression`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Id>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `GoogleIAPRewardsInfo`: `<productID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContentType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<DeleteAccount>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `GetProgressionRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AppPlatform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `ItemCollectRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AppPlatform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ConfigId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QuestProgressionRewardCollectRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AppPlatform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<QuestId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `PremiumShotPurchaseRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AppPlatform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ConfigId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QuestContainerCollectRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AppPlatform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ConfigId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `MultiplayerStadium`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `ReceiptInfo`: `<PurchaseState>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<PurchaseToken>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TransactionID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<OriginalTransactionID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Environment>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `StoreReceiptRequestModel`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PackageName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ProductSKU>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ProductType>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ISOCurrencyCode>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PriceInDecimel>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<IsFreeTrial>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `StoreReceiptResponseModel`: `<OrderId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PurchaseState>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Status>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `ProductMeta`: `<ItemId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ItemIdText>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.SinglePlayer.Models.SinglePlayerStadium`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `ContractInitialPeriod`: `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `ContractRenewalPeriod`: `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `StadiumRenewalPeriod`: `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AppPlatform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ConfigId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<BonusRewardID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Nationality>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RewardsMeta`: `<AllowDuplicates>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Contextid>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `SeasonGifts`: `<SeasonID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `SeasonGiftsInfo`: `<Rank>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `SeasonLevelChange`: `<Level>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<DowngradeTo>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ContextId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RewardsMeta`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.JerseyModMetadata`: `<JerseyTextColor>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.JerseyModData`: `<TeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CreatorId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CreatorName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetRank>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<IsT20Variant>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsTestVariant>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.LeaguePackageData`: `DBId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `TeamCount: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PlayerCount: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `JerseyCount: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.LeagueModMetadata`: `LeagueName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HasCustomLogo: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.LeagueModData`: `<LeagueId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CreatorId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CreatorName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetRank>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<RC24_TournamentID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RCSwipe_TournamentID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `AssetId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `Asset`: `Id: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `UserId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Platform: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<Success>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `RcUid: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `SwipeUid: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `ModUid: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `TeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `LeagueId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `PlayerId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `TeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `OwnMods: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `TeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `LeagueId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `OwnMods: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `OwnMods: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `PlayerId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `TeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `CreatorId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `OwnMods: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `<TeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CreatorId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `Message: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `TeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `LeagueId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `PlayerId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `TeamId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxPagesize: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `PageNumber: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `LeagueId: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `AssetId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Rating: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `QueryRequest`: `RcUid: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `SwipeUid: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `ModUid: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.PlayerModMetadata`: `PlayerName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `PlayerShortname: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `PlayerJerseyNo: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HasCustomFacemap: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `FaceThickness: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `FaceMesh: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HandColor: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HairType: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HairRGB: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HairHSL: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `FaceRGB: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HandTexture: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.PlayerModData`: `<PlayerId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CreatorId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CreatorName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetRank>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<TeamID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.TeamModMetadata`: `TeamName: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Abbreviation: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `HasCustomLogo: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ModsTool.TeamModData`: `<TeamId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CreatorId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CreatorName>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AssetRank>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<AuthURL>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AuthorizationCode>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<IsLinked>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PersonalAccessToken>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<IsLinked>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PersonalAccessToken>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ChallengerModeIsDown>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `RoomId: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PhotonUserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RoomId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CMUserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RoomId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryResponse`: `<IsHost>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PhotonRoomCode>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CMMatchId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CMTournamentsId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CMUsername>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CMOpponentUsername>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<CMSpaceId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Overs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Ranked>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<GameAlreadyStarted>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RoomId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RoomId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Winner>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<Score>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ChallengerMode.ChallengerModeMatch`: `Link: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ChallengerMode.ChallengerModeTournament`: `Title: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Id: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `Ranked: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `Overs: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `JoinURL: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `OverviewURL: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `EndTime: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `ScheduledStartTime: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `FilledSlots: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `MaxSlots: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `HasEntryFee: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `EntryFee: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ChallengerMode.ChallengerModePlayer`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TeamNumber>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsHost>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<IsReady>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<Winner>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<ChallengerModeUsername>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TriedToJoinSecondTime>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<PhotonUserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.Multiplayer.Models.ChallengerMode.ChallengerModeRoom`: `<RoomId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<SessionId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PhotonRoomCode>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Overs>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Ranked>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<Tie>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`, `<ChallengerModeRoomId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TournamentId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<SpaceId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<TournamentTitle>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `QueryRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.LiveOps.Progression`1`: `<ProgressionId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.LiveOps.QuestFlashSaleConfig`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<FlashSaleId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `ShotPurchaseInfo`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ShotID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `ShotConfig`: `<UID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ShotID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<Duration>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `Currency`: `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `LicensedTeam`: `<Item>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `KitBag`: `<Value>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsDefault>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `MissionItem`: `<PrevStarsCollected>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `RC3D.LiveOpsCore.Entities.LiveOps.Models.Base.ConfigBase`1`: `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ResetFrequency>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`
- `RC3D.LiveOpsCore.Entities.LiveOps.Models.Base.ContainerBase`2`: `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<MaxItems>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<CollectionDelay>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredDouble`, `<IsCompleted>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC3D.LiveOpsCore.Entities.LiveOps.Models.Base.ItemBase`: `<ItemUid>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Name>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<ItemID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<IsCompleted>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredBool`
- `RC3D.LiveOpsCore.Entities.InAppPurchase.InAppProductBase`: `<Platform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.InAppPurchase.InAppPurchaseInfo`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<PurchaseState>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`
- `BattingPresetConfig`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `RC3D.LiveOpsCore.Entities.InAppPurchase.SubscriptionItemBase`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `SubscriptionModelRequest`: `<UserId>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<AppPlatform>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`
- `SubscriptionItem`1`: `<ProductUID>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Title>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<Description>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredString`, `<RevealInDays>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`, `<RevealDelayInDays>k__BackingField: CodeStage.AntiCheat.ObscuredTypes.ObscuredInt`