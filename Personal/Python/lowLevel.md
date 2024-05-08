# PYTHON LOW LEVEL WORKING

### 1. How a programming language works?

- Source code (human readable) have to converted to machine code (0s & 1s) which the OS will execute.
- In C/C++
  - we compile the source code and we get the machine code file as output from the compiler.
  - Then we execute the machine code directly into OS.
  - So, the machine code file compiled in one OS (suppose Linux) cannot be executed in another OS (suppose Windows/Mac). This makes C/C++ platform dependent.
- In Java
  - we compile the source code and we get bytecode file as output. This bytecode file can only be run by JVM (Java Virtual Machine).
  - The JVM will convert the bytecode to machine code which OS will execute.
  - The bytecode compiled in one OS (suppose Linux) can be executed by any OS (suppose Windows/Mac), we have to install JVM for that OS then JVM will takes care of executing it. This makes Java Platform Independent.
- In Python
  - we just execute the source code.
  - Python comes with an interpreter. This interpreter contains the compilation and execution programs.
  - Python interpreter will first compile the source code into bytecode.
  - This bytecode, like Java is executed by the PVM (Python Virtual Machine).
  - The PVM converts the bytecode into machine code which the OS will execute.
  - As Python interpreter abstracts the compilation and execution process into a single command we call it interpreted language.
  - The bytecode, like java compiled in one OS (suppose Linux) can be executed by another OS (suppose Windows/Mac), we have to install the interpreter for that OS and it takes care of executing it. This makes Python platform independent.
- In PHP
  - we have similar compilation and execution process like Python.
  - PHP interpreter converts the source code into bytecode.
  - This bytecode will then be executed by Zend Engine. It converts the bytecode into machine code which the OS will execute. This makes the language platform independent.
  - Now, web server like Apache has module called `mod_php` has PHP compiler and Zend Engine build into it.
  - This means that PHP code can directly be executed from web servers.

### 2. How Python web application works? Use of Server Gateway Interface (WSGI/ASGI).

- In PHP, we seen that web server has a module which containes the PHP compiler and Zend Engine (executer).
- But, in python web server does not have any module to run the Python interpreter.
- Here comes the SGI (Server Gateway Interface). Web server will run the SGI program which in turn will run the Python interpreter.
- So, the request will first enter the web server which will forward the request to SGI server which will execute the Python program.

### 3. WSGI

- WSGI (Web Server Gateway Interface) is not a program but an interface. Some programs that implements WSGI are:
  - **Green Unicorn**: pre-fork worker model based server ported from the Ruby Unicorn project.
  - **uWSGI**: highly-performant WSGI server implementation.
  - **mod_wsgi**: Apache module implementing the WSGI specification.
  - **CherryPy**: pure Python web server that also functions as a WSGI server.
- It forward requests to synchronous python applications or functions.
- Gunicorn server can be configured to run multiple process of the app (also known as worker process) in different cpu cores, this enables in load distribution.

### 4. ASGI

- ASGI (Asynchronous Server Gateway Interface) is an interface. Some programs that implements ASGI are:
  - **Daphne**: Maintained as part of the Django project. Supports HTTP/1, HTTP/2, and WebSockets.
  - **Uvicorn**: Based on uvloop and httptools. Supports HTTP/1 and WebSockets.
- It primarily forward requests to asynchronous-capable python applications or functions.
- ASGI features:
  - **WSGI compatibilty**: a synchronous function or WSGI application can be run with ASGI server.
  - **WebSocket support**: ASGI servers support bidirectional communication channels like WebSockets, enabling real-time interactions between clients and servers. This enables building applications which require long-lived connections like real-time messaging applications, chat applications and streaming services.


### 5. What happens when we run a python script?

- When we run a python script, the script is submitted to the python interpreter.
- Components of python interpreter:
  - **Lexer:** It converts the code into stream of tokens.
  - **Parser:** It converts the stream of tokens produced by lexer into AST (Abstract Syntax Tree). It represents hierarchical structure of the code.
  - **Compiler:** It generates bytecode from AST.
  - **PVM (Python Virtual Machine):** It is responsible for executing the bytecode produced by the compiler. It manages program runtime environment. It handles memory management, variable scoping, garbage collection, GIL (Global Interpreter Lock), Dynamic typing, etc.
- In case of CPython implmentation, all interpreter components are build in C language.

### 6. Memory Management

We take the below example code and CPython implementation:

```py
def func():
  x = 5
  y = x
```

- Every variable or value in python is a struct object of C which has two variables
  - `ob_refcnt`: reference counter
  - `ob_type`: pointer that points to another struct object.
- When PVM executes the line `x = 5`
  - It creates struct object for `5` & `x` with different memory addresses.
  - For `5` object:
    - `ob_refcnt` incremented with 1.
    - `ob_type` points to struct object of `Integer`.
  - For `x` object:
    - `ob_refcnt` defaults to 0.
    - `ob_type` points to struct object of `5`.
- When PVM executes the line `y = x`
  - It creates struct object for `y`.
  - For `5` object:
    - `ob_refcnt` incremented with 2.
    - `ob_type` points to struct object of `Integer`.
  - For `x` object:
    - `ob_refcnt` incremented with 1.
    - `ob_type` points to struct object of `5`.
  - For `y` object:
    - `ob_refcnt` defaults to 0.
    - `ob_type` points to struct object of `x`.
  - For `y`, the struct object of `5` is not copied, i.e, **pass by reference**.
- When we delete or change values of both variables `x` & `y`
  - For `5` object:
    - `ob_refcnt` decreased to 0.
    - `ob_type` points to struct object of `Integer`.
    -  This object becomes avaliable for **garbage collection**.

### 7. GIL (Global Interpreter Lock)

- GIL is a mutex that allows only one thread have control over the python's interpreter.
- Python is **pass by reference** & variable's reference counter `ob_refcnt` is required to get the state of the object. This needs to be protected from race conditions. If multiple threads update `ob_refcnt`'s value then it can cause bugs like premature garbage collection.
- There are two types of programs:
  - I/O bound program.
  - CPU based or computation based program.
- For high CPU bound programs, GIL acquires the lock for a single thread and another thread cannot execute creating a performance bottleneck.
- But for I/O bound programs, GIL does not have much impact as it is released when waiting for I/O operation. So, another thread can work, i.e., **Concurrency**.
- For programs that have both I/O bound and high CPU bound operations
  - GIL will starve I/O bound treads while CPU bound threads will reacquire the lock everytime.
  - This issue was fixed in python version 3.2, by monitering the no. of request dropped counter by GIL.
