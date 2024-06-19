# SDLC without Devops

Suppose, a ecommerce application build using spring framework. I will cover the full SDLC process without any automation or Devops methods.

### Development Server:
- This is the server that every developer has in the machine setup locally.
- Developer will implement features or fix bugs and manual test it locally.
- Clone the spring repositery.
- Install java, jdk & spring in the machine to run the application.
- The application will be run in spring development server & loads development environment variables like development database credentials, etc.
- IDE setup and linting to be configured to prevent unhygenic code.

### Testing Server:
- This is the server that every developer has in the machine setup locally.
- Developer will implement features or fix bugs and manual test it locally.
- Clone the spring repositery.
- Install java, jdk & spring in the machine to run the application.
- The application will be run in spring development server & loads development environment variables like development database credentials, etc.
- IDE setup and linting to be configured to prevent unhygenic code.

Development
- git clone the software repo.
- suppose, the software is in spring framework.
- install jdk & maven for building & runnning the application.
- install linting and best practices restriction softwares.

Testing
- git clone the software repo the testing branch.
- install jdk & maven for building & runnning the application.
- build and run all the tests for the sofware. what are the type of tests run in this step?
- why we dont run tests in development server?
  - Becuz test cases may take a whole day to complete.
  - developer can take on other tasks in the meantime.
- Qa team will also the QA testng of the software from this server.

Production
- git clone the software repo the production branch.
- install jdk & maven for building & runnning the application.
- run the application. what happens if application failed here?
