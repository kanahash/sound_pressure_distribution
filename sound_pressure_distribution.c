#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define LX 1.0 // 直方体のx方向の長さ
#define LY 1.0 // 直方体のy方向の長さ

#define NX 2 // nxモード
#define NY 2 // nyモード

#define WIDTH 400  // 画像の幅（ピクセル数）
#define HEIGHT 400 // 画像の高さ（ピクセル数）

int	main(void)
{
	FILE	*fp;
	double	pressure;

	int x_px, y_px;
	double x_coord, y_coord;
	int r, g, b; // RGB値
	// PPMファイルを開く (バイナリモードで書き込み)
	fp = fopen("sound_pressure.ppm", "wb");
	if (fp == NULL)
	{
		perror("Error opening file");
		return (1);
	}
	// PPMヘッダーの書き込み
	// P6: バイナリ形式のPPM
	// WIDTH HEIGHT: 画像のサイズ
	// 255: 最大色値 (8ビットカラー)
	fprintf(fp, "P6\n%d %d\n255\n", WIDTH, HEIGHT);
	// ピクセルごとに音圧を計算し、色にマッピング
	for (y_px = 0; y_px < HEIGHT; y_px++)
	{
		for (x_px = 0; x_px < WIDTH; x_px++)
		{
			// ピクセル座標を物理座標に変換
			x_coord = (double)x_px / (WIDTH - 1) * LX;
			y_coord = (double)y_px / (HEIGHT - 1) * LY;
			// 音圧の計算
			// P(x, y) = cos(nx * pi * x / Lx) * cos(ny * pi * y / Ly)
			pressure = cos(NX * M_PI * x_coord / LX) * cos(NY * M_PI * y_coord
					/ LY);
			// 音圧をRGB値にマッピング
			// -1.0から1.0の範囲を0から1に正規化: (pressure + 1.0) / 2.0
			// これをカラーマップに変換
			// 例: -1.0 (青) -> 0.0 (黒/紫) -> 1.0 (赤) のようなグラデーション
			// coolwarmに近いカラーマップを簡易的に作成
			double normalized_pressure = (pressure + 1.0) / 2.0; // 0.0 to 1.0
			if (normalized_pressure < 0.5)
			{ // 青から黒/紫へ
				r = (int)(255 * 2 * normalized_pressure);
				g = (int)(255 * 2 * normalized_pressure);
				b = 255;
			}
			else
			{ // 黒/紫から赤へ
				r = 255;
				g = (int)(255 * 2 * (1.0 - normalized_pressure));
				b = (int)(255 * 2 * (1.0 - normalized_pressure));
			}
			// 中央付近（音圧0）を白に近づける調整
			double abs_pressure_scaled = fabs(pressure); // 0 (節) -> 1 (腹)
			if (abs_pressure_scaled < 0.1)
			{                                                  // 節の付近
				double mix_factor = abs_pressure_scaled / 0.1; // 0 to 1
				r = (int)(r * mix_factor + 255 * (1.0 - mix_factor));
				g = (int)(g * mix_factor + 255 * (1.0 - mix_factor));
				b = (int)(b * mix_factor + 255 * (1.0 - mix_factor));
			}
			// RGB値をファイルに書き込む
			fputc((unsigned char)r, fp);
			fputc((unsigned char)g, fp);
			fputc((unsigned char)b, fp);
		}
	}
	// ファイルを閉じる
	fclose(fp);
	printf("Sound pressure distribution saved to sound_pressure.ppm\n");
	return (0);
}
