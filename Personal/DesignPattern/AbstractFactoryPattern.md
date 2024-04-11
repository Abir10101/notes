# Abstract Factory Pattern

- When to use?
  - Use it when you need to work with various families of related products but dont want to depend on the concrete classes of those products.
- This is very much similar with factory pattern
  - **Factory Pattern:** We have to override the abstract factory method of abstract class in concrete classes.
  - **Abstract Factory Pattern:** Here we have multiple abstract factory methods in asbtract class which we will override in the concrete classes returning the concrete product.

## Examples

- **Pizza Store:** [Click here](examples/afpPizzaStore.py).
- **Computer Manufacturer:** [Click here](examples/afpComputerCompany.py).
