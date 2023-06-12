class Produkt:
    rodzaj = '';
    ilosc = 0;

    def __init__(self, rodzaj, ilosc):
        if not isinstance(ilosc, float) and not isinstance(ilosc, int):
            raise TypeError('Nieprawdidłowy typ danej został wprowadzony jako rodzaj substancji w kubku.');
        if ilosc < 0:
            raise ValueError ('Ilość substancji musi być większa od zera.');
        self.rodzaj = rodzaj;
        self.ilosc = ilosc;
        return;

    def zmien_stan(self, rodzaj):
        self.rodzaj = rodzaj;
        return;

    def podaj_ilosc(self):
        return self.ilosc;

    def podaj_rodzaj(self):
        return self.rodzaj;
