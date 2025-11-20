import cv2
import numpy as np
import os
import time


#  USBカメラから2つの画像を読み込んで保存
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラを開けません")
    exit()

print("1枚目を撮影します...")
time.sleep(1)             # 安定のため待つ
ret, img1 = cap.read()
cv2.imwrite("img1.jpg", img1)

print("2枚目を撮影します...")
time.sleep(1)
ret, img2 = cap.read()
cv2.imwrite("img2.jpg", img2)

cap.release()

print("取得した画像サイズ:", img1.shape)   # (H, W, 3)


#  --- OpenCV を用いたグレースケール化 ---
gray1_cv = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2_cv = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray1_cv.jpg", gray1_cv)
cv2.imwrite("gray2_cv.jpg", gray2_cv)


#  --- OpenCV を使わないグレースケール化 3種 ---

# ▼手法1：平均値法（(R+G+B)/3）
gray1_avg = np.mean(img1, axis=2).astype(np.uint8)
gray2_avg = np.mean(img2, axis=2).astype(np.uint8)

# ▼手法2：輝度法（人間の視覚）
gray1_lumi = (0.299 * img1[:, :, 2] + 0.587 * img1[:, :, 1] + 0.114 * img1[:, :, 0]).astype(np.uint8)
gray2_lumi = (0.299 * img2[:, :, 2] + 0.587 * img2[:, :, 1] + 0.114 * img2[:, :, 0]).astype(np.uint8)

# ▼手法3：最大値法（max(R,G,B)）
gray1_max = np.max(img1, axis=2).astype(np.uint8)
gray2_max = np.max(img2, axis=2).astype(np.uint8)

# 保存（3手法）
cv2.imwrite("gray1_avg.jpg",  gray1_avg)
cv2.imwrite("gray2_avg.jpg",  gray2_avg)
cv2.imwrite("gray1_lumi.jpg", gray1_lumi)
cv2.imwrite("gray2_lumi.jpg", gray2_lumi)
cv2.imwrite("gray1_max.jpg",  gray1_max)
cv2.imwrite("gray2_max.jpg",  gray2_max)


#  差分処理（OpenCV版）
diff_cv = cv2.absdiff(gray1_cv, gray2_cv)
cv2.imshow("Diff (OpenCV)", diff_cv)
cv2.imwrite("diff_cv.jpg", diff_cv)


#  差分処理（OpenCVを使わない版）
diff_avg = np.abs(gray1_avg.astype(int)  - gray2_avg.astype(int)).astype(np.uint8)
diff_lumi = np.abs(gray1_lumi.astype(int) - gray2_lumi.astype(int)).astype(np.uint8)
diff_max = np.abs(gray1_max.astype(int)  - gray2_max.astype(int)).astype(np.uint8)

cv2.imwrite("diff_avg.jpg", diff_avg)
cv2.imwrite("diff_lumi.jpg", diff_lumi)
cv2.imwrite("diff_max.jpg", diff_max)

cv2.imshow("Diff Avg", diff_avg)
cv2.imshow("Diff Lumi", diff_lumi)
cv2.imshow("Diff Max", diff_max)

cv2.waitKey(0)
cv2.destroyAllWindows()


#  保存画像のファイルサイズ確認
files = [
    "img1.jpg", "img2.jpg",
    "gray1_cv.jpg", "gray2_cv.jpg",
    "gray1_avg.jpg", "gray2_avg.jpg",
    "gray1_lumi.jpg", "gray2_lumi.jpg",
    "gray1_max.jpg", "gray2_max.jpg",
    "diff_cv.jpg",
    "diff_avg.jpg", "diff_lumi.jpg", "diff_max.jpg"
]

print("\n--- 保存画像のサイズ ---")
for f in files:
    print(f"{f}: {os.path.getsize(f)} bytes")