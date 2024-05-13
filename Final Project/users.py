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
    
def authenticate_user(credentials_path, username, password):
    with open(credentials_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                # Assuming the role is also stored in the same row
                return User(username, row['role'])
    return None
