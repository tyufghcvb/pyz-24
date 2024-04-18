from game import Game


class TimedGame(Game):

    def __init__(self, questions, time_limit):
        super().__init__(questions)
        self.remaining_time = time_limit

    def decrease_remaining_time(self):
        self.remaining_time -= 5

    def show_remaining_time(self):
        print(f"Remaining_time: {self.remaining_time}")

    def submit_answer(self, answer):
        # Specjalna logika dla gry z czasem
        # Przy poprawnej odpowiedzi wyświetla Remaining time
        # Przy błędnej odpowiedzi odejmuje czas jako karę i wyświetla Remaining time
        current_question = self.questions[self._current_question_index - 1]
        if current_question.check_answer(answer):
            self._score += 100
            self.show_remaining_time()
            return True
        else:
            self.decrease_remaining_time()
            self.show_remaining_time()
            return False
