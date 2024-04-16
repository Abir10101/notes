# Observer Pattern

- > **Defination:**  
  The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.
- Publishers + Subscribers = Observer Pattern
- Publisher is the Subject which will change. Subscribers are the ones which will run on change of the Subject/Publisher.
- This works like when you subscribe to a newsletter of a website.
  - when you subscribe you get notified when a new newsletter is posted.
  - you can unsubscribe to stop receiving notification from the website's newsletter.
- There are two types of observer pattern: **Push** & **Pull**
  - **Push:** Subject will notify the Subscribers.
  - **Pull:** Subscribers will pull the data whenever needed from the Subject.


## Rough
- implement weather station code.
- implement observer pattern in pizza factory app.
