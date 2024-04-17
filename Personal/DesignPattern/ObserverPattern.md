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
    - **Advantages:**
      - Subscriber does not have to poll to the Publisher to check for any changes (cpu efficient).
    - **Disadvantages:**
      - Publisher will push all data to all observers, some of these data might be irrelevant to some observers/subscribers (size inefficient).
  - **Pull:** Subscribers will pull the data whenever needed from the Subject.
    - **Advantages:**
      - Subscriber will call to only required getter methods of Publisher to get the state needed (size efficient).
    - **Disadvantages:**
      - Subscriber have to always poll to the Publisher to check for any changes (cpu inefficient).


## Rough
- implement weather station code.
- implement observer pattern in pizza factory app.
