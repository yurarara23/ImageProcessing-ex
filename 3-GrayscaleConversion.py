import cv2
import numpy as np
import os

# -------------------------------
#  USB カメラから画像を読み込む
# -------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラが開けません")
    exit()

ret, frame = cap.read()
cap.release()

if not ret:
    print("画像を取得できませんでした")
    exit()

print("入力画像のサイズ（NumPy配列）:", frame.shape)  # (H, W, 3)


#  OpenCV の関数を用いたグレースケール化
gray_cv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#  OpenCV を用いず自前でグレースケール化
#     代表的な手法 2 種類を実装する

# ---- 手法1：平均値法 (R + G + B) / 3 ----
gray_avg = np.mean(frame, axis=2).astype(np.uint8)

# ---- 手法2：輝度法 (0.299R + 0.587G + 0.114B) ----
# 人間の視覚に基づく一般的な白黒化
gray_lumi = (
    0.299 * frame[:, :, 2] +
    0.587 * frame[:, :, 1] +
    0.114 * frame[:, :, 0]
).astype(np.uint8)

# 必要ならもっと追加できます（最大値法・最小値法など）


#  保存する
cv2.imwrite("gray_cv.jpg", gray_cv)
cv2.imwrite("gray_avg.jpg", gray_avg)
cv2.imwrite("gray_lumi.jpg", gray_lumi)

print("保存しました：gray_cv.jpg")
print("保存しました：gray_avg.jpg")
print("保存しました：gray_lumi.jpg")


#  ファイルサイズを確認する
print("\n--- 保存画像のファイルサイズ ---")
print("gray_cv.jpg   :", os.path.getsize("gray_cv.jpg"), "bytes")
print("gray_avg.jpg  :", os.path.getsize("gray_avg.jpg"), "bytes")
print("gray_lumi.jpg :", os.path.getsize("gray_lumi.jpg"), "bytes")