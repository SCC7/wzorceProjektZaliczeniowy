# from builder import Builder
# from prod1 import Product1
from urzadzenie import Urzadzenie


class wybierz_urzadzenie:
    def __init__(self, urzadzenie:Urzadzenie) -> None:
        self._urzadzenie = urzadzenie;

    # def reset(self):
    #     self._product = Product1()
    #
    # @property
    # def product(self) -> Product1:
    #     product = self._product
    #     self.reset()
    #     return product


    def build(self, ilosc):
        try:
            self._urzadzenie.wypelnianie(ilosc);
            self._urzadzenie.dzialanie();
            return self._urzadzenie.oproznianie;
        except ValueError:
            print ('ValueError');
        except TypeError:
            print ('TypeError');