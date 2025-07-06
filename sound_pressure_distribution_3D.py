import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 3Dプロットに必要なモジュール

# 定数の設定
nx = 2    # x方向のモード次数
ny = 2    # y方向のモード次数
amplitude = 1.0 # 振幅の最大値

# 正規化された座標の範囲を設定 (x/Lx, y/Ly)
# 各軸に400点を使用し、滑らかなプロットを作成
x_normalized = np.linspace(0, 1, 400) # x/Lx
y_normalized = np.linspace(0, 1, 400) # y/Ly

# グリッドの作成
X_norm, Y_norm = np.meshgrid(x_normalized, y_normalized)

# 音圧分布の計算
# P(x/Lx, y/Ly) = A * cos(nx * pi * (x/Lx)) * cos(ny * pi * (y/Ly))
pressure_distribution = amplitude * np.cos(nx * np.pi * X_norm) * np.cos(ny * np.pi * Y_norm)

# --- 3次元音圧分布図の描画 ---
fig = plt.figure(figsize=(10, 8)) # 図のサイズを設定
ax = fig.add_subplot(111, projection='3d') # 3Dプロット用のサブプロットを追加

# plot_surface を使用して3Dサーフェスプロットを描画
# rstride, cstride はグリッドの密度を調整（値を大きくすると粗くなる）
# cmap はカラーマップ
surface = ax.plot_surface(Y_norm, X_norm, pressure_distribution, cmap='viridis', rstride=5, cstride=5) # YをX軸、XをY軸に指定して回転

# タイトルと軸ラベルの設定
ax.set_title(f'3D Sound Pressure Distribution (nx={nx}, ny={ny})')
ax.set_xlabel('y/Ly') # X軸をy/Ly
ax.set_ylabel('x/Lx') # Y軸をx/Lx
ax.set_zlabel('Sound Pressure') # Z軸を音圧

# カラーバーの追加
fig.colorbar(surface, shrink=0.5, aspect=10, label='Sound Pressure')

# レイアウトの調整
plt.tight_layout()

# 図の表示
plt.show()