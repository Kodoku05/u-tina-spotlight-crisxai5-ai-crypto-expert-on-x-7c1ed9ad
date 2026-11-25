// Entry program: copies POST.json (the X post address) to the output
// directory, where the make.fun gate reads it. Standard library only.
import { copyFile, mkdir } from 'node:fs/promises';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR || '/bot';
const outputDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
const source = join(botDir, 'POST.json');
const destination = join(outputDir, 'POST.json');

try {
  await mkdir(outputDir, { recursive: true });
  await copyFile(source, destination);
} catch (error) {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Could not copy POST.json. Check that ${source} exists and that ${outputDir} is writable: ${message}`);
  process.exit(1);
}
