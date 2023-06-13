def sprawdz_poprawnosc_wyboru_w_menu(wejscie, poprawne_wejscia):
    if not any(wejscie == element for element in poprawne_wejscia):
        print('Nie mamy takiej opcji');
        return False;
    else:
        return True;


def wybierz_kawe(wybor):
    while True:
        print('Wybierz jedną z dostępnych pozycji:');
        print('[e]spresso, [a]mericano, [c]apucino, kawa z [m]lekiem');
        input_string = input('Jeśli chcesz wyjść z programu, wciśnij [q].');
        if input_string == 'q':
            return input_string;
        if not any(input_string == element for element in wybor):
            print('Nie mamy takiej opcji');
            continue;
        return input_string

def wybierz_rozmiar(wybor):
    while True:
        print('[m]ała, [d]uża kawa?')
        print('[p]owrót do poprzedniego menu')
        input_string = input();
        if input_string == 'd':
            return 'l';
        if input_string == 'm':
            return input_string
        if input_string == 'p':
            return input_string;
        print('Niepoprawny rozmiar! Proszę wybrać jedną z dwóch poniższych opcji:');