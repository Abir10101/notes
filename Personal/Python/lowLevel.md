# PYTHON LOW LEVEL WORKING

### 1. How a programming language works

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

- WSGI (Web Server Gateway Interface) is not a program but an interface. Programs that implements WSGI are:
  - **Green Unicorn**: pre-fork worker model based server ported from the Ruby Unicorn project.
  - **uWSGI**: highly-performant WSGI server implementation.
  - **mod_wsgi**: Apache module implementing the WSGI specification.
  - **CherryPy**: pure Python web server that also functions as a WSGI server.
- Features of WSGI server:
  - Gunicorn server can be configured to run multiple process of the app (also known as worker process) in different cpu cores, this enables in load distribution.

<hr>
