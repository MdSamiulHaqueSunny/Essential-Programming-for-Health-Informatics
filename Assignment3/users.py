import csv
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def can_access_patient_info(self):
        return self.role in ['clinician', 'nurse']

    def can_add_patient(self):
        return self.role in ['clinician', 'nurse']

    def can_remove_patient(self):
        return self.role in ['clinician', 'nurse']

    def can_retrieve_patient(self):
        return self.role in ['clinician', 'nurse']

    def can_count_visits(self):
        return self.role != 'management'

    def can_generate_statistics(self):
        return self.role == 'management'
    
def authenticate_user(credentials_file):
    username_input = input("Enter username: ").strip()
    password_input = input("Enter password: ").strip()

    with open(credentials_file, mode='r') as csvfile:
        # We're not defining fieldnames yet because we want to print the entire row as is.
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row.
        
        for row in reader:
            # Check if any of the fields in the row match the input credentials.
            for field in row:
                if field.strip() == username_input:
                    # Assuming the password is in the next column.
                    password_index = row.index(field) + 1
                    if row[password_index].strip() == password_input:
                        # We found the user, assuming the role is in the next column.
                        role_index = password_index + 1
                        return User(field.strip(), row[role_index].strip())
    return None