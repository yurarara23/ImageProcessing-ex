import cv2
import os

cap = cv2.VideoCapture(0)

width = 640
height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"設定した解像度: {width}x{height}")
print(f"カメラの実際の解像度: {actual_width}x{actual_height}")

ret, frame = cap.read()

cap.release()

# メモリ上の画像データサイズを確認 
input_size_bytes = frame.nbytes
print(f"カメラから取り込んだ画像データサイズ: {input_size_bytes} バイト")

# JPEGで保存
output_path = "output.jpg"
cv2.imwrite(output_path, frame)

# 保存されたJPEGのデータサイズを取得
output_size_bytes = os.path.getsize(output_path)
print(f"保存したJPEGファイルのサイズ: {output_size_bytes} バイト")