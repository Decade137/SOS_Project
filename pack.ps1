$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
Set-Location $root

$sdkVersion = "8.5.3"
$sdkRoot = Join-Path $root "tools\renpy-$sdkVersion-sdk"
$renpy = Join-Path $sdkRoot "renpy.py"
$python = Join-Path $sdkRoot "lib\py3-windows-x86_64\python.exe"
$fontCache = Join-Path $root "tools\cache"
$fontDir = Join-Path $root "Play\game\fonts"
$fonts = @(
    @{ Name = "NotoSansSC-Regular"; Tag = "Sans2.004"; Path = "Sans/SubsetOTF/SC" },
    @{ Name = "NotoSerifSC-Regular"; Tag = "Serif2.003"; Path = "Serif/SubsetOTF/SC" },
    @{ Name = "NotoSerifSC-Bold"; Tag = "Serif2.003"; Path = "Serif/SubsetOTF/SC" }
)
$packageDir = Join-Path $root "Build\packages"
$staging = Join-Path $root "Build\staging"
$gameDir = Join-Path $root "Build\SOS_Project"

function Get-RemoteFile([string]$Url, [string]$Destination) {
    if (Test-Path $Destination) {
        return
    }
    $folder = Split-Path $Destination
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
    Write-Host "下载 $Url"
    & curl.exe -L --fail --retry 3 -o $Destination $Url
    if ($LASTEXITCODE -ne 0) {
        if (Test-Path $Destination) {
            Remove-Item $Destination -Force
        }
        throw "下载失败：$Url"
    }
}

function Ensure-FontSource($Font) {
    $fontSource = Join-Path $fontCache ($Font.Name + ".otf")
    if ((Test-Path $fontSource) -and (Get-Item $fontSource).Length -ge 100000) {
        return
    }
    if (Test-Path $fontSource) {
        Remove-Item $fontSource -Force
    }
    $fontUrls = @(
        "https://github.com/notofonts/noto-cjk/raw/$($Font.Tag)/$($Font.Path)/$($Font.Name).otf",
        "https://cdn.jsdelivr.net/gh/notofonts/noto-cjk@$($Font.Tag)/$($Font.Path)/$($Font.Name).otf"
    )
    foreach ($url in $fontUrls) {
        try {
            Get-RemoteFile $url $fontSource
            if ((Get-Item $fontSource).Length -ge 100000) {
                return
            }
            Remove-Item $fontSource -Force
        } catch {
            if (Test-Path $fontSource) {
                Remove-Item $fontSource -Force
            }
        }
    }
    throw "下载中文字体失败：$($Font.Name)"
}

function Ensure-Font {
    foreach ($font in $fonts) {
        Ensure-FontSource $font
    }

    if (-not (Get-Command node -ErrorAction SilentlyContinue)) {
        $missing = $fonts | Where-Object { -not (Test-Path (Join-Path $fontDir ($_.Name + ".ttf"))) }
        if (-not $missing) {
            Write-Host "未找到 Node.js，沿用已有字体。"
            return
        }
        throw "准备中文字体需要 Node.js。请先安装 Node.js，再重新运行 pack.bat。"
    }

    if (-not (Test-Path (Join-Path $root "pack\node_modules\subset-font"))) {
        Push-Location (Join-Path $root "pack")
        & npm install --no-fund --no-audit
        if ($LASTEXITCODE -ne 0) {
            Pop-Location
            throw "安装字体工具失败。"
        }
        Pop-Location
    }
    & node (Join-Path $root "pack\subset-font.mjs")
    if ($LASTEXITCODE -ne 0) {
        throw "生成中文字体失败。"
    }
}

function Ensure-Sdk {
    if ((Test-Path $renpy) -and (Test-Path $python)) {
        return
    }
    $zip = Join-Path $root "tools\renpy-$sdkVersion-sdk.zip"
    Get-RemoteFile "https://www.renpy.org/dl/$sdkVersion/renpy-$sdkVersion-sdk.zip" $zip
    Write-Host "解压 Ren'Py SDK"
    if (Test-Path $sdkRoot) {
        Remove-Item $sdkRoot -Recurse -Force
    }
    New-Item -ItemType Directory -Force -Path (Join-Path $root "tools") | Out-Null
    & tar.exe -xf $zip -C (Join-Path $root "tools")
    if ($LASTEXITCODE -ne 0) {
        throw "解压 Ren'Py SDK 失败。"
    }
    if (-not (Test-Path $renpy)) {
        throw "SDK 里没有 renpy.py。"
    }
}

Ensure-Font
Ensure-Sdk

Write-Host "检查剧情数据"
& $python -c "import sys; sys.path.insert(0, r'$root\Play\game'); import story_data; story_data.validate()"
if ($LASTEXITCODE -ne 0) {
    throw "剧情数据检查失败。"
}

Write-Host "检查脚本"
& $python $renpy (Join-Path $root "Play") lint
if ($LASTEXITCODE -ne 0) {
    throw "Ren'Py 脚本检查失败。"
}

Write-Host "打包 Windows 版"
New-Item -ItemType Directory -Force -Path $packageDir | Out-Null
& $python $renpy (Join-Path $sdkRoot "launcher") distribute --destination $packageDir --package win --no-update (Join-Path $root "Play")
if ($LASTEXITCODE -ne 0) {
    throw "打包失败。"
}

$zip = Get-ChildItem $packageDir -Filter "*.zip" | Where-Object { $_.Name -notmatch "update" } | Select-Object -First 1
if ($null -eq $zip) {
    throw "打包目录里没有 zip。"
}

if (Test-Path $staging) {
    Remove-Item $staging -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $staging | Out-Null
& tar.exe -xf $zip.FullName -C $staging
if ($LASTEXITCODE -ne 0) {
    throw "解压游戏包失败。"
}

$exe = Get-ChildItem $staging -Recurse -Filter "SOS_Project.exe" | Select-Object -First 1
if ($null -eq $exe) {
    throw "游戏包里没有 SOS_Project.exe。"
}

if (Test-Path $gameDir) {
    Remove-Item $gameDir -Recurse -Force
}
if ($exe.Directory.FullName -eq (Resolve-Path $staging).Path) {
    Rename-Item $staging $gameDir
} else {
    Move-Item $exe.Directory.FullName $gameDir
    Remove-Item $staging -Recurse -Force
}

Write-Host ""
Write-Host "可以运行："
Write-Host (Join-Path $gameDir "SOS_Project.exe")
