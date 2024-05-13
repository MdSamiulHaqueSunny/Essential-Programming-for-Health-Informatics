class Visit:
    def __init__(self, visit_id, visit_time, visit_department, gender, race, age, ethnicity, insurance, zip_code, chief_complaint, note=None):
        # Constructor: Initializes a new Visit object with detailed information about the visit.
        self.visit_id = visit_id  
        self.visit_time = visit_time  
        self.visit_department = visit_department  
        self.gender = gender  
        self.race = race  
        self.age = age  
        self.ethnicity = ethnicity  
        self.insurance = insurance 
        self.zip_code = zip_code  
        self.chief_complaint = chief_complaint  
        self.note = note  
    
    def update_visit_info(self, **kwargs):
        # Allows updating the visit's information with any number of attributes via keyword arguments.
        for key, value in kwargs.items():  # Iterates over provided keyword arguments.
            if hasattr(self, key):  # Checks if the visit object has the attribute named `key`.
                setattr(self, key, value)  # Updates the attribute `key` to the new value `value`.
    
    def get_visit_details(self):
        # Returns a dictionary of all visit details, including the note if present.
        details = self.__dict__.copy()  # Creates a copy of the visit's attribute dictionary.
        if self.note:
            # If a note is associated with the visit, add its details to the dictionary.
            details["Note"] = self.note.get_note_info()
        return details  # Returns the dictionary with visit details.