# SDLC without Devops

Suppose, a ecommerce application build using spring framework. I will cover the full SDLC process without any automation or Devops methods.

### Development Server
- This is the server that every developer has in the machine setup locally.
- Developer will implement features or fix bugs and manual test it locally.
- Clone the spring repository.
- Install java, jdk & spring in the machine to run the application.
- The application will be run in spring development server & loads development environment variables like development database credentials, etc.
- IDE setup and linting to be configured to prevent unhygenic code.
- After developing the desired feature, developer will push the code to testing server.

### Testing Server
- This is the server where feature testing happens to find any bugs & vulnerabilities before making the code live.
- Types of Tests:
  - **Unit Tests**: Test individual components/classes in isolation.
  - **Integration Tests**: Test how different components work together.
  - **End-to-End (E2E) Tests**: Test the entire application flow from start to finish.
  - **Performance Tests**: Measure how the application performs under load.
- Server setup with installing jdk & maven for building & runnning the application.
- Pull the code from the **testing** git branch.
- Build the application and run all the test scenarios using maven.
- QA team will manual test the software from this server. This includes usability testing, exploratory testing, and ensuring the software meets requirements.
- Why seperate server for testing?
  - Becuz test cases can take huge time to complete like a whole day.
  - Developers to focus on other tasks while testing is going on.
  - This server can be dedicated to testing workloads only.
- After passing everything from this server the code will pushed to production server.

### Production Server
- This server is where the most stable code lives and end users will use this server.
- Server setup with installing jdk & maven for building & runnning the application.
- Pull the code from the **release** git branch.
- The application will be run in production server like Tomcat & loads production environment variables like production database credentials, etc.
- Someone will moniter the application in this server and any problem may leads to:
  - Rollback to previous version.
  - Hotfix tasks to developers.
