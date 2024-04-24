from game import Game

class TimedGame(Game):
    def __init__(self, questions, time_limit):
        super().__init__(questions)
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

    def __str__(self):
        return f'Time--> {self.time_limit}'



def main():
    from question import Question
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris", difficulty='easy'),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4",  difficulty='easy'),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare", difficulty='easy'),
    ]

    game = TimedGame(question_list, 10)
    print(game)


if __name__ == '__main__':
    main()