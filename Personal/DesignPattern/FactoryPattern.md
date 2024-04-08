# Factory Pattern

## When to use?

- When **class** needs to be **easily extendable** to allow for the addition of **new class types** without modifying existing client code.
- The pattern is particularly useful when you’re dealing with a large number of objects that **share a common interface** but have different **underlying complexities**. It helps in organising object creation process.

## How to implement?

- Theortically divide Classes into **Factory** and **Product**.
- Factory Class, ex: **ClassA** would return different object of the Product Class respective of the condition given. Basically, if else statements goes to this class. This class solely focus on returning the concrete Product Object.
- Create another class, ex: **ClassB** which will be dependent on the factory class, ClassA, call the product creation method of ClassA and actually creates the product for the client. This method of ClassB will be call by the Driver Class.
- Follow **dependency inversion** for making ClassB depend on ClassA.
- For Product Classes, create an interface for all products then implements it in their concrete classes. This must follow the principle `Program to an Abstraction not to an Implementation`.

## Example

#### Creating different user types

```python
class UserCreator:
	@abstractmethod
	def createUser():
		pass
	
	def getUserDetails(self) -> User:		
		user = self.createUser()
		user.toJson()
		user.getPrivileges()
		return user

class AdminUserCreator(UserCreator):
	def createUser() -> User:
		return AdminUser()

class NormalUserCreator(UserCreator):
	def createUser() -> User:
		return NormalUser()

class User():
	@abstractmethod
	def toJson():
		pass
	
	@abstractmethod
	def getPrivileges():
		pass

class AdminUser(User):
	def toJson():
		user = db.connect.query(sql)
		return jsonEncode(user)
	
	def getPrivileges():
		privilges = db.connect.query(sql)
		return privilges

class NormalUser(User):
	def toJson():
		user = db.connect.query(sql)
		return jsonEncode(user)
	
	def getPrivileges():
		privilges = db.connect.query(sql)
		return privilges

class Driver():
	def main():
		adminUser = AdminUserCreator()
		normalUser = NormalUserCreator()
		print(adminUser.getUserDetails())
		print(normalUser.getUserDetails())
```

#### Creating Pizza Store

```py
from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []
	
    def getName(self):
        return self.name
	
    def prepare(self):
        print(f"Preparing {self.name}")
	
    def bake(self):
        print(f"Baking {self.name}")
	
    def cut(self):
        print(f"Cutting {self.name}")
	
    def box(self):
        print(f"Boxing {self.name}")
	
    def __str__(self):
        display = f"---- {self.name} ----\n"
        display += f"{self.dough}\n"
        display += f"{self.sauce}\n"
        for topping in self.toppings:
            display += f"{topping}\n"
        return display

class WbStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "West Bengal Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")

class WbStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "West Bengal Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
        self.toppings.append("Garlic")
        self.toppings.append("Onion")
        self.toppings.append("Mushrooms")
        self.toppings.append("Red Pepper")

class BanStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Bangalore Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Fresh Mozzarella")
        self.toppings.append("Parmesan")
	
    def cut(self):
        print(f"Cutting the pizza into square slices")

class BanStyleVeggiePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Bangalore Deep Dish Veggie Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings.append("Shredded Mozzarella Cheese")
        self.toppings.append("Black Olives")
        self.toppings.append("Spinach")
        self.toppings.append("Eggplant")
	
    def cut(self):
        print(f"Cutting the pizza into square slices")

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

class WbPizzaStore(PizzaStore):
    def createPizza(self, type :str) -> Pizza:
        if(type == "cheese"):
            return WbStyleCheesePizza()
        elif (type == "veggie"):
            return WbStyleVeggiePizza()

class BanPizzaStore(PizzaStore):
    def createPizza(self, type :str) -> Pizza:
        if(type == "cheese"):
            return BanStyleCheesePizza()
        elif (type == "veggie"):
            return BanStyleVeggiePizza()


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

```
