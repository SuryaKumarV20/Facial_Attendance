import cv2

print("[INFO] Opening webcam...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Camera could not be opened!")
    exit()

print("[INFO] Press 'q' to quit...")
while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Frame not read properly")
        break

    cv2.imshow('Camera Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
