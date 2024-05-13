#Course: HI 741
#Instructor: Dr. Lu He
#Final Project
#Submitted by: Md Samiul Haque Sunny
#Resoures Used: Project Instructions, Class Lectures, Python Documentation on built-in Data types, Anaconda(Jupiter Notebook) for cell by cell debugging, Chat GPT for clarificaiton
import sys
import tkinter as tk
from hospitals import Hospital
from ui import HospitalUI

def main(credentials_path, input_path):
    root = tk.Tk()
    hospital = Hospital()
    hospital.load_patients_from_file(input_path)

    app = HospitalUI(root, hospital, credentials_path)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    credentials_path = sys.argv[1]
    patients_path = sys.argv[2]
    main(credentials_path, patients_path)
