from question import Question
import json


def check_answer_correct(question, answer):
    return question.correct_answer == answer


class Game:
    def __init__(self, questions, question_value):
        self.questions = questions
        self.question_value = question_value
        self._current_question_index = 0
        self._score = 0
        self.check = check_answer_correct
        self.answer_log = []
        self.game_state = {}

    # Zadanie 3.
    @classmethod
    def fromjson(cls, question_value, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        questions = []
        for item in data:
            question = Question(
                item['question'],
                item['options'],
                item['correct_answer'],
                item['difficulty']
            )
            questions.append(question)
        return cls(questions, question_value)

    def __str__(self):
        return f"Current score: {self._score}"

    def __len__(self):
        return len(self.questions)

    def __getitem__(self, index):
        # return self.questions[index] if index < len(self.questions) else None
        if index < len(self.questions):
            return self.questions[index]
        else:
            None

    def __setitem__(self, index, value):
        if index < len(self.questions):
            self.questions[index] = value
        else:
            raise IndexError

    def get_next_question(self):
        if self._current_question_index < len(self.questions):
            question = self.questions[self._current_question_index]
            self._current_question_index += 1
            return question
        else:
            return None

    # Zadanie 1 log_answers
    def log_answers(func_submit_answer):
        def nested(self, answer):
            result = func_submit_answer(self, answer)
            score_log = self.get_score()
            log = f'Given Answer {answer}, current scores {score_log} PLN'
            self.answer_log.append(log)
            # print(f"Logged: {self.answer_log} ")
            return result

        return nested

    @log_answers
    def submit_answer(self, answer):
        current_question = self.questions[self._current_question_index - 1]
        if self.check(current_question, answer):
            # Zadanie 6. Previous self._score += 100, now hierarchy question_value increased like in original game
            self._score = self.question_value[self._current_question_index - 1]
            # print(f"indeks {self._current_question_index - 1}")
            return True
        else:
            return False

    def get_score(self):
        return self._score

    # @property
    # def get_score(self):
    #     # ... punkty property
    #     return f'Player score in total: {self._score}'

    def is_to_save(self):
        save = input("Please pres s and enter to save game: ")
        if save == 's':
            self.save_game()

    # Zadanie 4.
    @staticmethod
    def correct_range_answer():
        answer = input("Please enter a valid number of your answer: ")
        while not answer.isdigit() or int(answer) not in range(1, 5):
            answer = input("Please enter a valid number of your answer in range 1-4: ")
        return int(answer)

    def save_game(self, filename='game_save.json'):
        self.game_state = {
            "game_type": "with hints",
            "last_question_index": self._current_question_index - 1,
            "current_score": self.get_score(),
            "hints_allowed": 0,
            "time_remaining": 0
        }

        with open(filename, 'w') as file:
            json.dump(self.game_state, file, indent=4)

# def main():
#     from question import Question
#     question_list = [
#         Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris", "easy"),
#         Question("What is 2 + 2?", ["3", "4", "2", "5"], "4", "easy"),
#         Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare", "easy"),
#         Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare", "easy")
#     ]
#     question_value = [100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 1000000]
#
#     # game = Game(question_list, question_value)
#     # print(len(game))
#     # print(game[0])
#     # game[0] = Question("What is 5 + 2?", ["3", "7", "2", "5"], "7", "easy")
#     # print(game[0])
#
#     # Constructor from json
#
#     # game = Game('questions.json', question_value)
#     # print(game.get_score())
#     # print(len(game))
#     # print(game[0])
#
#
# if __name__ == '__main__':
#     main()
