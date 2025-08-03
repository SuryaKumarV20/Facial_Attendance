import cv2
import os
import csv

def TakeImage(enrollment, name):
    haar_cascade_path = "haarcascade_frontalface_default.xml"
    trainimage_path = "TrainingImage"

    if enrollment.strip() == "" or name.strip() == "":
        print("[ERROR] Enrollment number or Name is missing.")
        return

    try:
        if not os.path.exists(trainimage_path):
            os.makedirs(trainimage_path)

        cam = cv2.VideoCapture(0)
        detector = cv2.CascadeClassifier(haar_cascade_path)
        sampleNum = 0

        print("[INFO] Starting to capture images. Press 'q' to quit.")

        while True:
            ret, img = cam.read()
            if not ret:
                print("[ERROR] Failed to open camera.")
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                sampleNum += 1
                face_img = gray[y:y+h, x:x+w]
                filename = f"{enrollment}_{name}_{sampleNum}.jpg"
                filepath = os.path.join(trainimage_path, filename)
                cv2.imwrite(filepath, face_img)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.imshow("Capturing Images", img)

            if cv2.waitKey(1) & 0xFF == ord('q') or sampleNum >= 50:
                break

        cam.release()
        cv2.destroyAllWindows()

        # Save to CSV
        with open("StudentDetails/studentdetails.csv", "a+", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([enrollment, name])

        print(f"[✅] Images Saved for ER No: {enrollment}, Name: {name}")

    except Exception as e:
        print(f"[❌ ERROR] {e}")

# 👇 Run only when executed directly
if __name__ == "__main__":
    enrollment = input("Enter Enrollment Number: ")
    name = input("Enter Name: ")
    TakeImage(enrollment.strip(), name.strip())
