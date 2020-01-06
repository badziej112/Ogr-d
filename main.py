from Symulacja import Symulacja

if __name__ == "__main__":

    sim = Symulacja(4)
    sim.start()

    print("Witaj w symulacji ogrodnika!")

    while sim.cykl < 99:
        print("-------------------------")
        print("Wybierz akcje:")
        print("[1] - Posadz rosline.")
        print("[2] - Pokaż twoje zasoby.")
        print("[3] - Sprawdź pole.")
        print("[4] - Podlej rośliny.")
        print("[5] - Zakupy.")
        print("[0] - Pomiń turę.")
        print("-------------------------")

        wybor = int(input())
        sim.dzialania(wybor)

