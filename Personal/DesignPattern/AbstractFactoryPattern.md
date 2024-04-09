# Abstract Factory Pattern

- When to use?
    - The Abstract Factory Pattern used for security measures by providing an interface for creating families of related or dependent objects without specifying their concrete classes.
    - The Abstract Factory defines the interface that all Concrete factories must implement, which consists of a set of methods for producing products.

- Is that a [Factory Pattern](./FactoryPattern.md) lurking inside the Abstract Factory?
    - **HeadFirst**: Can you explain yourself, Factory Method? 
    - **Factory Method**: Sure. Both Abstract Factory and I create objects – that’s our jobs. But I do it through inheritance...
    - **Abstract Factory**: ...and I do it through object composition.
    - **Factory Method**: Right. So that means, to create objects using Factory Method, you need to extend a class and override a factory method.
    - **Abstract Factory**: I provide an abstract type for creating a family of products. Subclasses of this type define how those products are produced. To use the factory, you instantiate one and pass it into some code that is written against the abstract type. So, like Factory Method, my clients are decoupled from the actual concrete products they use.
    - **HeadFirst**: Oh, I see, so another advantage is that you group together a set of related products. What happens if you need to extend that set of related products, to say add another one? Doesn’t that require changing your interface?
    - **Abstract Factory**: That’s true; my interface has to change if new products are added, which I know people don’t like to do. Use me whenever you have families of products you need to create and you want to make sure your clients create products that belong together.
    - **Factory Method**: Use me to decouple your client code from the concrete classes you need to instantiate, or if you don’t know ahead of time all the concrete classes you are going to need. To use me, just subclass me and implement my factory method!
