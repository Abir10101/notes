# SDLC without DevOps

The Software Development Life Cycle (SDLC) is a structured process that guides the creation of high-quality software. It encompasses all stages, from initial planning and requirements gathering, through coding and testing, to deployment and maintenance. This article explores the SDLC in the context of a Java application. I'll focus on SDLC stages from **Development** to **Deployment** & **Monitering** of the application.

## Development Server: The Crucible of Innovation

- **Purpose:** The development server is a local environment where individual developers implement features, fix bugs, and conduct initial testing.
- **Setup:** Developers clone the code repository and install Java & JDK. The application runs in this server using development environment variables (e.g., development database credentials).
- **Tools:** IDEs and code linters are used to ensure code quality and consistency.
- **Workflow:** After developing and locally testing a feature, the developer pushes the code to the testing server.

## Testing Server: The Bastion of Quality Assurance

- **Purpose:** This server is dedicated to comprehensive feature testing to identify bugs and vulnerabilities before deployment.
- **Types of Tests:**
    - **Unit Tests:** Verify the functionality of individual components in isolation.
    - **Integration Tests:** Check how different components interact.
    - **End-to-End (E2E) Tests:** Simulate user flows through the entire application.
    - **Performance Tests:** Assess how the application handles load and stress.
- **Setup:** JDK and Maven (for building and running the application) are installed. Code is pulled from the "testing" Git branch.
- **QA Role:** Quality Assurance (QA) teams manually test the software, focusing on usability, exploratory testing, and requirement fulfillment.
- **Benefits of a Separate Server:**
    - Long-running tests won't block developers.
    - Dedicated resources for testing ensure reliability.
- **Next Step:** After successful testing, the code is promoted to the production server.

## Production Server: The Arena of Real-World Usage

- **Purpose:** This is the live environment where end-users interact with the application. It houses the most stable code version.
- **Setup:** Similar to the testing server, JDK and Maven are installed. Code is pulled from the "release" Git branch. The application runs in a production server environment (e.g., Tomcat) using production environment variables.
- **Monitoring:** The application is continuously monitored. If issues arise, actions might include:
    - Rolling back to a previous version.
    - Assigning hotfix tasks to developers.

## Conclusion

This SDLC approach can be done manually without automation but in the world of fast feature deployment we have to automate some steps and implement devops methodology. I'll be writing about automating this application setup in my future articles.

This is my first blog writing. Feel free to comment if you have any questions or any refinement to the article. If you like the blog , don’t forget to like it & share with your friends/colleagues.

To get in personal touch, connect me on:
Linkedin:https://www.linkedin.com/in/abirmoulick/

Thanks for reading
Written with ❤️ & passion 🔥 by Abir Moulick
