from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato cream_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushroom red_onion oregano')
STEP_DELAY = 3


class Pizza:
    def __init__(self, name):
        self.name = name;
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough

        print(f'preparing the {self.dough.name} dough of your {self}')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('Margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print(f'adding tomato sauce to your Margarita')
        self.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print(f'Done with the tomato sauce')

    def add_topping(self):
        topping_desc = "podwójna mozzarella, oregano"
        topping_items = (PizzaTopping.double_mozzarella, PizzaTopping.oregano)
        print(f'adding toppings({topping_desc}) to your Margarita')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the toppings({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your margarita for {self.baking_time}s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f'your Margarita is ready!')


class CarbonaraBuilder:
    def __init__(self):
        self.pizza = Pizza('Carbonara')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print(f'adding tomato sauce to your {self.pizza}')
        self.sauce = PizzaSauce.cream_fraiche
        time.sleep(STEP_DELAY)
        print(f'Done with the {self.sauce} sauce')

    def add_topping(self):
        topping_desc = "mozzarella, boczek, szynka, pieczarki, czerwona cebula"
        topping_items = (
        PizzaTopping.mozzarella, PizzaTopping.bacon, PizzaTopping.ham, PizzaTopping.mushroom, PizzaTopping.red_onion)
        print(f'adding toppings({topping_desc}) to your Margarita')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the toppings({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking your {self.pizza} for {self.baking_time}s')
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f'your {self.pizza} is ready!')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self,builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        input_msg = "What pizza would you like, [m]argarita or [c]arbonara?"
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, only [m]argarita and [c]arbonara are available'
    return(True,builder)

def main():
    builders = dict(m=MargaritaBuilder, c=CarbonaraBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print('\n')
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print('\n')
    print(f'Enjoy your {pizza}!')

if __name__ == '__main__':
    main()