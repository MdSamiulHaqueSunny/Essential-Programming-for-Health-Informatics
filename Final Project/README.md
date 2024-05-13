

# Hospital Management System

## Project Overview
The Hospital Management System is a Python-based application designed to manage patient data for hospitals. It allows users to authenticate based on their roles and perform various functions related to patient management.

## Features
- **User Authentication**: Secure login system to authenticate users based on roles.
- **Patient Management**: Capabilities to add, update, and remove patient records.
- **Visit Tracking**: Functionality to count and track visits on specified dates.
- **Statistics Generation**: Generate key statistics for management and admin roles.
- **Role-Based Access Control**: Different functionalities are available based on the user's role.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Tkinter (usually comes with Python)

### Running the Application
Execute the following command from the root of the project directory to run the application:
```bash
python main.py Project_credentials.csv Project_patient_information.csv
```

## Usage
Upon launching the application, log in with valid credentials. Based on your role, you will be presented with various options:
- **Admin/Management**: Generate statistics and exit.
- **Nurse/Clinician**: Retrieve, add, and remove patients, count visits, and exit.

## Contributing
Contributions are welcome! If you would like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch: 
   ```bash
   git checkout -b new-feature
   ```
3. Make your changes and commit them: 
   ```bash
   git commit -am 'Add some feature'
   ```
4. Push to the branch: 
   ```bash
   git push origin new-feature
   ```
5. Submit a pull request.

---
