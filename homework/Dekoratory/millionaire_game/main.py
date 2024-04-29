from game import Game
from hinted_game import HintGame
from fileloader import load_questions_from_file
from timed_game import TimedGame




def play_game(game):
    print("Welcome to the Millionaire Game!\n")
    while True:
        question = game.get_next_question()

       # list question_value in __init__:
        if not question or (game.get_score() == max(game.question_value)):
            print("Congratulations! You've completed the game.")
            break
        print(question)
        game.is_to_save()

        if isinstance(game, HintGame):
            while True:
                resp = input('Do you need a hint? Y/N').upper()
                if resp == 'Y':
                    game.request_hint(question)
                    break
                elif resp == 'N':
                    break
                else:
                    print('No such option; Try again!')

        answer = int(input("Please enter the number of your answer: "))
        #answer = Game.correct_range_answer()

        if Game.is_valid(answer, question.options) and game.submit_answer(question.options[int(answer) - 1]):
            print("The correct answer --> ", question.correct_answer)
            print(f"Current score: {game.get_score()} PLN")
        else:
            break
    print(f"Your final score is: {game.get_score()} PLN")


def main():
    question_list = load_questions_from_file('questions.json')
    question_value = [100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 1000000]

    while True:
        quests = """What kind of game you wanna play
         1 - normal
         2 - with hints 
         3 - timed
          Select -> """

        selected_game = input(quests)
        if selected_game == '1':
            game_instance = Game(question_list, question_value)
            #game_instance = Game.fromjson(question_value, 'questions.json')
            break
        elif selected_game == '2':
            game_instance = HintGame(question_list, question_value)
            break
        elif selected_game == '3':
            game_instance = TimedGame(question_list, question_value, 20)
            break
        else:
            print('No such option, please try again')

    play_game(game_instance)

if __name__ == "__main__":
    main()