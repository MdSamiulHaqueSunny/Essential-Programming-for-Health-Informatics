#Course: HI 741
#Instructor: Dr. Lu He
#Assignment_3
#Submitted by: Md Samiul Haque Sunny
#Resoures Used: Assignment Instructions, Class Lectures, Python Documentation on built-in Data types, Anaconda(Jupiter Notebook) for cell by cell debugging, Chat GPT for clarificaiton
import sys
from hospitals import Hospital, generate_statistics
from users import authenticate_user


def main(credentials_file, input_path):
        # Initializes the main function for the Hospital Management System.
    hospital = Hospital()  # Creates a new Hospital object.
    hospital.load_patients_from_file(input_path)  # Loads patients from a file.
    print("Welcome to the Hospital Management System")
    user = authenticate_user(credentials_file)
    if user is None:
        print("Invalid credentials. Access denied.")
        return
    print(f"Welcome {user.username}! You have {user.role} access.")
    if user.can_generate_statistics():
                while True:
                    command = input("Enter command (visits_by_department)(Enter 'Stop' to exit): ").strip().lower()
                    if command == "stop":
                        print("Exiting the system.")  # Exits the loop and ends the program.
                        break
                    elif command == "visits_by_department":
                        print("Generating statistics...")
                        generate_statistics(hospital.patients)
    else:
        while True:
            # Continuously prompts the user for commands until 'Stop' is entered.
            command = input("Enter command (add_patient, remove_patient, retrieve_patient, count_visits)(Enter 'Stop' to exit): ").strip().lower()
            if command == "stop":
                print("Exiting the system.")  # Exits the loop and ends the program.
                break
            elif command == "add_patient":
            # Adds a new patient to the system based on the inputted patient ID.
                patient_id = input("Enter Patient ID: ").strip()
                hospital.add_patient(patient_id)
            elif command == "remove_patient":
            # Removes a patient from the system based on the inputted patient ID.
                patient_id = input("Enter Patient ID: ").strip()
                hospital.remove_patient(patient_id)
            elif command == "retrieve_patient":
            # Retrieves and displays information for a specified patient.
                patient_id = input("Enter Patient ID: ").strip()
                hospital.retrieve_patient(patient_id)
            elif command == "count_visits":
            # Counts and displays the number of visits on a specified date.
                date = input("Enter date (yyyy-mm-dd): ").strip()
                hospital.count_visits(date)
            else:
                print("Invalid command.")  # Notifies the user of an unrecognized command.
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    credentials_path = sys.argv[1]
    patients_path = sys.argv[2]
    main(credentials_path, patients_path)
    