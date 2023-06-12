# from builder import Builder
# from prod1 import Product1
from urzadzenia.urzadzenie import Urzadzenie


class WybierzUrzadzenie:
    def __init__(self, urzadzenie: Urzadzenie) -> None:
        self._urzadzenie = urzadzenie;


    # def reset(self):
    #     self._product = Product1()
    #
    # @property
    # def product(self) -> Product1:
    #     product = self._product
    #     self.reset()
    #     return product

    def build(self, rodzaj_substancji, ilosc):
        try:
            # print('DEBUG rodzaj urzadzenia:')
            # print(self._urzadzenie.zidentyfikuj(self));
            # print('DEBUG urzadzenie.wypelnianie')
            self._urzadzenie.wypelnianie(self, rodzaj_substancji, ilosc);
            # print('DEBUG urzadzenie.dzialanie')
            self._urzadzenie.dzialanie(self);
            # print('DEBUG urzadzenie.oproznianie')
            return self._urzadzenie.oproznianie(self);
        except ValueError:
            print('ValueError');
        # except TypeError:
        #     print('TypeError');
