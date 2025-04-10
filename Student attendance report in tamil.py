import tkinter as tk
from tkinter import messagebox
import datetime
import csv

class AttendanceSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student info
        self.attendance = {}  # Dictionary to store today's attendance
        self.date = datetime.date.today().strftime("%Y-%m-%d")
        self.root = tk.Tk()
        self.root.title("Tamil School Attendance System")

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()

        # Create labels and entries
        self.label1 = tk.Label(self.frame1, text="Student ID:")
        self.label1.pack(side=tk.LEFT)
        self.entry1 = tk.Entry(self.frame1)
        self.entry1.pack(side=tk.LEFT)

        self.label2 = tk.Label(self.frame1, text="Student Name:")
        self.label2.pack(side=tk.LEFT)
        self.entry2 = tk.Entry(self.frame1)
        self.entry2.pack(side=tk.LEFT)

        # Create buttons
        self.button1 = tk.Button(self.frame2, text="Add Student", command=self.add_student)
        self.button1.pack(side=tk.LEFT)
        self.button2 = tk.Button(self.frame2, text="Remove Student", command=self.remove_student)
        self.button2.pack(side=tk.LEFT)
        self.button3 = tk.Button(self.frame2, text="Mark Attendance", command=self.mark_attendance)
        self.button3.pack(side=tk.LEFT)
        self.button4 = tk.Button(self.frame2, text="View All Students", command=self.view_students)
        self.button4.pack(side=tk.LEFT)
        self.button5 = tk.Button(self.frame2, text="Generate Daily Report", command=self.generate_daily_report)
        self.button5.pack(side=tk.LEFT)
        self.button6 = tk.Button(self.frame2, text="Exit", command=self.root.destroy)
        self.button6.pack(side=tk.LEFT)

        # Create text box
        self.text_box = tk.Text(self.frame3)
        self.text_box.pack()

    def add_student(self):
        student_id = self.entry1.get()
        name = self.entry2.get()
        if student_id not in self.students:
            self.students[student_id] = name
            self.text_box.insert(tk.END, f"Student {name} (ID: {student_id}) added successfully!\n")
        else:
            self.text_box.insert(tk.END, "Student ID already exists!\n")

    def remove_student(self):
        student_id = self.entry1.get()
        if student_id in self.students:
            del self.students[student_id]
            self.text_box.insert(tk.END, f"Student ID {student_id} removed successfully!\n")
        else:
            self.text_box.insert(tk.END, "Student ID not found!\n")

    def mark_attendance(self):
        student_id = self.entry1.get()
        status = self.entry2.get().upper()
        if student_id in self.students:
            self.attendance[student_id] = status
            self.text_box.insert(tk.END, f"Attendance marked for {self.students[student_id]}: {status}\n")
        else:
            self.text_box.insert(tk.END, "Student ID not found!\n")

    def view_students(self):
        self.text_box.delete(1.0, tk.END)
        if not self.students:
            self.text_box.insert(tk.END, "No students registered yet!\n")
        else:
            self.text_box.insert(tk.END, "\nRegistered Students:\n")
            for id, name in self.students.items():
                self.text_box.insert(tk.END, f"ID: {id} - Name: {name}\n")

    # def generate_daily_report(self):
    #     filename = f"Attendance_{self.date}.txt"
    #     with open(filename, 'w', encoding='utf-8') as file:
    #         file.write(f"Attendance Report - {self.date}\n")
    #         file.write("====================\n")
    #         file.write("மாணவர் வருகைப் பதிவு\n\n")

    #         present_count = 0
    #         absent_count = 0
            
    #         for student_id, name in self.students.items():
    #             status = self.attendance.get(student_id, "Not Marked")
    #             tamil_status = "நிகழ்காலம்" if status == "P" else "இல்லை" if status == "A" else "குறிக்கப்படவில்லை"
    #             file.write(f"ID: {student_id} - பெயர்: {name} - நிலை: {tamil_status}\n")
                
    #             if status == "P":
    #                 present_count += 1
    #             elif status == "A":
    #                 absent_count += 1

    #         file.write("\nமொத்தம்:\n")
    #         file.write(f"நிகழ்கால மாணவர்கள்: {present_count}\n")
    #         file.write(f"இல்லாத மாணவர்கள்: {absent_count}\n")
    #         file.write(f"மொத்த மாணவர்கள்: {len(self.students)}\n")

            
    #    # Read the file contents
    #     with open(filename, 'r') as file:
    #       contents = file.read()
 
    # # Display the contents in the GUI
    #     self.text_box.delete(1.0, tk.END)
    #     self.text_box.insert(tk.END, contents)


    def generate_daily_report(self):
        filename = f"Attendance_{self.date}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"Attendance Report - {self.date}\n")
            file.write("====================\n")
            file.write("மாணவர் வருகைப் பதிவு\n\n")
            present_count = 0
            absent_count = 0
            for student_id, name in self.students.items():
                status = self.attendance.get(student_id, "Not Marked")
                tamil_status = "நிகழ்காலம்" if status == "P" else "இல்லை" if status == "A" else "குறிக்கப்படவில்லை"
                file.write(f"ID: {student_id} - பெயர்: {name} - நிலை: {tamil_status}\n")
                if status == "P":
                    present_count += 1
                elif status == "A":
                    absent_count += 1
            file.write("\nமொத்தம்:\n")
            file.write(f"நிகழ்கால மாணவர்கள்: {present_count}\n")
            file.write(f"இல்லாத மாணவர்கள்: {absent_count}\n")
            file.write(f"மொத்த மாணவர்கள்: {len(self.students)}\n")

    # Read the file contents
        with open(filename, 'r', encoding='utf-8') as read_file:
            contents = read_file.read()

    # Display the contents in the GUI
        self.text_box.delete(1.0, tk.END)
        self.text_box.insert(tk.END, contents)

        

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    attendance_system = AttendanceSystem()
    attendance_system.run()