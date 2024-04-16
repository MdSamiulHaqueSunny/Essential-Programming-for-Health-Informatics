class Patient:
    def __init__(self, patient_id):
        # Constructor: Initializes a new Patient object with a unique patient ID and an empty list for visits.
        self.patient_id = patient_id
        self.visits = []  # A list to store visits associated with this patient.
    
    def add_visit(self, visit):
        # Adds a new Visit object to this patient's list of visits.
        self.visits.append(visit)
    
    def remove_visit(self, visit_id):
        # Removes a visit from this patient's list of visits based on the visit ID.
        # This creates a new list excluding the visit with the specified visit_id.
        self.visits = [visit for visit in self.visits if visit.visit_id != visit_id]
    
    def get_patient_info(self):
        # Returns a dictionary containing the patient's ID and details of all their visits.
        # It uses list comprehension to call `get_visit_details` on each Visit object in the visits list.
        return {
            "Patient ID": self.patient_id,
            "Visits": [visit.get_visit_details() for visit in self.visits]
        }