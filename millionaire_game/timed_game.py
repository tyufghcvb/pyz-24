# TODO

class TimedGame(game):
    # time_limit = 10
    # def __init__(self, questions):
    #     super().__init__(questions)

    def __init__(self, questions, time_limit):
    # time_limit = 10
    # def __init__(self, questions):
    #     super().__init__(questions)

    def submit_answer(self, answer):
        # Specjalna logika dla gry z czasem
        # Przy poprawnej odpowiedzi wyświetla Remaining time
        # Przy błędnej odpowiedzi odejmuje czas jako karę i wyświetla Remaining time
        current_question = self.questions[self._current_question_index - 1]
        if current_question.check_answer(answer):
            self._score += 100
            return True
        else:
            return False
        pass
