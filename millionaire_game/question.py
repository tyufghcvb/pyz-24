class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

    def _format_questions_and_options(self):
        #self.__format_questions_and_options = f"{self.question}\nOptions: {self.options}"
        responses=""
        for id, res in enumerate(self.options):
            responses += f'{id + 1} - {res}\n'
        return f"{self.question}\n{responses}"

    def __str__(self):
        # return f"{self.question}\nOptions: {self.options}"
        return self._format_questions_and_options()


