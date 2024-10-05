# Ghazi Lassoued's Messaging Platform

#### Description:

Overview:

The Messaging Platform is a web application developed as my final project for Harvard's CS50 course. The platform allows users to communicate with one another through private messages. It supports features such as user registration, secure login, sending and receiving messages, and maintaining a history of sent messages.

The project is built using Flask, a lightweight Python web framework, and SQLite for database management. The front end is constructed with HTML and CSS to ensure a responsive and user-friendly interface. The goal of this project was to create a functional and user-friendly messaging system that emphasizes simplicity and effectiveness.

Project Files:

### 1. `app.py`
This is the main Flask application file. It contains the routing logic for all the different pages and functionalities of the platform. The routes include:
- **`/register`**: Handles user registration, allowing new users to create an account.
- **`/login`**: Manages user authentication, ensuring that users can securely log in.
- **`/send`**: Allows users to send messages to other registered users, including a subject and body.
- **`/inbox`**: Displays all received messages, allowing users to view messages sent to them.
- **`/history`**: Shows the history of sent messages, letting users review their outgoing communication.
- **`/logout`**: Logs users out of their account securely, ending their session.
- **`/reply`**: Enables users to reply to messages directly from the inbox, simplifying the conversation process.

### 2. `helpers.py`
This file contains helper functions that support the main application. These functions include:
- **`login_required`**: A decorator that ensures routes are only accessible to logged-in users. This is critical for maintaining security and preventing unauthorized access to sensitive pages.
- **`apology`**: Returns an error message template when something goes wrong, providing users with a clear understanding of issues encountered.
- **`lookup`**: A function that can be modified or expanded to interact with external APIs if needed. While not currently in use, it offers flexibility for future expansion.

### 3. `project.db`
This is the SQLite database file that stores all the data for the platform, including user credentials and messages. The database contains two primary tables:
- **`users`**: Stores user information including `id`, `username`, and hashed passwords. This ensures that user data is securely managed and protected against unauthorized access.
- **`messages`**: Contains all the messages sent through the platform, including `id`, `sender`, `receiver`, `subject`, `body`, and `timestamp`. This structured storage enables efficient retrieval and management of messages.

### 4. `requirements.txt`
This file lists all the Python dependencies required to run the project. It includes:
- **Flask**: The main web framework used to build the application.
- **Werkzeug**: A WSGI utility library used for password hashing and session management.
- **SQLite3**: The database management system used to store user and message data.

### 5. `static/styles.css`
This is the stylesheet file that contains all the custom CSS for styling the web pages. The design aims to create a clean and minimalistic user interface, focusing on usability and clarity. The custom CSS allows for precise control over the look and feel of the platform, ensuring that it meets the project's design goals.

### 6. `templates/`
The `templates` directory contains all the HTML files used by Flask to render the pages. These templates include:
- **`layout.html`**: The base template that includes the common elements shared across all pages, such as the navigation bar and footer.
- **`register.html`**: The registration page template, designed to be straightforward and user-friendly.
- **`login.html`**: The login page template, where users authenticate themselves to access their accounts.
- **`index.html`**: The inbox page template, displaying received messages in a clear and organized manner.
- **`history.html`**: The template for displaying sent messages, helping users keep track of their communications.
- **`send.html`**: The page template for composing and sending new messages, designed for ease of use.
- **`reply.html`**: The template for replying to a received message, streamlining the conversation process.
- **`apology.html`**: A generic error page template used for handling errors, providing users with informative feedback when something goes wrong.

Design Choices:

### 1. User Authentication
One of the key design considerations was ensuring secure user authentication. Passwords are hashed using the `Werkzeug` library, and Flask's session management is used to keep users logged in securely. This design choice was made to prioritize user security, ensuring that sensitive information remains protected.

### 2. Database Schema
The database schema is kept simple yet efficient, with two main tables: `users` and `messages`. This schema was chosen to support the core functionality of the platform while ensuring scalability for potential future features like message threads or group chats. The simplicity of the schema allows for easy maintenance and potential expansion.

### 3. User Interface
The UI design is focused on simplicity and functionality. The layout is responsive, meaning it adjusts well to different screen sizes, ensuring a good user experience on both desktops and mobile devices. The color scheme is kept minimal to maintain focus on the content. This design choice was made to enhance usability and accessibility, ensuring that users can easily navigate the platform.

### 4. Flask Framework
Flask was chosen for its lightweight nature and ease of use. It allows for quick development and easy integration of Python functions, which is ideal for a project of this scope. The decision to use Flask also aligns with the course's focus on learning and implementing core programming concepts. Flask's flexibility and simplicity made it the perfect choice for this project, allowing for rapid development while maintaining control over the application's structure.

### 5. Custom CSS
While using external libraries like Bootstrap could have expedited the styling process, I opted to write custom CSS. This decision was driven by the desire to have full control over the appearance and to practice CSS skills. Writing custom CSS allowed me to tailor the platform's design to match my specific vision, ensuring a unique and cohesive look.

## Challenges Faced

Throughout the development of this project, I encountered several challenges, including managing user sessions, ensuring database integrity, and creating a responsive layout. Debugging and testing were crucial in resolving these issues. I also had to carefully design the data flow to ensure that user inputs are handled securely, preventing common vulnerabilities like SQL injection and XSS attacks. These challenges provided valuable learning opportunities, helping me to develop a deeper understanding of web development and security.

Future Improvements:

- **Message Deletion**: Adding the ability for users to delete messages. This feature would enhance user control over their inbox and help manage clutter.
- **Real-time Messaging**: Implementing WebSocket functionality for real-time messaging. This would make the platform more dynamic and responsive, providing a better user experience.
- **User Profiles**: Enhancing user profiles with additional information and customization options. Allowing users to personalize their profiles would add a more engaging and interactive element to the platform.

Conclusion :

This messaging platform is a culmination of the skills and concepts learned throughout the CS50 course. It demonstrates proficiency in web development, database management, and user interface design. The project serves as a solid foundation for further development and can be expanded with additional features in the future. I am proud of the work I have accomplished and look forward to exploring further improvements and enhancements to make this platform even more robust and user-friendly.

Author:

**Ghazi Lassoued**
- CS50 Final Project
- Monastir, Tunisia

