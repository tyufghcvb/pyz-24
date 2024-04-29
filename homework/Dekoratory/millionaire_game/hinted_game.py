import json

from game import Game
import datetime


class HintGame(Game):
    hints_allowed = 3

    def __init__(self, questions, question_value):
        super().__init__(questions, question_value)

    def request_hint(self, current_question):
        if self.hints_allowed > 0:
            print(f"Hint: The answer starts with {current_question.correct_answer[0]}")
            self.hints_allowed -= 1
        else:
            print("No hints left!")

    @classmethod
    def set_hints_number(cls, number):
        cls.hints_allowed = number

    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return 'We play!'
        return 'Sorry no!'

    #
    # @property
    # def get_score(self):
    #     # ... punkty property
    #     return f'Player score in total: {self.score}'
    #
    # @property
    # def get_remaining_questions(self, ):
    #     # ... punkty property
    #     return f'Player score in total: {self.score}'

    # Zadanie 2. Dekorator @ property.Do HintedGame dodaj właściwość score i remaining_questions
    @property
    def get_remaining_hints(self):
        # ... hints property
        return f'Player hints: {self.hints_allowed}'

    # @property def get_score(self): can overwrite property parents class behaviour, after chaning in values for question_value
    #
    @property
    def score(self):
        return self._score

    @property
    def remaining_questions(self):
        # remaining_questions property
        # print(f"current_question_index: {self._current_question_index} ")
        # remaining_questions = 10 - (self._current_question_index)
        remaining_questions = max(10 - self._current_question_index, 0)
        # Version for game with no defined value for each question
        # remaining_questions = len(self.questions) - self._current_question_index
        return remaining_questions

    def save_game(self, filename='game_save.json'):
        self.game_state = {
            "game_type": "with hints",
            "last_question_index": self._current_question_index - 1,
            "current_score": self.get_score(),
            "hints_allowed": self.hints_allowed,
            "time_remaining": 0
        }

        with open(filename, 'w') as file:
            json.dump(self.game_state, file, indent=4)


def main():
    from question import Question
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris", difficulty='easy'),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4", difficulty='easy'),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare",
                 difficulty='easy'),
    ]

    # Zadanie 2.
    game = HintGame(question_list)

    print(f'Property get_remaining_hints {game.get_remaining_hints}')
    HintGame.set_hints_number(5)
    print(f'Property get_remaining_hints {game.get_remaining_hints}')
    print(f'Property get_remaining_questions {game.get_remaining_questions}')

    # game1 = HintGame(question_list)
    # game2 = HintGame(question_list)
    #
    #
    # print(game1.hints_allowed)
    # print(game2.hints_allowed)
    # HintGame.set_hints_number(5)
    #
    # print(game1.hints_allowed)
    # print(game2.hints_allowed)
    #
    # today = datetime.date.today()
    # print(HintGame.is_weekend(today))


if __name__ == '__main__':
    main()
