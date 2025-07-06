import numpy as np
import matplotlib.pyplot as plt

# 定数の設定
# Lx, Ly は正規化されているため、ここでは1として扱います
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

# --- 音圧分布図の描画 ---
plt.figure(figsize=(8, 6)) # 図のサイズを設定

# contourf を使用して等高線図（塗りつぶしあり）を描画
# cmap='viridis' はカラーマップの一種で、色の濃淡で値の大小を表現
# levels は等高線の数を指定
contour = plt.contourf(Y_norm, X_norm, pressure_distribution, levels=50, cmap='viridis') # Yを横軸、Xを縦軸に指定
plt.colorbar(contour, label='Sound Pressure') # カラーバーの追加

# タイトルと軸ラベルの設定
plt.title(f'Sound Pressure Distribution (nx={nx}, ny={ny})')
plt.xlabel('y/Ly') # 横軸をy/Ly
plt.ylabel('x/Lx') # 縦軸をx/Lx

# グリッドの表示
plt.grid(True, linestyle='--', alpha=0.7)

# レイアウトの調整
plt.tight_layout()

# 図の表示
plt.show()