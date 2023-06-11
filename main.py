import time;

import espresso
from brewcoffee import tworzNapoj
from progressbar import printProgressBar


def main():
    running = True;
    while running:
        print('CoffeeMaker 2000 menu');
        print('Select one of available options:');
        print('[e]spresso, [a]mericano');
        print('If you wish to quit the program, press [q].');
        inputString = input();
        #kawa, czasWazeniaKawy, rodzajGramatycznyKawy;
        if (inputString == 'e'):
            kawa = espresso;
            maszyna = tworzNapoj(kawa);


        #maszyna = brewCoffee(inputString);

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

        if inputString == "q":
            quit();


if __name__ == '__main__':
    main();