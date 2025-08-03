import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Main GUI window
root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Title Label
tk.Label(root, text="Attendance System", font=("Helvetica", 20, "bold"), fg="#2d2d2d", bg="#f0f0f0").pack(pady=20)

# Button Actions
def take_images():
    subprocess.run(["python", "takeImage.py"])

def train_model():
    subprocess.run(["python", "trainImage.py"])
    messagebox.showinfo("Training", "Training Completed Successfully!")

def mark_attendance():
    subprocess.run(["python", "automaticAttedance.py"])
    messagebox.showinfo("Attendance", "Attendance Marked (Check CSV File)")

def open_attendance_folder():
    attendance_path = os.path.abspath("Attendance")
    os.startfile(attendance_path)

# Buttons
tk.Button(root, text="📸 Take Images", width=25, height=2, bg="#4285f4", fg="white", command=take_images).pack(pady=10)
tk.Button(root, text="🧠 Train Model", width=25, height=2, bg="#34a853", fg="white", command=train_model).pack(pady=10)
tk.Button(root, text="✅ Mark Attendance", width=25, height=2, bg="#fbbc05", fg="black", command=mark_attendance).pack(pady=10)
tk.Button(root, text="📁 View Attendance CSV", width=25, height=2, bg="#9c27b0", fg="white", command=open_attendance_folder).pack(pady=10)

# Exit button
tk.Button(root, text="❌ Exit", width=10, bg="#d32f2f", fg="white", command=root.quit).pack(pady=20)

root.mainloop()
