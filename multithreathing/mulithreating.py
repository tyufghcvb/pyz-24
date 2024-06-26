import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)  # Opóźnieniedla symulacji czasochłonnej operacji

def perform_main_thread_tasks():
    print("Wątek główny wykonuje inne zadania.")
    for _ in range(100):
        print('.', end="")
        time.sleep(0.01)  # Opóźnieniedla symulacji trwającej operacji
    print()
    print('Koniec głównego zadania')

def main():
    # Utworzenie wątku
    thread = threading.Thread(target=print_numbers)
    # Uruchomienie wątku
    thread.start()

    # Wykonanie zadania przez główny wątek
    perform_main_thread_tasks()

    # Oczekiwanie na zakończenie wątku
    thread.join()
    print("Wątek pomocniczy zakończył pracę.")

if __name__ == "__main__":
    main()