from game import Game
import datetime

class HintGame(Game):
    def __init__(self, questions, hints_allowed):
        super().__init__(questions)
        self.hints_allowed = hints_allowed

    def request_hint(self, current_question):
        if self.hints_allowed > 0:
            print(f"Hint: The answer starts with {current_question.correct_answer[0]}")
            self.hints_allowed -= 1
        else:
            print("No hints left!")




