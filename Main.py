# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from Drink import Drink
from HotDrink import HotDrink
from MineralWater import MineralWater
from DrinkMachine import DrinkMachine


class Main:
    controller = DrinkMachine()

    drink = Drink("тархун", 200)
    hot_drink = HotDrink("кофе", 200, 85)
    mineral = MineralWater("Горячий ключ", 300, "не газированная")

    controller.setProduct(Drink("буратино", 500))
    controller.setProduct(drink)

    controller.setProduct(hot_drink)
    controller.setProduct(mineral)

    controller.allProduct()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
