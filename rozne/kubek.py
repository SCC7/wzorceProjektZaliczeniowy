class Kubek:
    rozmiar = 0;
    zawartosc = dict();

    def __init__(self, rozmiar):
        # print(f'DEBUG kubek.rozmiar = {rozmiar}')
        if not isinstance(rozmiar, int) and not isinstance(rozmiar, float):
            raise TypeError('Zły typ danych został wprowadzony jako rozmiar kubka.');
        if 0 > rozmiar > 400:
            raise ValueError('Zły rozmiar kubka!');
        self.rozmiar = rozmiar;
        self.zawartosc = dict();

    def dodaj_zawartosc(self, rodzaj, ilosc):
        if not isinstance(rodzaj, str):
            raise TypeError('Zły typ danych został wprowadzony jako rodzaj zawartości.');
        # if not isinstance(rodzaj, produkt.podaj_rodzaj):
        #     raise TypeError('Niepożądany obiekt znalazł się w kubku.');
        self.zawartosc[rodzaj] = ilosc;
        self.sprawdz_czy_sie_miesci();

    def sprawdz_czy_sie_miesci(self):
        suma = 0;
        # print(f'DEBUG Tegesy w kubku: {self.zawartosc.keys()}')
        # print(f'Rozmiar kubka: {self.rozmiar}')
        for x in self.zawartosc:
            # print(f'DEBUG Zawartość kubka: {self.zawartosc[x]}')
            # print(f'DEBUG suma = {suma}')
            suma += self.zawartosc[x];
            # print(f'DEBUG suma = {suma}')
            if suma > self.rozmiar:
                # print(f'test float/int: czy {suma} == {self.rozmiar}? {suma == self.rozmiar}')
                # pass
                raise ValueError(f'Kubek został przepełniony! Rozmiar kubka: {self.rozmiar}, zawartość kubka: {suma}');

    def pokaz_zawartosc(self):
        print('###############################')
        print('Zawartość twojego kubka z kawą:')
        x = 1;
        suma = 0;
        for key in self.zawartosc:
            print(f'{x}. {key}: {self.zawartosc[key]} ml');
            suma += self.zawartosc[key];
            x += 1;
        print(f'Razem: {suma} ml')
        print('###############################')
