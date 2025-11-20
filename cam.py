import cv2

cap = cv2.VideoCapture(0)

width = 640
height = 480
fps = 30

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera (Press q to Quit)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()