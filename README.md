# 音圧分布シミュレーション

このプログラムは、指定された直方体内の音圧分布を計算し、PPM形式の画像ファイルとして出力します。

## 使い方

### 1. ソースコードのコンパイル

`sound_pressure_distribution.c` ファイルをコンパイルするには、以下のコマンドを使用します。
数学関数（`cos`など）を使用しているため、` -lm` オプションで数学ライブラリをリンクする必要があります。

```bash
cc sound_pressure_distribution.c -o sound_pressure_distribution -lm

python sound_pressure.py

./sound_pressure_distribution

magick convert sound_pressure.ppm sound_pressure.png

convert sound_pressure.ppm sound_pressure.png

