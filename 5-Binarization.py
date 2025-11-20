import cv2
import numpy as np
import os


#  USBカメラから画像を読み込む
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラを開けません")
    exit()

ret, img = cap.read()
cap.release()

if not ret:
    print("画像が取得できません")
    exit()

print("【入力画像サイズ】", img.shape)   # (H, W, C)


#  --- OpenCV を用いたグレースケール化 ---
gray_cv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_cv.jpg", gray_cv)


#  --- OpenCV を用いないグレースケール化 ---
#       ここでは平均値法を使用
gray_avg = np.mean(img, axis=2).astype(np.uint8)
cv2.imwrite("gray_avg.jpg", gray_avg)


#  --- OpenCV を用いた 2値化（手法1: 固定閾値）---
_, binary_cv_100 = cv2.threshold(gray_cv, 100, 255, cv2.THRESH_BINARY)
_, binary_cv_150 = cv2.threshold(gray_cv, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite("binary_cv_100.jpg", binary_cv_100)
cv2.imwrite("binary_cv_150.jpg", binary_cv_150)


#  --- OpenCV を用いない 2値化 ---
# 閾値100
binary_np_100 = np.where(gray_avg > 100, 255, 0).astype(np.uint8)

# 閾値150
binary_np_150 = np.where(gray_avg > 150, 255, 0).astype(np.uint8)

cv2.imwrite("binary_np_100.jpg", binary_np_100)
cv2.imwrite("binary_np_150.jpg", binary_np_150)


#  表示（必要な画像のみ表示）
cv2.imshow("Gray (OpenCV)", gray_cv)
cv2.imshow("Binary CV 100", binary_cv_100)
cv2.imshow("Binary CV 150", binary_cv_150)
cv2.imshow("Binary NP 100", binary_np_100)
cv2.imshow("Binary NP 150", binary_np_150)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 保存した画像のファイルサイズ確認
print("\n--- 保存画像のファイルサイズ ---")
files = [
    "gray_cv.jpg", "gray_avg.jpg",
    "binary_cv_100.jpg", "binary_cv_150.jpg",
    "binary_np_100.jpg", "binary_np_150.jpg"
]

for f in files:
    print(f"{f}: {os.path.getsize(f)} bytes")