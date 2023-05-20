import numpy as np
import cv2
from matplotlib import pyplot as plt
image = cv2.imread("image.jpg")
# 閉曲線を定義
vertices = np.array([(100, 100), (800, 400),(800, 500),(100, 500)])
# 閉曲線を内包する領域を作成

# 楕円のパラメータ
center_x = 600
center_y = 600
major_radius = 80
minor_radius = 520
angle = 30  # 度数法で指定

mask = np.zeros_like(image[:, :, 0])  # マスク用のゼロ配列を作成
cv2.fillPoly(mask, [vertices], 255)
# 楕円を描画して領域内のピクセルを抽出
cv2.ellipse(mask, (center_x, center_y), (major_radius, minor_radius), angle, 0, 360, 255, -1)

# マスクを元画像に適用してフィルタリング
filtered_image = cv2.bitwise_and(image, image, mask=mask)
plt.imshow(filtered_image)
print("end!")
