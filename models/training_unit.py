class TrainingUnit:
    def __init__(self, id, description, camp_id, camp_name, training_number, training_type, date=None):
        self.id = id
        self.description = description
        self.training_type = training_type
        self.camp_id = camp_id
        self.camp_name = camp_name
        self.training_number = training_number
        self.date = date
        self.exercises = []
