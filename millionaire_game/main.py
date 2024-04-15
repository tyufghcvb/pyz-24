from game import Game
from question import Question
import random

def play_game(game):
    print("Welcome to the Millionaire Game!\n")
    while True:
        question = game.get_next_question()
        if not question:
            print("Congratulations! You've completed the game.")
            break
        print(question)
        answer = input("Please enter the number of your answer: ")
        if game.submit_answer(question.options[int(answer) - 1]):
            print("Correct!\n")
        else:
            print("Wrong! The correct answer was:", question.correct_answer)
            break
    print(f"Your final score is: {game.get_score()}")


def main():
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4"),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
    ]
    random.shuffle(question_list)
    game_instance = Game(question_list)
    play_game(game_instance)

if __name__ == "__main__":
    main()