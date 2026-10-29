# SOS_Project

Unofficial single-player text game. The player picks bullet-marked options, plays themself, and solves deduction puzzles. Scenario modules follow a Call of Cthulhu–style TRPG structure. The fiction is the world of The Melancholy of Haruhi Suzumiya.

非官方单人文字游戏。玩家选择圆点选项，扮演自己，进行推理解谜。剧本模块用类似 COC 跑团的结构。故事世界是《凉宫春日的忧郁》。

- Policy: [AGENTS.md](AGENTS.md)
- Design: [Docs/GAME_DESIGN.md](Docs/GAME_DESIGN.md) · [中文](Docs/GAME_DESIGN.zh-CN.md)
- Handoff: [Docs/MEMORY.md](Docs/MEMORY.md) · [Docs/TODO.md](Docs/TODO.md)

The playable game is the Ren'Py 8.5.3 project in `Play/`. On Windows, double-click `pack.bat` or run `powershell -NoProfile -ExecutionPolicy Bypass -File pack.ps1`. The script downloads the Ren'Py SDK on first use, prepares a Chinese font, and writes `Build/SOS_Project/SOS_Project.exe`. Double-click that exe. Keep the whole `Build/SOS_Project` folder together; the exe starts the game and the files beside it are the runtime. A player does not install Ren'Py. Node.js is required on the machine that packs, because the font subset is rebuilt from the script text. Progress is saved in `%LOCALAPPDATA%/SOS_Project/save.json`.

可玩工程是 `Play/` 里的 Ren'Py 8.5.3 项目。在 Windows 上双击 `pack.bat`，或运行 `powershell -NoProfile -ExecutionPolicy Bypass -File pack.ps1`。脚本会在第一次使用时下载 Ren'Py SDK、准备中文字体，并写出 `Build/SOS_Project/SOS_Project.exe`。双击这个 exe 即可开始。整个 `Build/SOS_Project` 文件夹要留在一起：exe 负责启动，旁边的文件是运行所需的程序。玩家不必安装 Ren'Py。打包的那台电脑需要 Node.js，因为字体子集会按脚本文字重新生成。进度存在 `%LOCALAPPDATA%/SOS_Project/save.json`。
