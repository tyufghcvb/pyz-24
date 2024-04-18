from game import Game


class HintGame(Game):
    def __init__(self, questions, hints_allowed):
        super().__init__(questions)
        self.hints_allowed = hints_allowed

    def request_hint(self, current_question):
        # Sprawdzaczy uztkownik ma prawo do podpowiedzi
        # Jeśli tak uzytkownik otrzymuje podpowiedz np. "Hint: The answer starts with letter: {first letter}"
        # W przeciwnym wypadku wyświetl komunikat informujacy ze uzytkownik wykorzytal wszystkie podpowiedzi
        if self.hints_allowed > 0:
            self.hints_allowed -= 1
            hint = current_question.correct_answer
            print(f"Hint: The answer starts with letter: \"{hint[0]}\"")
        else:
            print(f"No more hints available on this cruel World")

