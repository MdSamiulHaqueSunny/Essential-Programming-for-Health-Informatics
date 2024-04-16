class Note:
    def __init__(self, note_id, note_type):
        # Constructor: Initializes a new Note object with a unique note ID and the type of note.
        self.note_id = note_id  
        self.note_type = note_type  
    
    def get_note_info(self):
        # Returns a dictionary containing the note's ID and type.
        # This method provides a structured way to access basic information about the note.
        return {
            "Note ID": self.note_id,
            "Note Type": self.note_type
        }