import numpy as np
import cv2
from matplotlib import pyplot as plt
image = cv2.imread("image.jpg")
# 閉曲線を定義
vertices = np.array([(100, 100), (800, 400),(800, 500),(100, 500)])
# 閉曲線を内包する領域を作成
mask = np.zeros_like(image[:, :, 0])  # マスク用のゼロ配列を作成
cv2.fillPoly(mask, [vertices], 255)
# マスクを元画像に適用してフィルタリング
filtered_image = cv2.bitwise_and(image, image, mask=mask)
plt.imshow(filtered_image)

