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

- **User Types:** [Click here](examples/fpUserFactory.py)
- **Pizza Store:** [Click here](examples/fpPizzaStore.py).
- **Computer Manufacturer:** [Click here](examples/fpComputerCompany.py).

