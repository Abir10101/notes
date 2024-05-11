# PYTHON DEVELOPMENT

### 1. Test Driven Development

- Test-Driven Development (TDD) is an iterative development cycle that emphasizes writing tests before writing the actual feature or function.  
- TDD usually follows the "Red-Green-Refactor" cycle:
  1. Add a test to the test suite
  2. (Red) Run all the tests to ensure the new test fails.
  3. (Green) Write just enough code to get that single test to pass. Run all tests.
  4. (Refactor) Improve the initial code while keeping the tests green Repeat.

![tdd](src/tdd.png


### 2. CSRF

- > A Cross-Site Request Forgery (CSRF) attack is a type of attack where an attacker tricks an authenticated user into performing an unintended action on a website.
- Example of how an attacker might perform a CSRF attack:
  - The attacker identifies a website that is vulnerable to CSRF attacks. For example, a website that allows users to transfer funds.
  - The attacker creates a malicious link that, when clicked, will send a request to the vulnerable website. The link might look something like this: `https://example.com/transfer_funds?amount=1000&to=abcd@example.c`. This link appears to be a legitimate request to transfer $1000 to an email address.
  - The attacker sends the malicious link to the victim, usually through email, or a chat message. The link might be disguised as a legitimate request from the website or a trusted source.
  - The victim clicks the link, thinking it’s a legitimate request. Their browser sends the request to the vulnerable website, including the malicious parameters (amount=1000&to=abcd@example.c).
  - The vulnerable website processes the request, thinking it’s a legitimate request from the authenticated user. The website transfers $1000 to the attacker’s email address without the user’s knowledge or consent.
- **Prevention:**
  - **Anti-CSRF token:** Implementing anti-CSRF tokens in forms and verifying them on the server-side.
  - **Referer/Origin Validation:** Check that requests come from your trusted domain.
  - **Custom Headers:** Use headers that are difficult for third-party sites to replicate.


### 3. Model, ORM & Migrations

- **Model:**
  - > A model is a class representation of the structure and relationships of a database schema.
  - It typically consists of entities, attributes, and relationships between them.
  - Its purpose is to provide a provide a structure for the data, stored in the database.
  - It often includes methods to manipulate that data.
- **Object Relational Mapping (ORM):**
  - > An ORM is a tool that allows you to interact with a database using Model objects rather than writing raw SQL code.
  - Its purpose is to provide a layer of abstraction between the application and the database, enabling developers to use the programming language's syntax instead of SQL.
- **Migrations:**
  - > A migration is a script that contains instructions for altering the database schema. It includes operations such as creating tables, adding columns, or modifying existing structures.
  - Migration files are stored in SCM, enables versioning the database schema with the application's models.
