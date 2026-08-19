const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const inputFile = path.join(__dirname, 'channel_icon_master.svg');
const outputSizes = [800, 176, 48];

async function renderIcon() {
  console.log('SVG → PNG レンダリング開始...\n');

  try {
    // 各サイズでレンダリング
    for (const size of outputSizes) {
      const outputFile = path.join(__dirname, `channel_icon_${size}.png`);

      await sharp(inputFile, { density: 384 })
        .resize(size, size, { fit: 'contain', background: { r: 30, g: 43, b: 66, alpha: 1 } })
        .png()
        .toFile(outputFile);

      const stats = fs.statSync(outputFile);
      const fileSize = stats.size;

      console.log(`✓ ${path.basename(outputFile)}`);
      console.log(`  実寸: ${size}×${size}px`);
      console.log(`  ファイルサイズ: ${fileSize} bytes`);
      console.log(`  パス: ${outputFile}\n`);
    }

    // 48版を 288px に NEAREST で拡大（目視確認用）
    const zoomFile = path.join(__dirname, 'channel_icon_48_zoom.png');
    const icon48 = path.join(__dirname, 'channel_icon_48.png');

    await sharp(icon48)
      .resize(288, 288, { kernel: 'nearest', fit: 'contain', background: { r: 30, g: 43, b: 66, alpha: 1 } })
      .png()
      .toFile(zoomFile);

    const zoomStats = fs.statSync(zoomFile);
    console.log(`✓ ${path.basename(zoomFile)} (目視確認用, NEAREST拡大)`);
    console.log(`  実寸: 288×288px`);
    console.log(`  ファイルサイズ: ${zoomStats.size} bytes`);
    console.log(`  パス: ${zoomFile}\n`);

    console.log('✓ レンダリング完了');
  } catch (error) {
    console.error('エラーが発生しました:', error.message);
    process.exit(1);
  }
}

renderIcon();
