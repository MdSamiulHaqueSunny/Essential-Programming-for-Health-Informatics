import uuid
from patients import Patient
from visits import Visit
from notes import Note

class Hospital:
    def __init__(self):
        # Constructor: Initializes a new Hospital object with an empty dictionary to store patients.
        self.patients = {}  # A dictionary to store Patient objects, with patient IDs as keys.
    def add_patient(self, patient_id):
        # Adds a new Patient object to the hospital's patient dictionary if the patient ID is not already present.
        # Also prompts the user for visit_time and generates a unique visit_ID.
        if patient_id not in self.patients:
        # Prompt for visit time
            visit_time = input("Enter Visit Time (YYYY-MM-DD HH:MM): ").strip()
        # Generate a unique visit_id using uuid
            visit_id = str(uuid.uuid4())
        # Create a new Patient object and a new Visit object with the generated visit_id and prompted visit_time
            new_patient = Patient(patient_id)
            new_visit = Visit(visit_id, visit_time, visit_department=None, gender=None, 
                          race=None, age=None, ethnicity=None, insurance=None, 
                          zip_code=None, chief_complaint=None, note=None)
        # Add the visit to the patient's visits
            new_patient.add_visit(new_visit)
        # Store the new Patient object in the hospital's dictionary
            self.patients[patient_id] = new_patient
            print(f"New patient with ID {patient_id} added with visit ID {visit_id} at {visit_time}.")
        else:
        # If patient already exists, prompt for visit time and create a new visit_id
            visit_time = input("Enter Visit Time (YYYY-MM-DD HH:MM): ").strip()
            visit_id = str(uuid.uuid4())
        
        # Since the patient already exists, retrieve the patient object
            existing_patient = self.patients[patient_id]
        
        # Create a new Visit object and add it to the existing patient's visits
            new_visit = Visit(visit_id, visit_time, visit_department=None, gender=None, 
                          race=None, age=None, ethnicity=None, insurance=None, 
                          zip_code=None, chief_complaint=None, note=None)
            existing_patient.add_visit(new_visit)
            print(f"Added new visit for existing patient with ID {patient_id} and visit ID {visit_id} at {visit_time}.")        
    def remove_patient(self, patient_id):
        # Removes a Patient object from the hospital's patient dictionary based on the patient ID.
        # Outputs a message indicating whether the patient was removed or if the patient ID does not exist.
        if patient_id in self.patients:
            del self.patients[patient_id]  # Removes the Patient object from the dictionary.
            print(f"Patient with ID {patient_id} has been removed.")
        else:
            print("Patient ID does not exist.")
    def retrieve_patient(self, patient_id):
        # Retrieves and prints information about a specific patient based on the patient ID.
        # Outputs patient information or a message if the patient ID does not exist.
        if patient_id in self.patients:
            patient_info = self.patients[patient_id].get_patient_info()  # Retrieves patient information.
            print("Patient Information:", patient_info)
        else:
            print("Patient ID does not exist.")
    def count_visits(self, date):
        # Counts and prints the number of visits to the hospital on a specific date.
        count = sum(1 for patient in self.patients.values() for visit in patient.visits if visit.visit_time == date)
        print(f"Total visits on {date}: {count}")
    
    def load_patients_from_file(self, file_path):
        # Loads patient and visit information from a specified file path.
        # This method reads the file, skipping malformed lines, and updates the hospital's patient dictionary.
        with open(file_path, 'r') as file:
            next(file)  # Skips the header line.
            for line in file:
                parts = line.strip().split(',')[1:]  # Splits each line into parts.
                if len(parts) < 13:  # Checks for malformed lines.
                    print(f"Skipping malformed line: {line}")
                    continue  # Skips to the next line if malformed.

                # Unpacks parts into variables for easier readability and manipulation.
                patient_id, visit_id, visit_time, visit_department, race, gender, ethnicity, age, zip_code, insurance, chief_complaint, note_id, note_type = parts
         
                note = Note(note_id, note_type)  # Creates a Note object.
                visit_age = age  # Specific variable for age to enhance readability.
          
                # Creates a Visit object with the unpacked variables.
                visit = Visit(visit_id, visit_time, visit_department, gender, race, visit_age,
                        ethnicity, insurance, zip_code, chief_complaint, note)
                      
                # Adds or updates the patient in the hospital's patient dictionary.
                if patient_id not in self.patients:
                    self.patients[patient_id] = Patient(patient_id)
                else:
                    print(f"Updating patient: {patient_id}")
                
                # Adds the visit to the patient's record.
                self.patients[patient_id].add_visit(visit)
    def generate_statistics(self):
        # Count the number of visits per department
        stats = {}
        for patient in self.patients.values():
            for visit in patient.visits:
                department = visit.visit_department
                stats[department] = stats.get(department, 0) + 1
        return stats
        for department, count in stats.items():
            print(f"{department}: {count} visits") # Print the statistics or save them to a file
            
