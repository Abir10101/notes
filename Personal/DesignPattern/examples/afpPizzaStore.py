from abc import ABC, abstractmethod

# Ingredients
class Dough(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Sauce(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Cheese(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Veggies(ABC):
    @abstractmethod
    def __str__(self):
        pass

class ThickCrustDough(Dough):
    def __str__(self):
        return "ThickCrust style extra thick crust dough"

class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Tomato sauce with plum tomatoes"

class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Shredded Mozzarella"

class BlackOlives(Veggies):
    def __str__(self):
        return "Black Olives"

class Spinach(Veggies):
    def __str__(self):
        return "Spinach"

class Eggplant(Veggies):
    def __str__(self):
        return "Eggplant"

class ThinCrustDough(Dough):
    def __str__(self):
        return "ThinCrust style thin crust dough"

class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"

class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"

class Garlic(Veggies):
    def __str__(self):
        return "Garlic"

class Onion(Veggies):
    def __str__(self):
        return "Onion"

class Mushroom(Veggies):
    def __str__(self):
        return "Mushroom"

class RedPepper(Veggies):
    def __str__(self):
        return "RedPepper"


# Ingredient Factories
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def createDough(self) -> Dough:
        pass

    @abstractmethod
    def createSauce(self) -> Sauce:
        pass

    @abstractmethod
    def createCheese(self) -> Cheese:
        pass

    @abstractmethod
    def createVeggies(self) -> list[Veggies]:
        pass

class WbPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self) -> Dough:
        return ThickCrustDough()

    def createSauce(self) -> Sauce:
        return PlumTomatoSauce()

    def createCheese(self) -> Cheese:
        return MozzarellaCheese()

    def createVeggies(self) -> list[Veggies]:
        veggies = [
            BlackOlives(),
            Spinach(),
            Eggplant()
        ]

        return veggies

class BanPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self) -> Dough:
        return ThinCrustDough()

    def createSauce(self) -> Sauce:
        return MarinaraSauce()

    def createCheese(self) -> Cheese:
        return ReggianoCheese()

    def createVeggies(self) -> list[Veggies]:
        veggies = [
            Garlic(),
            Onion(),
            Mushroom(),
            RedPepper()
        ]

        return veggies


# Pizzas
class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.veggies = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print(f"Baking {self.name}")

    def cut(self):
        print(f"Cutting {self.name}")

    def box(self):
        print(f"Boxing {self.name}")

    def __str__(self):
        display = f"---- {self.name} ----"
        display += f"\n{self.dough}"
        display += f"\n{self.sauce}"
        display += f"\n{self.cheese}"
        for veggie in self.veggies:
            display += f"\n{veggie}"
        return display

class CheesePizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()

class VeggiePizza(Pizza):
    def __init__(self, ingredientFactory):
        super().__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()


# Pizza Factories
class PizzaStore:
    @abstractmethod
    def createPizza(self):
        pass

    def orderPizza(self, type :str):
        pizza = self.createPizza(type)
        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();
        print(pizza)

class WbPizzaStore(PizzaStore):
    def __init__(self):
        self.ingredientFactory = WbPizzaIngredientFactory()

    def createPizza(self, type :str) -> Pizza:
        pizza = None
        if type == "cheese":
            pizza = CheesePizza(self.ingredientFactory)
            pizza.setName("West Bengal Style Cheese Pizza")
        elif type == "veggie":
            pizza = VeggiePizza(self.ingredientFactory)
            pizza.setName("West Bengal Style Veggie Pizza")

        return pizza

class BanPizzaStore(PizzaStore):
    def __init__(self):
        self.ingredientFactory = BanPizzaIngredientFactory()

    def createPizza(self, type: str) -> Pizza:
        pizza = None
        if type == "cheese":
            pizza = CheesePizza(self.ingredientFactory)
            pizza.setName("Bangalore Style Cheese Pizza")
        elif type == "veggie":
            pizza = VeggiePizza(self.ingredientFactory)
            pizza.setName("Bangalore Style Veggie Pizza")

        return pizza


#  Driver
if __name__ == "__main__":
    wbStore = WbPizzaStore()
    wbStore.orderPizza("cheese")
    print("=====")
    wbStore.orderPizza("veggie")
    print("============================")
    banStore = BanPizzaStore()
    banStore.orderPizza("cheese")
    print("=====")
    banStore.orderPizza("veggie")
