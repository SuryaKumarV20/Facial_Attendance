import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[ERROR] Cannot open camera")
    exit()

print("[INFO] Camera opened successfully")

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to grab frame")
        break

    cv2.imshow("Test Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
