class Game:
    def __init__(self, questions):
        self.questions = questions
        self._current_question_index = 0
        self._score = 0

    def __str__(self):
        return f"Current score: {self._score}"

    def __len__(self):
        return len(self.questions)

    def __getitem__(self, index):
        if index < len(self.questions):
            return self.questions[index]
        else:
            None

    def __setitem__(self, index, question):
        if index < len(self.questions):
            self.questions[index] = question
        else:
            raise IndexError

    def get_next_question(self):
        if self._current_question_index < len(self.questions):
            question = self.questions[self._current_question_index]
            self._current_question_index += 1
            return question
        else:
            return None

    def submit_answer(self, answer):
        current_question = self.questions[self._current_question_index - 1]
        if current_question.check_answer(answer):
            self._score += 100
            return True
        else:
            return False

    def get_score(self):
        return f'{self._score} PLN'


# from question import Question
#
# question_list = [
#     Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
#     Question("What is 2 + 2?", ["3", "4", "2", "5"], "4"),
#     Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
# ]
# testgame = Game(question_list)
#
# new_question = ("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
#
# print(len(testgame))
#
# print(testgame[1])
#
# testgame[0] = Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
#
# print(testgame[0])
