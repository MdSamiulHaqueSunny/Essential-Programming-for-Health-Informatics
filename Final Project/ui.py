import tkinter as tk
from tkinter import messagebox, simpledialog
from users import authenticate_user
from hospitals import Hospital

class HospitalUI:
    def __init__(self, root, hospital, credentials_path):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("400x400")
        self.hospital = hospital
        self.credentials_path = credentials_path
        self.setup_login_frame()

    def setup_login_frame(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        tk.Label(self.login_frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        tk.Label(self.login_frame, text="Password:").pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        tk.Button(self.login_frame, text="Login", command=self.validate_login).pack()

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.user = authenticate_user(self.credentials_path, username, password)
        if self.user:
            messagebox.showinfo("Login Successful", f"Welcome {self.user.username}!")
            self.login_frame.pack_forget()
            self.setup_main_menu(self.user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    def setup_main_menu(self, user):
        self.main_menu_frame = tk.Frame(self.root)
        self.main_menu_frame.pack()
        if self.user.role in ['admin', 'management']:
            actions = ["Generate Key Statistics", "Exit"]
        else:
            actions = ["Retrieve Patient", "Add Patient", "Remove Patient", "Count Visits", "Exit"]
        # actions = ["Retrieve Patient", "Add Patient", "Remove Patient", "Count Visits", "Generate Key Statistics", "Exit"] if self.user.can_generate_statistics() else ["Retrieve Patient", "Add Patient", "Remove Patient", "Count Visits", "Exit"]

        for action in actions:
            button = tk.Button(self.main_menu_frame, text=action, command=lambda act=action: self.handle_action(act))
            button.pack()

    def handle_action(self, action):
        if action == "Exit":
            self.root.quit()
        elif action == "Retrieve Patient":
            self.retrieve_patient()
        elif action == "Add Patient":
            self.add_patient()
        elif action == "Remove Patient":
            self.remove_patient()
        elif action == "Count Visits":
            self.count_visits()
        elif action == "Generate Key Statistics":
            self.generate_statistics()

    def retrieve_patient(self):
        patient_id = simpledialog.askstring("Retrieve Patient", "Enter Patient ID:")
        if patient_id:
            patient_info = self.hospital.retrieve_patient(patient_id)
            messagebox.showinfo("Patient Information", patient_info)

    def add_patient(self):
        patient_id = simpledialog.askstring("Add Patient", "Enter Patient ID:")
        if patient_id:
            self.hospital.add_patient(patient_id)
            messagebox.showinfo("Add Patient", "Patient added successfully.")

    def remove_patient(self):
        patient_id = simpledialog.askstring("Remove Patient", "Enter Patient ID:")
        if patient_id:
            self.hospital.remove_patient(patient_id)
            messagebox.showinfo("Remove Patient", "Patient removed successfully.")

    def count_visits(self):
        date = simpledialog.askstring("Count Visits", "Enter Date (YYYY-MM-DD):")
        if date:
            count = self.hospital.count_visits(date)
            messagebox.showinfo("Count Visits", f"Total visits on {date}: {count}")

    def generate_statistics(self):
        stats = self.hospital.generate_statistics()
        messagebox.showinfo("Statistics", stats)

# To run the UI:
if __name__ == "__main__":
    root = tk.Tk()
    hospital = Hospital()  # Assuming Hospital class handles initialization of hospital details
    app = HospitalUI(root, hospital, 'credentials.csv')
    root.mainloop()
