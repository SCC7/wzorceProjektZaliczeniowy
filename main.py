from przepisy.americano import Americano
from przepisy.espresso import Espresso
from rozne.brewcoffee import tworzNapoj


def main():
    running = True;
    while running:
        print('CoffeeMaker 2000 menu');
        print('Select one of available options:');
        print('[e]spresso, [a]mericano');
        print('If you wish to quit the program, press [q].');
        input_string = input();
        if input_string == 'q':
            running = False;
            quit();
        # wybor_napoju = dict(e=Espresso, a=Americano);
        # kawa, czasWazeniaKawy, rodzajGramatycznyKawy;
        dostepne_napoje = dict(e=Espresso(), a=Americano())

        kawa = dostepne_napoje[input_string]
        maszyna = tworzNapoj(kawa, 'm');
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
