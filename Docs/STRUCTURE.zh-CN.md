# 结构

英文 `Docs/STRUCTURE.md` 为准。本文件只复述同一批事实。

## 根目录

- `AGENTS.md`：本仓库的常驻政策。
- `README.md`：指向政策与设计约定的短说明。
- `Docs/AI_PROJECT_HANDOFF_RULES.md`：可移植的交接规范。不是本游戏的设计。
- `Docs/MEMORY.md`：仍成立的事实和决定。
- `Docs/PROCESS.md`：工作方式和会话记录。
- `Docs/STRUCTURE.md`：本目录图。
- `Docs/TODO.md`：待办。
- `Docs/GAME_DESIGN.md`：控制台循环、类似 COC 的模块约定、凉宫春日故事边界。
- `Game/SOS_Project.csproj`：面向 `net10.0` 的控制台工程，把可玩的剧情数据编译进程序。
- `Game/Program.cs`：控制台入口。
- `Game/Story.cs`：场景、选项、线索、手稿和状态数据。
- `Game/StoryRunner.cs`：编号选项循环、状态效果、重读与可选彩色画面。
- `Scenarios/00-zero-floor.md`：已写的中文第一人称第 0 号剧本，含八阶段故事圆环与完整模块章节。
- `Scenarios/ZeroFloor.Play.cs`：编译用玩家剧情数据，涵盖开场、S00—S05、K01—K03 和 H01 初版。
- `Docs/LOGS/`：长会话笔记。目前只有 `.gitkeep`。
- `.git/`：仓库元数据。不要手改。

中文镜像是同一路径加上 `.zh-CN.md`。没有 `AGENTS.zh-CN.md`。

## 功能 → 文件

- 交接政策：`AGENTS.md`，`Docs/AI_PROJECT_HANDOFF_RULES.md`
- 产品约定：`Docs/GAME_DESIGN.md`，`Docs/GAME_DESIGN.zh-CN.md`
- 第一份剧本的决定：`Docs/MEMORY.md`、`Docs/GAME_DESIGN.md` 及其中文镜像。
- 第 0 号剧本正文与主持人笔记：`Scenarios/00-zero-floor.md`（中文源文件；尚无英文译本）。
- 第 0 号剧本可游玩的开场数据：`Scenarios/ZeroFloor.Play.cs`（由 Markdown 整理而来；玩家输出不含主持人笔记）。
- 控制台程序：`Game/Program.cs`、`Game/Story.cs`、`Game/StoryRunner.cs`、`Game/SOS_Project.csproj`。
- 仍成立的决定：`Docs/MEMORY.md`，`Docs/MEMORY.zh-CN.md`
- 下一步：`Docs/TODO.md`，`Docs/TODO.zh-CN.md`
- 运行时决定：.NET 10 的 C# 控制台，目标是发布为 Windows x64 自包含单文件 exe，写在 `Docs/GAME_DESIGN.md`。源码位于 `Game/`，尚未发布。

`Scenarios/` 包含第 0 号完整剧本草稿和编译用开场首段。用户已要求开始实现；C# 工程位于 `Game/`。

## 文档索引

- `Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` 未创建。只有在产生证据文件时才添加。
