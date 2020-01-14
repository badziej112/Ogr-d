from Symulacja import Symulacja

if __name__ == "__main__":

    sim = Symulacja(4)
    sim.start()

    print("Witaj w symulacji ogrodnika!")

    while sim.cykl < 200 or sim.monety <= 1000:

        if sim.woda <= 0 and sim.nawoz <= 0 and sim.nasiona <= 0:
            print("Przegrałeś! Skończyły ci się zasoby.")
            print("Zdobyto", sim.monety, "monet w", sim.cykl, "turach.")
            sys.exit()

        print("-------------------------")
        print("Wybierz akcje:")
        print("[1] - Posadz rosline.")
        print("[2] - Pokaż twoje zasoby.")
        print("[3] - Sprawdź pole.")
        print("[4] - Podlej lub nawieź rośliny.")
        print("[5] - Zakupy.")
        print("[6] - Wykop i sprzedaj.")
        print("[0] - Pomiń turę.")
        print("-------------------------")

        wybor = int(input())
        sim.dzialania(wybor)

    print("Wygrałeś!")
    print("Zdobyto", sim.monety, "monet w", sim.cykl, "turach.")



