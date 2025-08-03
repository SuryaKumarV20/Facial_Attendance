import os
import cv2
import numpy as np
from PIL import Image

def train_classifier():
    data_dir = "TrainingImage"
    if not os.path.exists(data_dir):
        print("[❌] TrainingImage folder not found.")
        return

    image_paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []

    print(f"[INFO] Found {len(image_paths)} image files for training...")

    for image_path in image_paths:
        try:
            img = Image.open(image_path).convert('L')
            image_np = np.array(img, 'uint8')
            filename = os.path.split(image_path)[-1]
            id_str = filename.split('_')[0]

            # Handle non-integer ID by hashing
            id_num = abs(hash(id_str)) % (10 ** 8)

            faces.append(image_np)
            ids.append(id_num)
            print(f"[+] Processed {filename} => ID: {id_num}")

        except Exception as e:
            print(f"[⚠️] Skipping file {image_path}: {e}")

    if not faces:
        print("[❌] No faces found for training. Please check image data.")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))

    if not os.path.exists("TrainingImageLabel"):
        os.makedirs("TrainingImageLabel")

    recognizer.save("TrainingImageLabel/trainner.yml")
    print("[✅] Training complete. Model saved as trainner.yml")

train_classifier()
