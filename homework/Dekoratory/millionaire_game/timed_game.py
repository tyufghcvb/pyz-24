import json

from game import Game
import time


class TimedGame(Game):
    def __init__(self, questions, question_value, time_limit):
        super().__init__(questions, question_value)
        self.time_limit = time_limit

    def submit_answer(self, answer):
        if super().submit_answer(answer):
            print(f"Correct! Remaining time: {self.time_limit}")
            return True
        elif self.time_limit > 0:
            self.time_limit -= 10
            print(f"Wrong! Time penalty applied. Remaining time: {self.time_limit}")
            return True
        else:
            print(f"Wrong! No more time left!")
            return False

    @property
    def best_time(self):
        # ... mechanizm teorytyczny odmierzania czasu
        return f'Player best time: {self.time_limit}'

    def __str__(self):
        return f'time--> {self.time_limit}'


    @property
    def get_remaining_time(self):
        # ... punkty property
        return f'Player score in total: {self.time_limit}'

    def save_game(self, filename='game_save.json'):
        self.game_state = {
            "game_type": "timed",
            "last_question_index": self._current_question_index - 1,
            "current_score": self.get_score(),
            "hints_allowed": 0,
            "time_remaining": self.time_limit
        }

        with open(filename, 'w') as file:
            json.dump(self.game_state, file, indent=4)



# def main():
#     from question import Question
#     question_list = [
#         Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris", difficulty='easy'),
#         Question("What is 2 + 2?", ["3", "4", "2", "5"], "4",  difficulty='easy'),
#         Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare", difficulty='easy'),
#     ]
#
#     game = TimedGame(question_list, 10)
#     print(game)
#     print(game.best_time)
#     game.time_limit = 100
#     print(game)
#     print(game.best_time)
    #

    # def uppercase_decorator(func_in):
    #     def nested(a):
    #         txt = func_in(a)
    #         return txt.upper()
    #
    #     return nested
    #
    # @uppercase_decorator
    # def quot(a):
    #     return a
    #
    # print(quot("jajajjaa"))

    # def time_counter(func_in):
    #     def nested(a, b, c):
    #         time_start = time.time()
    #         result = func_in(a, b, c)
    #         time_end = time.time()
    #         duration = time_end - time_start
    #         print(f"Function executed in {duration} seconds")
    #         return result
    #     return nested
    #
    # @time_counter
    # def func(a, b, c):
    #     pow_abc=a**b**c
    #     print("Sleeping")
    #     time.sleep(5)
    #     return pow_abc
    #
    # print(func(2, 3, 4))

# if __name__ == '__main__':
#     main()
