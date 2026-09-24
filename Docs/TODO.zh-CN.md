# 待办

英文 `Docs/TODO.md` 为准。本文件只复述同一批事实。

状态：`Not started`（未开始），`Blocked by product choice`（等产品决定），`Ready for design`（可以设计），`Ready for implementation`（可以实现），`Implemented; validation pending`（已写完，核对未完成）。

## P0

### DOC-001 交接文档与设计约定
- Status: Implemented; validation pending
- Dependencies: 无
- Current files: `AGENTS.md`、`Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`、`Docs/GAME_DESIGN.md`、中文镜像、`Docs/AI_PROJECT_HANDOFF_RULES.md`
- Work: 保持英文文档与中文镜像事实一致。
- Done when: 新会话不靠猜测就能读到产品目标、模块结构和未决问题。

### DES-002 挡住第一份剧本的选择
- Status: Implemented; validation pending
- Dependencies: DOC-001
- Current files: `Docs/GAME_DESIGN.md` 的未决问题，`Docs/MEMORY.md`
- Work: 第一份模块选用空间路线谜、跨年代人际故事和外星 AI 观测谜。正文是虚构无名城市中的中文第一人称故事，按八阶段故事圆环推进。属性名称、数值和检定结算方式留给以后模块；本模块只用直接选项。
- Done when: 选定的故事方向和第一人称语言已写入 `Docs/MEMORY.md`，且 `Docs/GAME_DESIGN.md` 相符；仍需编辑复核。

## P1

### DES-003 第 0 号完整剧本
- Status: Implemented; validation pending
- Dependencies: DES-002
- Current files: `Scenarios/00-zero-floor.md`
- Work: 一份中文第一人称 Markdown 模块，有完整故事圆环、原创正文、双结局、线索解锁推理，以及直接选项。没有引擎。
- Done when: 标题信息、主持人简报、时间线、开场、人物、地点、线索、场景、选项、检定、结局、手稿都在。每条线索都有揭示条件。每个结论选项写明所需线索 id。每一拍列出自己的选项并标明显示方式。仍需编辑和游玩流程核对。

### ENG-001 C# 控制台运行时
- Status: Implemented; validation pending
- Dependencies: 用户已要求开始实现。运行时是 .NET 10 上的 C# 控制台。发布目标是 Windows x64 自包含单文件 exe。
- Current files: `Game/SOS_Project.csproj`、`Game/Program.cs`、`Game/Story.cs`、`Game/StoryRunner.cs`、`Scenarios/ZeroFloor.Play.cs`。
- Work: 源码框架按编号选项推进场景，处理线索与旗标的条件和效果，可重读已发现的线索和手稿，并按需打印彩色 `■` 画面。编译用剧情数据涵盖开场、S00—S05、K01—K03 和 H01 初版。在 S05，`0` 可重读手稿，两个编号选项都可结束预览。玩家输出不含主持人笔记。
- Done when: 静态审阅确认开场首段与剧本一致；另外获得授权后，通过构建或试玩确认控制台行为。尚未运行构建、测试或发布。不添加 Unity。

### ENG-002 接入第 0 号剧本后续内容
- Status: Ready for implementation
- Dependencies: ENG-001、DES-003；接入后续内容时处理它们的核对结果。
- Current files: `Scenarios/00-zero-floor.md`、`Scenarios/ZeroFloor.Play.cs`、`Game/Story.cs`、`Game/StoryRunner.cs`。
- Work: 接入 S06—S16、其余线索和手稿、线索解锁推理与两条结局路径，不让玩家看到主持人笔记。本模块保持直接选项。属性规则、存档及删除本游戏 exe／存档属于单独决定或后续工作。
- Done when: 完整剧本能按照文档中的条件与反馈通向两个结局，线索门槛和重读保持有效。在用户要求试玩时验证。
