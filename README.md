# My Blog

My Blog is a web application built with Flask. It allows users to create, read, update, and delete blog posts. Additionally, users can register accounts, log in, and manage their profiles. This application uses SQLite and SQLAlchemy to store and retrieve user and post data. The application also ensures that no two users have the same email or username, and users may also not update their information to existing emails or usernames.

## Features

- **User Authentication**: Users can register accounts, log in, and log out.
- **Profile Management**: Users can update their profile information and profile picture.
- **Blog Post Management**: Users can create, read, update, and delete blog posts.
- **Responsive Design**: The application is built with Bootstrap for a mobile-friendly experience.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask WTForms
- Flask Login

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/my_blog.git
    cd my_blog
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. Run the application:
    ```bash
    flask run
    ```

## Usage

- Navigate to the home page to view recent blog posts.
- Register for an account or log in if you have an existing account.
- Update your profile information and profile picture on the account page.
- Create a new blog post or edit/delete existing ones.
- Log out when you're done.

