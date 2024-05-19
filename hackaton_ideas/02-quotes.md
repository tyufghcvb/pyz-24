## Apka cytatów z książek

### Cel
Stworzenie prostej aplikacji webowej z użyciem Flask, która pozwoli na przechowywanie i przeglądanie ulubionych cytatów z książek. Aplikacja nie wymaga systemu logowania ani zarządzania kontami użytkowników.

### Wymagania
1. **Strona główna (index)**:
   - Wyświetla wszystkie cytaty, posortowane od najnowszego.
   - Zawiera menu z linkiem do strony umożliwiającej dodanie nowego cytatu.
   - Po dodaniu cytatu użytkownik jest przekierowywany z powrotem na stronę główną, gdzie widoczne są wszystkie cytaty.

2. **Strona pojedynczego cytatu**:
   - Umożliwia przeczytanie całego cytatu.
   - Zawiera przycisk umożliwiający powrót na stronę główną.

3. **Strona dodawania cytatu**:
   - Zawiera jedno pole tekstowe do wpisania cytatu i przycisk do dodania cytatu.

### Funkcjonalności dodatkowe
- Na stronie głównej przy długich cytatach powinna znajdować się opcja "zobacz więcej", która przenosi na stronę pojedynczego cytatu. A wyświelne jest tylko N-pierwszych znaków.
- Rozważ użycie SQLite jako bazy danych dla prostoty implementacji.

### Aspekty wizualne
- Aspekty wizualne nie będą oceniane. Skupiamy się na funkcjonalności.

### Implementacja
- Użyj frameworka Flask do stworzenia aplikacji.
- Pamiętaj o przekierowaniach po dodaniu cytatu.

### Uruchomienie
- Aplikacja powinna być łatwa do uruchomienia lokalnie, zalecane użycie wirtualnego środowiska i `requirements.txt` dla zależności Pythona.
