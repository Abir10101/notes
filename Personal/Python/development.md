# PYTHON DEVELOPMENT

### 1. Test Driven Development

- Test-Driven Development (TDD) is an iterative development cycle that emphasizes writing tests before writing the actual feature or function.
- TDD usually follows the "Red-Green-Refactor" cycle:
  1. Add a test to the test suite
  2. (Red) Run all the tests to ensure the new test fails.
  3. (Green) Write just enough code to get that single test to pass. Run all tests.
  4. (Refactor) Improve the initial code while keeping the tests green Repeat.

![](src/tdd.png)
- [Full implementation](https://github.com/mjhea0/flaskr-tdd).


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
  - It consists of entities, attributes, and relationships between tables.
  - Its purpose is to provide a structure for the data, stored in the database.
  - It often includes methods to manipulate datas in the table.
- **Object Relational Mapping (ORM):**
  - > An ORM is a tool that is used to interact with a database using Model objects rather than writing raw SQL code.
  - Its purpose is to provide a layer of abstraction between the application and the database, enabling developers to use the programming language's syntax instead of SQL.
- **Migrations:**
  - > A migration is a script file that contains instructions for altering the database schema. It includes operations such as creating tables, adding columns, or modifying existing structures.
  - Migration files are stored in SCM, enables versioning the database schema with the application's models.


### 4. Global Error Handling In Flask

- Flask has a decorator function `errorhandler()` that can catch errors globally from flask application.
- Implementation:
  ```py
  from flask import Flask, abort, jsonify
  from werkzeug.exceptions import HTTPException

  app = Flask(__name__)

  @app.errorhandler(Exception)
  def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

  @app.route("/")
  def index():
    abort(409)
  ```
  Output:
  ```sh
  $ http get http://127.0.0.1:1234/
  HTTP/1.0 409 CONFLICT
  Content-Length: 31
  Content-Type: application/json
  Date: Sun, 29 Mar 2015 17:06:54 GMT
  Server: Werkzeug/0.10.1 Python/3.4.3

  {
      "error": "409: Conflict"
  }

  $ http get http://127.0.0.1:1234/abcd
  HTTP/1.0 404 NOT FOUND
  Content-Length: 32
  Content-Type: application/json
  Date: Sun, 29 Mar 2015 17:06:58 GMT
  Server: Werkzeug/0.10.1 Python/3.4.3

  {
      "error": "404: Not Found"
  }
  ```


### 5. Middleware in Flask

- Middleware is a class/function that runs before sending a request to a route function or after returning a response from a route function.
- Usecases:
  - Authorization
  - Logging
  - Caching
- Implementations:
  - Using `before_request` hook.
    ```py
    from flask import Flask, request
    from datetime import datetime

    app = Flask(__name__)

    @app.before_request
    def before_request():
      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      print(f"Timestamp: {timestamp}, Route: {request.path}, Method: {request.method}")

    @app.route('/')
    def index():
        return "Hello World"
    ```
  - Using python decorator.
    ```py
    from flask import Flask, request
    from datetime import datetime
    from functools import wraps

    app = Flask(__name__)

    def log_request_details(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Timestamp: {timestamp}, Route: {request.path}, Method: {request.method}")
            return f(*args, **kwargs)
        return decorated_function

    @app.route('/')
    @log_request_details
    def index():
        return "Hello World"
    ```
  - Using `before_request_funcs` for a blueprint.
    ```py
    from flask import Flask, Blueprint, request
    from datetime import datetime

    app = Flask(__name__)

    # Define the blueprint
    api = Blueprint('main_blueprint', __name__)

    # Define the before_request function for the blueprint
    def logDetails():
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Timestamp: {timestamp}, Route: {request.path}, Method: {request.method}")

    # Define a route within the blueprint
    @api.route('/')
    def index():
        return 'hello world'

    # Register the before_request function with the app's before_request_funcs
    app.before_request_funcs = {
        'main_blueprint': [logDetails]
    }

    # Register the blueprint with the main app
    app.register_blueprint(api)
    ```


### 6. Flask Application Context

- Flask application object created like `app = FLask(__name__)` might cause importing errors while working in factory pattern archietecture or blueprints. To solve this issue flask uses contexts that is available thought the application.
- Flask creates a application context that can be accessed via `current_app` attribute inside the blueprints.
- **Application Context Lifecyle:** Whenever a request recieved from WSGI server flask creates a application comtext and request context. The context lives until the request completes processing.
  - **Request Context:** This will contain the request attributes like HTTP methods, request headers, session attributes, etc.
  - **Application Context:** This will contain config variables, logger attributes, global variables, etc.
- We need to manually create and teardown contexts in certain scenarios where app request is not made. An example of certain scenario is Application Testing.
