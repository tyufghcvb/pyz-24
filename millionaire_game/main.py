from game import Game
from question import Question
from hint_game import HintGame
from timed_game import TimedGame
import random


def display_menu():
    print("\nPlease choose your level of wealthiness, or, perhaps, your level of greediness:\n")
    print("1. Modest - a friend of mice and master of little hints.")
    print("2. Comfortable - no need for help, no pressure, just cruising.")
    print("3. Extremely wealthy - you can play hard, as time will let you!")


def play_game(game, give_hint, time_countdown):
    while True:
        question = game.get_next_question()

        if not question:
            print("Congratulations! You've completed the game.")
            break
        print(question)
        if give_hint:
            game.request_hint(question)
        answer = input("Please enter the number of your answer: ")
        if game.submit_answer(question.options[int(answer) - 1]):
            print("Correct!\n")
        else:
            print("Wrong! The correct answer was:", question.correct_answer)
            break
        if time_countdown:
            game.show_remaining_time()

    print(f"Your final score is: {game.get_score()}")


def main():
    question_list = [
        Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
        Question("What is 2 + 2?", ["3", "4", "2", "5"], "4"),
        Question("Who wrote 'Macbeth'?", ["Shakespeare", "Austen", "Joyce", "Hemingway"], "Shakespeare")
    ]
    random.shuffle(question_list)

    display_menu()

    #   game_instance = None
    give_hint = False
    time_countdown = False

    while True:
        choice = input("\n The number of your answer: ")
        if choice == '1':
            game_instance = HintGame(question_list, 2)
            give_hint = True
            break
        elif choice == '2':
            game_instance = Game(question_list)
            break
        elif choice == '3':
            game_instance = TimedGame(question_list, 20)
            time_countdown = True
            break
        else:
            print("Invalid input, please try again.")
    play_game(game_instance, give_hint, time_countdown)


if __name__ == "__main__":
    main()
