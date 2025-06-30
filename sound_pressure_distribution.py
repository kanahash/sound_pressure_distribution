import numpy as np
import matplotlib.pyplot as plt

# 直方体のサイズを設定（仮の値、必要に応じて変更してください）
Lx = 1.0
Ly = 1.0

# nx = 2, ny = 2 のモード
nx = 2
ny = 2

# xとyの座標範囲を生成
# 細かくするほど滑らかな図になります
x = np.linspace(0, Lx, 200)
y = np.linspace(0, Ly, 200)

# 2Dグリッドの作成
X, Y = np.meshgrid(x, y)

# 音圧分布の計算
# P(x, y) = cos(nx * pi * x / Lx) * cos(ny * pi * y / Ly)
P = np.cos(nx * np.pi * X / Lx) * np.cos(ny * np.pi * Y / Ly)

# プロットの作成
plt.figure(figsize=(8, 6))
plt.imshow(P, origin='lower', extent=[0, Lx, 0, Ly], cmap='coolwarm', aspect='auto')

# カラーバーの追加
cbar = plt.colorbar()
cbar.set_label('Sound Pressure (normalized)')

# タイトルと軸ラベルの設定
plt.title(f'Sound Pressure Distribution (nx={nx}, ny={ny})')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# グリッドの表示（任意）
plt.grid(True, linestyle=':', alpha=0.7)

# プロットの表示
plt.show()