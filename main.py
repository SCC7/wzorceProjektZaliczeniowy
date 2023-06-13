from przepisy.americano import Americano
from przepisy.capucino import Capucino
from przepisy.espresso import Espresso
from przepisy.KawaZMlekiem import KawaZMlekiem
from rozne.brewcoffee import tworzNapoj
from rozne.sprawdzanieWejscia import wybierz_kawe, wybierz_rozmiar


def main():
    running = True;
    while running:
        poprawne_wejscia_menu = ['e', 'a', 'c', 'm', 'q'];
        poprawne_wejscia_rozmiary = ['m', 'd', 'p'];
        print();
        print('KawoMator 2000 menu');
        main_loop = True;
        while main_loop:
            napoj_do_stworzenia = wybierz_kawe(poprawne_wejscia_menu)
            if napoj_do_stworzenia == 'q':
                quit();

            rozmiar_napoju = wybierz_rozmiar(poprawne_wejscia_rozmiary)
            if rozmiar_napoju == 'p':
                continue;

            # if not any(input_string == element for element in poprawne_wejscia):
            #     if input_string == 'd':
            #         print("Nie mamy takiej opcji")
            #         continue;
            #     print('Nie mamy takiej opcji');
            #     continue;
            # if input_string == 'q':
            #     running = False;
            #     quit();
            # running_choice_loop = False;

            # niepoprawny_rozmiar = True;
            # while niepoprawny_rozmiar:
            #     print('[m]ała, [d]uża kawa?')
            #     print('[p]owrót do poprzedniego menu')
            #     input_string_druga = input();
            #     if input_string_druga == 'd':
            #         input_string_druga = 'l';
            #         super.niepoprawny_rozmiar = False;
            #         go_back_to_menu = True;
            #         break;
            #     if input_string_druga == 'm':
            #         super.niepoprawny_rozmiar = False;
            #         go_back_to_menu = True;
            #         break;
            #     if input_string_druga == 'p':
            #         break;

            #     print('Niepoprawny rozmiar! Proszę wybrać jedną z dwóch poniższych opcji:');
            # if go_back_to_menu:
            #     continue;

            dostepne_napoje = dict(e=Espresso, a=Americano, c=Capucino, m=KawaZMlekiem)

            kawa = dostepne_napoje[napoj_do_stworzenia]
            tworzNapoj(kawa(rozmiar_napoju))

            input('Naciśnij enter, aby zacząć od nowa');
            break;
        # napoj_do_stworzenia = wybor_napoju[input_string];
        # maszyna = stworz_napoj(napoj_do_stworzenia)
        # maszyna = brewCoffee(inputString);

        # if inputString == "e":
        #     print('Twoje espresso jest przygotowywane');
        #
        #     points = list(range(0, 67));
        #     pointsLength = len(points);
        #     printProgressBar(0, pointsLength, prefix = "Postęp procesu:", suffix = "complete", length = 50);
        #     for i, points in enumerate(points):
        #         time.sleep(0.1);
        #         printProgressBar(0+i, pointsLength, prefix="Postęp procesu:", suffix="complete", length=50);
        #     printProgressBar(pointsLength, pointsLength, prefix="Postęp procesu:", suffix="complete", length=50);
        #
        #     print('Twoje espresso jest gotowe! Smacznego!');


if __name__ == '__main__':
    main();
