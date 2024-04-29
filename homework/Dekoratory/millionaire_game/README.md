# Milionaire Game

1.  Dodaj dekorator `log_answers` do naszej gry, który rejestruje każdą odpowiedź użytkownika i wynik po każdym pytaniu. 

2. `@property` 
        Dekorator `@property` jest używany do tworzenia getterów i setterów Pythona. Można go użyć do zarządzania dostępem do atrybutów klasy.
        Do `HintedGame` dodaj właściwość score i remaining_questions
3. `@classmethod`
        Dodaj metodę klasy, która będzie się zachowywać jako alternatywny konstruktor - stworzy instancję Game z wczytanego pliku JSON z pytaniami
        `game_instance = Game.from_json('questions.json')`
4.  `@staticmethod `
        Dodaj metodę walidacji odpowiedzi podanej przez użytkownika, która sprawdza, czy podana odpowiedź mieści się w zakresie dostępnych opcji
5.