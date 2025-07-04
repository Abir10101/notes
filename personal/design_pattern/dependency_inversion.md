# Dependency Inversion Principle

- Idea behind Dependency Inversion Principle:
  - Depend upon abstractions. Do not depend upon concrete classes.
  - It suggests that our high-level components should not depend on our low-level components; rather, they should both depend on abstractions.


- The following guidelines can help you avoid OO designs that violate
the Dependency Inversion Principle:
  - No variable should hold a reference to a concrete class.
  - No class should derive from a concrete class.
  - No method should override an implemented method of any of its base classes.


- How to think about Dependency Inversion using our famous Pizza example:
  - **Guru**: You need to implement a PizzaStore. What’s the first thought that pops into your head?  
  **Student**: Pizza Stores prepare, bake and box pizzas. So, my store needs to be able to make  a bunch of different pizzas: CheesePizza, VeggiePizza, ClamPizza, and so on...

  - **Guru**: Right, you start at top and follow things down to the concrete classes. But, as you’ve seen, you don’t want your store to know about the concrete pizza types, because then it’ll be dependent on all those concrete classes! Now, let’s “invert” your thinking... instead of starting at the top, start at the Pizzas and think about what you can abstract.  
  **Student**: Well, a CheesePizza and a VeggiePizza and a ClamPizza are all just Pizzas, so they should share a Pizza interface.

  - **Guru**: But to do that you’ll have to rely on a factory to get those concrete classes out of your Pizza Store. Once you’ve done that, your different concrete pizza types depend only on an abstraction and so does your store. We’ve taken a design where the store depended on concrete classes and inverted those dependencies (along with your thinking).


- For example see [this](./FactoryPattern.md#creating-pizza-store).
