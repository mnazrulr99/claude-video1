import {bundle} from '@remotion/bundler';
import {renderStill, selectComposition} from '@remotion/renderer';
import path from 'path';
const times = JSON.parse(process.argv[2]); const out = process.argv[3]; const showSafe = process.argv[4]==='1';
const serveUrl = await bundle({entryPoint: path.resolve('src/index.ts')});
const browserExecutable='/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell';
const comp = await selectComposition({serveUrl, id: 'JamWira', inputProps: {showSafe}, browserExecutable});
for (const t of times) {
  await renderStill({composition: comp, serveUrl, output: `${out}/f_${String(t).padStart(5,'0')}.png`, frame: Math.round(t*30), inputProps: {showSafe}, scale: 0.5, browserExecutable, chromiumOptions:{gl:'swangle'}});
  console.log('done', t);
}
