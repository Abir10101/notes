# Observer Pattern

- > **Defination:**  
  The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all of its dependents are notified and updated automatically.
- Publishers + Subscribers = Observer Pattern
- Publisher is the Subject which will change. Subscribers are the ones which will run on change of the Subject/Publisher.
- This works like when you subscribe to a newsletter of a website.
  - when you subscribe you get notified when a new newsletter is posted.
  - you can unsubscribe to stop receiving notification from the website's newsletter.
- There are two types of observer pattern: **Push** & **Pull**
  - **Push:** Publisher will send all the data to all its observers.  
  **Disadvantage:** Some of these data might be irrelevant to some observers/subscribers (size inefficient).
  - **Pull:** Publisher will send only the state changed flag to all its observers. Observer will use getter methods of Publisher to get only those data which is relevant to it (size efficient).


## Rough
- implement weather station code.
- implement observer pattern in pizza factory app.
