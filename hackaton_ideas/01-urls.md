# Generator linków affiliacyjnych 

## Cel:
Celem zadania jest stworzenie skryptu w Pythonie, wykorzystującego programowanie obiektowe, który umożliwi przetwarzanie linków URL do produktów księgarni i generowanie dedykowanych linków na podstawie identyfikatora klienta.

Zapoznaj się z dokumentacją przykładowego [programu parterskiego](https://program-partnerski.helion.pl/dokumentacjapp.pdf).

### Przykłady
- **Struktura URL**:
  - Strona główna: `https://helion.pl/` → `https://helion.pl/view/[ID klienta]`
  - Strona produktu: `https://helion.pl/ksiazki/nazwa_ksiazki` → `https://helion.pl/view/[ID klienta]/nazwa_ksiazki`
  - Strona promocji: `https://helion.pl/kategorie/promocja-xyz` → `https://helion.pl/page/[ID klienta]/promocja/promocja-xyz`
  - Link do kategorii: `https://helion.pl/kategorie/programowanie` → `https://helion.pl/page/[ID klienta]/kategorie/programowanie`

    
### Etap 1
Stwórz skrypt, w którym obierzesz od klienta:
- numer id klienta - to kod numeryczny, pięciocyfrowy np. `90412`
- link do produktu

### Etap 2
Napisz funkcję, która pobiera od użytkownika lub sama rozpoznaje jakiego typu został podany url.

URL jakie obsługuje funkcja:
- strona główna
- strona produktu
- strona promocji
- dodanie zestawu do koszyka
- link do kategorii
-  ...

### Etap 3

Użytkowników może wielokrotnie dodać link do przekształcenia w link dedykowany.

### Etap 4

Użytkownik może zapisać wszystkie do tej pory zrobione linki do pliku `txt` lub `csv`

### Wymagania

Zadbaj o aspekty takie jak obsługa błędów 
- błędny input użytkownika - tekstowy czy plik wejściowy
- nierozpoznany typ URL
- URL nieprawidłowy


### Rozszerzenia
- Użytkownik podaje plik `.txt` lub `.csv` z listą książek. Każda książka znajduje sięw nowym wierszu.
- Otrzymuje plik wynikowy z listą dedykowanych linków.
- Zmodyfikuj program tak, by w pliku wynikowym pierwsza kolumna zawierała link oryginalny, druga `-`, a trzecia link dedykowany.
- Kod powinen analogicznie działać dla innych domen grupy helion np. ebookpoint czy videopoint.

### Rozszerzenie

Zapoznaj się z wyrażeniami regularnymi, by przetestować czy podany input jest linkiem


## Wskazówki
[opcjonalne, mogą pomóc w planowaniu prac]

### Etap 1: Przygotowanie podstawowej struktury
1. **Stworzenie klasy `LinkProcessor`**:
   - Klasa powinna być odpowiedzialna za przetwarzanie dostarczonych linków URL i generowanie linków dedykowanych.
   - Metoda `generate_dedicated_link` powinna przyjmować identyfikator klienta i link URL, a następnie zwracać przetworzony link.

### Etap 2: Interfejs użytkownika
1. **Implementacja interfejsu użytkownika**:
   - Napisz prosty skrypt lub interfejs wiersza poleceń, który pozwala użytkownikowi na wprowadzenie identyfikatora klienta i linku URL.
   - Skrypt powinien używać instancji klasy `LinkProcessor` do generowania dedykowanych linków na podstawie danych wejściowych użytkownika.

### Etap 3: Rozpoznawanie typów URL
1. **Funkcja rozpoznawania URL**:
   - Zaimplementuj w klasie `LinkProcessor` metodę `recognize_url_type`, która analizuje i klasyfikuje linki URL do jednej z kategorii:
     - Strona główna
     - Strona produktu
     - Strona promocji
     - Dodanie zestawu do koszyka
     - Link do kategorii

### Etap 4: Zapis do pliku
1. **Stworzenie klasy `FileHandler`** lub oddzielnego modułu odczytu/zapisu:
   - Klasa odpowiedzialna za obsługę plików (txt lub csv).
   - Metoda `save_links_to_file`, która przyjmuje listę linków i zapisuje je w odpowiednim formacie.

### Rozszerzenia
1. **Przetwarzanie plików z linkami**:
   - Umożliw programowi przetwarzanie plików .txt lub .csv z wejściową listą linków.
   - Każdy link powinien znajdować się w nowym wierszu.
   - Wynikowy plik powinien zawierać dedykowane linki w odpowiednio sformatowanych kolumnach.

