# Horoskop

Aplikacja “Horoskop” - pyta użytkownika o datę urodzenia i przypadkowe dane. Na podstawie danych wyświelta znak zodiaku oraz magiczną przepowiednie na dany dzień.

### Cel
Stworzenie aplikacji webowej "Horoskop" w Flask, która pozwala użytkownikowi wprowadzić datę urodzenia oraz wyświetla jego znak zodiaku wraz z magiczną przepowiednią na dany dzień.

### Wymagania funkcjonalne
1. **Formularz wejściowy**:
   - Strona główna powinna zawierać formularz, w którym użytkownik może wprowadzić swoją datę urodzenia.
   - Po wprowadzeniu daty, aplikacja powinna przekierować użytkownika do strony z wynikami.

2. **Wyświetlanie wyników**:
   - Na stronie wyników powinien być wyświetlany znak zodiaku odpowiadający podanej dacie urodzenia.
   - Dodatkowo, strona powinna wyświetlać przepowiednię na aktualny dzień.

3. **Opcjonalnie**:
   - Możliwość wyświetlenia przepowiedni na inny, wybrany dzień.

### Aspekty techniczne
- Aplikacja powinna być zbudowana przy użyciu frameworka Flask.
- Dane dotyczące znaków zodiaku i przepowiedni mogą być pobierane z zewnętrznego API.

### API
- Wybierz darmowe API , które oferuje przepowiednie dzienna, tygodniową, miesięczną i roczną dla każdego znaku zodiaku. 
- Można je wykorzystać do uzyskania przepowiedni na podstawie daty urodzenia np. Aztro, Horoscope Match itp.

### Uruchomienie
- Aplikacja powinna być łatwa do uruchomienia lokalnie, zalecane użycie wirtualnego środowiska i `requirements.txt` dla zależności Pythona.
### Wskazówki
- Rozważ użycie JavaScriptu do dodatkowej interakcji na stronie, np. do wyboru innej daty bez konieczności ponownego ładowania strony.
- Zapewnij walidację wprowadzanych danych w formularzu, aby upewnić się, że data urodzenia jest w prawidłowym formacie.