from models.training_unit import TrainingUnit


class TrainingManager:
    def __init__(self):
        self.trainings = []
        self.next_id = 1

    def add_trainig(self, id, description, camp_id, camp_name, training_type, date=None):
        new_training = TrainingUnit(self.next_id, description, camp_id, date)
        self.trainings.append(new_training)
        self.next_id += 1

    def update_training_unit(self, id, description, camp_id, camp_name, training_type, date=None):
        training = self.get_training_unit(id)
        if training:
            training.description = description
            training.date = date

    def get_training_unit(self, id: int):
        for trn in self.trainings:
            if trn.id == id:
                return trn

    def delete(self, id: int):
        exp = self.get_expense(id)
        if exp != None:
            self.expenses.remove(exp)
