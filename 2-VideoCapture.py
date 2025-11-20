import cv2

cap = cv2.VideoCapture(0)

# パラメータ
width = 640
height = 480
fps = 30

# カメラへ設定を適用
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, fps)

print("設定した解像度:", width, "x", height)
print("設定したFPS:", fps)
print("実際の解像度:", cap.get(cv2.CAP_PROP_FRAME_WIDTH), "x", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("実際のFPS:", cap.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera (Press q to Quit)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
