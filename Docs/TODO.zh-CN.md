# 待办

英文 `Docs/TODO.md` 为准。本文件只复述同一批事实。

状态：`Not started`（未开始），`Blocked by product choice`（等产品决定），`Ready for design`（可以设计），`Ready for implementation`（可以实现），`Implemented; validation pending`（已写完，核对未完成），`Complete`（完成）。

## P0

### DOC-001 交接文档与设计约定
- Status: Complete
- Dependencies: 无
- Current files: `AGENTS.md`、`Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`、`Docs/GAME_DESIGN.md`、中文镜像、`Docs/AI_PROJECT_HANDOFF_RULES.md`
- Work: 保持英文文档与中文镜像事实一致。
- Done when: 新会话不靠猜测就能读到产品目标、模块结构和未决问题（中英文交接审阅已验证）。

### DES-002 挡住第一份剧本的选择
- Status: Complete
- Dependencies: DOC-001
- Current files: `Docs/GAME_DESIGN.md` 的未决问题，`Docs/MEMORY.md`
- Work: 第一份模块于 2026-09-30 重写，是 2009-08-31 的一次无尽八月支线：异世界人入团考试、排除法推理，以及被补写的过去。正文是中文第一人称故事，按八阶段故事圆环推进。属性名称、数值和检定结算方式留给以后模块；本模块只用直接选项。
- Done when: 选定的故事方向和第一人称语言写入 `Docs/MEMORY.md` 与 `Docs/GAME_DESIGN.md`，并与完整剧本复核（已达到）。

## P1

### DES-003 第 0 号完整剧本
- Status: Complete
- Dependencies: DES-002
- Current files: `Scenarios/00-zero-floor.md`
- Work: 一份中文第一人称 Markdown 模块，有完整故事圆环、原创正文、三个结局、线索解锁推理，以及直接选项。
- Done when: 约定章节、揭示条件、线索门槛及每拍选项齐全，已做编辑复核并试玩全部结局。旧版已达到；2026-09-30 重写版仍需构建并试玩 E01、E02、E03。

### ENG-001 Ren'Py 窗口运行时
- Status: Implemented; validation pending
- Dependencies: 用户要求离开控制台，改用 Ren'Py。发布目标是 `pack.bat` 打出的 Windows 版。
- Current files: `Play/game/script.rpy`、`Play/game/options.rpy`、`Play/game/story_data.py`、`Play/game/engine.rpy`、`Play/game/screens.rpy`、`pack.bat`、`pack.ps1`。
- Work: 源码推进选项，处理线索及旗标门槛和效果，可重读已发现材料，偶尔显示彩色 `■` 画面，从单一存档继续，并处理三个结局与送返结局的限定范围清理。玩家输出不含主持人笔记。2026-10-21 已用 `pack.ps1` 生成 exe，打包窗口能够打开；剧情试玩仍待完成。
- Done when: 静态审阅确认源码符合设计约定，`pack.bat` 生成 `Build/SOS_Project/SOS_Project.exe`，并试玩确认 E01、E02、E03。不运行自动测试套件。不添加 Unity。

### ENG-002 接入第 0 号剧本后续内容
- Status: Complete
- Dependencies: ENG-001、DES-003；接入后续内容时处理它们的核对结果。
- Current files: `Scenarios/00-zero-floor.md`、`Play/game/story_data.py`、`Play/game/engine.rpy`。
- Work: 接入 S06—S16、其余线索和手稿、线索解锁推理与两条结局路径，不让玩家看到主持人笔记。本模块保持直接选项，按剧情进度追加手稿，避免提前剧透。
- Done when: 静态流程审阅确认双结局按文档条件及反馈可达，且获授权的程序试玩证实两条路线（已达到）。

### REL-001 Windows Ren'Py 打包
- Status: Implemented; validation pending
- Dependencies: ENG-001、ENG-002。用户要求自己能打包，不必每次再让人代劳。
- Current files: `pack.bat`、`pack.ps1`、`Play/game/options.rpy`、`README.md`、本地被忽略的产物 `Build/SOS_Project/SOS_Project.exe`。
- Work: `pack.bat` 打出 Windows 游戏目录。E01 删除存档，并只安排删除该目录里的 `SOS_Project.exe`。2026-10-21 已用 `pack.ps1` 生成 `dist/SOS_Project/SOS_Project.exe`，窗口能够打开。在临时副本上观察 E01 清理仍待完成。
- Done when: `pack.bat` 已生成 exe，并且试玩确认 E01、E02、E03，包括在临时副本上确认 E01 清理。
