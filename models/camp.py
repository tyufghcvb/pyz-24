class Camp:
    def __init__(self, id, name, description, training_units, start_date=None, end_date=None):
        self.id = id
        self.name = name
        self.description = description
        self.training_units = training_units
        self.start_date = start_date
        self.end_date = end_date
