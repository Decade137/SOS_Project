# 结构

英文 `Docs/STRUCTURE.md` 为准。本文件只复述同一批事实。

## 根目录

- `AGENTS.md`：本仓库的常驻政策。
- `README.md`：指向政策与设计约定的短说明。
- `.gitignore`：忽略 `tools/`、`Build/`、`pack/node_modules/`，以及 Ren'Py 缓存和日志。
- `pack.bat` 与 `pack.ps1`：需要时下载 Ren'Py 8.5.3，生成中文字体子集，并写出 `Build/SOS_Project/SOS_Project.exe`。
- `pack/subset-font.mjs`：用 `tools/cache/` 里的 Noto 源字体，在 `Play/game/fonts/` 生成 `NotoSansSC-Regular`、`NotoSerifSC-Regular` 和 `NotoSerifSC-Bold` 子集。
- `Docs/AI_PROJECT_HANDOFF_RULES.md`：可移植的交接规范。不是本游戏的设计。
- `Docs/MEMORY.md`：仍成立的事实和决定。
- `Docs/PROCESS.md`：工作方式和会话记录。
- `Docs/STRUCTURE.md`：本目录图。
- `Docs/TODO.md`：待办。
- `Docs/GAME_DESIGN.md`：游玩循环、类似 COC 的模块约定、凉宫春日故事边界。
- `Play/game/options.rpy`：Ren'Py 窗口、构建名 `SOS_Project`，以及停用会抢键的默认快捷键。
- `Play/game/script.rpy`：跳过 Ren'Py 默认主菜单并启动游戏。
- `Play/game/story_data.py`：玩家可见的开场、场景、选项、线索、手稿、画面和结局。长正文在 `story_prose.py`、`story_long.py`、`story_more2.py`、`story_more3.py`，由它导入。
- `Play/game/engine.rpy`：页面流程、线索与旗标门槛、一份 JSON 存档、档案重读，以及送返结局的限定范围清理。
- `Play/game/screens.rpy`：居中的阅读栏（`reading`）、开始页（`title_page`）、带选中竖条的共用选项列表（`choice_list`）、共用按键与计时器（`page_keys`）、确认框和通知、页面底色，以及彩色 `■` 网格。
- `Play/game/fonts/`：菜单和提示用的 Noto Sans SC 子集，正文和标题用的 Noto Serif SC Regular 与 Bold 子集，以及 OFL 许可。
- `Scenarios/00-zero-floor.md`：已写的中文第一人称第 0 号剧本《凉宫春日的心愿》，含八阶段故事圆环与完整模块章节；文件名沿用旧名。`Scenarios/ZeroFloor.Play.cs` 与 `Game/` 控制台工程已于 2026-10-29 删除。
- `Docs/LOGS/`：长会话笔记。目前只有 `.gitkeep`。
- `.git/`：仓库元数据。不要手改。

中文镜像是同一路径加上 `.zh-CN.md`。没有 `AGENTS.zh-CN.md`。

## 功能 → 文件

- 交接政策：`AGENTS.md`，`Docs/AI_PROJECT_HANDOFF_RULES.md`
- 产品约定：`Docs/GAME_DESIGN.md`，`Docs/GAME_DESIGN.zh-CN.md`
- 第一份剧本的决定：`Docs/MEMORY.md`、`Docs/GAME_DESIGN.md` 及其中文镜像。
- 第 0 号剧本正文与主持人笔记：`Scenarios/00-zero-floor.md`（中文源文件；尚无英文译本）。
- 第 0 号剧本可游玩的剧情数据：`Play/game/story_data.py`（由 Markdown 整理而来；玩家输出不含主持人笔记）。长正文模块：`story_prose.py`、`story_long.py`、`story_more2.py`、`story_more3.py`。
- Ren'Py 运行时：`Play/game/script.rpy`、`Play/game/engine.rpy`、`Play/game/screens.rpy`、`Play/game/options.rpy`、`Play/game/story_data.py`。
- 窗口、开始页与菜单输入：`Play/game/screens.rpy` 和 `Play/game/engine.rpy`；交互约定：`Docs/GAME_DESIGN.md` 和 `Docs/GAME_DESIGN.zh-CN.md`。
- 打包：`pack.bat`、`pack.ps1`、`pack/subset-font.mjs`。产物在被忽略的 `Build/`。SDK 下载在被忽略的 `tools/`。
- 仍成立的决定：`Docs/MEMORY.md`，`Docs/MEMORY.zh-CN.md`
- 下一步：`Docs/TODO.md`，`Docs/TODO.zh-CN.md`
- 运行时决定：Ren'Py 8.5.3 窗口，打包为 Windows x64，写在 `Docs/GAME_DESIGN.md`。源码位于 `Play/`。构建出的游戏是 `Build/SOS_Project/SOS_Project.exe`。

`Scenarios/` 包含第 0 号剧本。第 0 号剧本默认玩家熟悉 SOS 团及其相关故事（包括无尽八月的循环），玩家输出通过细节、记录和角色反应体现这份熟悉，不直接解释其来源。可玩工程位于 `Play/`。

剧本 Markdown 与 `Play/game/story_data.py` 在 2026-10-29 对齐，包括加长的调查场、K11–K13 和 H05–H06。存档是 `%LOCALAPPDATA%/SOS_Project/save.json`，版本 4。包括版本 3 在内的旧存档不会被读取。`save.bin` 不会被读取。这次加长之前的存档，如果场景 id 还在，仍能读；已经走过的场不会重放。

## 文档索引

- `Docs/MEMORY.md`、`Docs/PROCESS.md`、`Docs/STRUCTURE.md`、`Docs/TODO.md`
- `Docs/GAME_DESIGN.md`
- `Docs/LOGS/`
- `Docs/Reports/` 未创建。只有在产生证据文件时才添加。
