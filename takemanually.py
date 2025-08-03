# takemanually.py

import tkinter as tk
import tkinter.ttk as ttk
import os
import csv
import pandas as pd
from datetime import datetime
import json

window = tk.Tk()
window.geometry("800x650")
window.title("Manual Attendance Fill System")

d = {}
subs = []

def load_students():
    try:
        with open("StudentDetails/StudentDetails.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

students = load_students()

def fill_student():
    name = Name.get()
    enroll = Enr.get()

    if not name or not enroll:
        Notifi.configure(
            text="Please enter both Name and Enrollment No.",
            bg="red",
            fg="white",
            width=33,
            font=("times", 19, "bold"),
        )
        Notifi.place(x=180, y=380)
        return

    student = {"Name": name, "Enrollment": enroll}
    key = len(d)
    d[key] = student
    update_table()
    Notifi.configure(
        text="Student added successfully.",
        bg="Green",
        fg="white",
        width=33,
        font=("times", 19, "bold"),
    )
    Notifi.place(x=180, y=380)

def update_table():
    for row in tree.get_children():
        tree.delete(row)

    for key, student in d.items():
        tree.insert("", "end", values=(key+1, student["Enrollment"], student["Name"]))

def create_csv():
    # Ensure the directory exists before saving
    output_dir = "Attendance(Manually)"
    os.makedirs(output_dir, exist_ok=True)

    Date = datetime.now().strftime("%Y_%m_%d")
    Hour = datetime.now().strftime("%H")
    Minute = datetime.now().strftime("%M")
    Second = datetime.now().strftime("%S")

    subb = Subject.get() or "UnknownSubject"

    # Add current date as attendance column
    for key, value in d.items():
        d[key][Date] = 1

    df = pd.DataFrame(d).T  # Transpose to make each student a row
    csv_name = (
        os.path.join(output_dir,
        subb + "_" + Date + "_" + Hour + "-" + Minute + "-" + Second + ".csv")
    )
    df.to_csv(csv_name, index=False)
    O = "CSV created Successfully"
    Notifi.configure(
        text=O,
        bg="Green",
        fg="white",
        width=33,
        font=("times", 19, "bold"),
    )
    Notifi.place(x=180, y=380)

# UI Components

tk.Label(
    window, text="Manual Attendance Entry", font=("times", 29, "bold")
).pack(pady=20)

tk.Label(window, text="Enter Name", font=("times", 15)).place(x=50, y=100)
Name = tk.Entry(window, width=30, font=("times", 15))
Name.place(x=250, y=100)

tk.Label(window, text="Enter Enrollment", font=("times", 15)).place(x=50, y=150)
Enr = tk.Entry(window, width=30, font=("times", 15))
Enr.place(x=250, y=150)

tk.Label(window, text="Enter Subject", font=("times", 15)).place(x=50, y=200)
Subject = tk.Entry(window, width=30, font=("times", 15))
Subject.place(x=250, y=200)

tk.Button(
    window,
    text="Add Student",
    command=fill_student,
    width=20,
    font=("times", 15, "bold"),
    bg="green",
    fg="white",
).place(x=100, y=250)

tk.Button(
    window,
    text="Generate CSV",
    command=create_csv,
    width=20,
    font=("times", 15, "bold"),
    bg="blue",
    fg="white",
).place(x=400, y=250)

Notifi = tk.Label(window, text="", font=("times", 17))
Notifi.place(x=180, y=380)

tree = ttk.Treeview(window, columns=("Sl No", "Enrollment", "Name"), show="headings")
tree.heading("Sl No", text="Sl No")
tree.heading("Enrollment", text="Enrollment No")
tree.heading("Name", text="Student Name")
tree.column("Sl No", width=60)
tree.column("Enrollment", width=120)
tree.column("Name", width=200)
tree.place(x=100, y=450, width=600, height=150)

if __name__ == "__main__":
    window.mainloop()
