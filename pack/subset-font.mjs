import fs from "fs";
import path from "path";
import subsetFont from "subset-font";

const root = path.resolve("Play/game");
const fonts = [
    ["tools/cache/NotoSansSC-Regular.otf", "Play/game/fonts/NotoSansSC-Regular.ttf"],
    ["tools/cache/NotoSerifSC-Regular.otf", "Play/game/fonts/NotoSerifSC-Regular.ttf"],
    ["tools/cache/NotoSerifSC-Bold.otf", "Play/game/fonts/NotoSerifSC-Bold.ttf"],
];
const characters = new Set("■");

for (let code = 32; code < 127; code += 1) {
    characters.add(String.fromCharCode(code));
}

function walk(directory) {
    for (const name of fs.readdirSync(directory)) {
        const fullPath = path.join(directory, name);
        if (fs.statSync(fullPath).isDirectory()) {
            if (name === "cache" || name === "fonts") {
                continue;
            }
            walk(fullPath);
            continue;
        }
        if (name.endsWith(".py") || name.endsWith(".rpy")) {
            for (const character of fs.readFileSync(fullPath, "utf8")) {
                characters.add(character);
            }
        }
    }
}

walk(root);
const text = [...characters].join("");
for (const [sourcePath, destinationPath] of fonts) {
    const destination = path.resolve(destinationPath);
    const subset = await subsetFont(fs.readFileSync(path.resolve(sourcePath)), text, {
        targetFormat: "truetype",
    });
    fs.mkdirSync(path.dirname(destination), { recursive: true });
    fs.writeFileSync(destination, subset);
    console.log(`${path.basename(destination)} ${subset.length} 字节，${characters.size} 个字符`);
}
