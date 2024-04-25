# Observer Pattern

- > **Defination:**  
  The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.
- Publishers + Subscribers = Observer Pattern
- Publisher is the Subject which will change. Subscribers are the ones which will run on change of the Subject/Publisher.
- This works like when you subscribe to a newsletter of a website.
  - when you subscribe you get notified when a new newsletter is posted.
  - you can unsubscribe to stop receiving notification from the website's newsletter.
- There are two types of observer pattern: **Push** & **Pull**
  - **Push:** Publisher will call the `update` method of observer and sending all the data in parameter.  
  **Disadvantage:** Some of these data might be irrelevant to some observers/subscribers (size inefficient).  
  **Advantage:** For small datasets this is the simplest approach and require less coding.  
  - **Pull:** Publisher will call the `update` method of observers. Observer will use getter methods of Publisher to get only those data which is relevant to it (size efficient).

## Examples

- **Weather Station:** [Click here](examples/opWeatherStation.py).

## Design Principles

- *Identify the aspects of your application that vary and separate them from what stays the same:*
  - The thing that varies in the Observer Pattern is the state of the Subject and the number and types of Observers. With this pattern, you can vary the objects that are dependent on the state of the Subject, without having to change that Subject. That’s called planning ahead!
- *Program to an interface, not an implementation:*
  - Both the Subject and Observer use interfaces. The Subject keeps track of objects implementing the Observer interface, while the observers register with, and get notified by, the Subject interface. As we’ve seen, this keeps things nice and loosely coupled.
- *Favor composition over inheritance:*
  - The Observer Pattern uses composition to compose any number of Observers with their Subjects. These relationships aren’t set up by some kind of inheritance hierarchy. No, they are set up at runtime by composition!
- *Classes should be open for extension, but closed for modification:*
  - The Subject Class can notify more objects without changing its existing code.

