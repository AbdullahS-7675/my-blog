# my_blog
my_blog is a CRUD (Create, Read, Update, Delete) application built with Flask. This application allows users to register and login to their accounts. Users can also create, read, update, and delete blog posts. Additionally, users can update their personal information and profile pictures.

## Features
- **User Authentication**: Register, login, and logout functionality.
- **User Profile Management**: Update username, email, and profile picture.
- **Blog Post Management**: Create, view, edit, and delete blog posts.
- **Responsive Design**: Built with Bootstrap for a clean, simple, and responsive UI

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask WTForms
- Flask Login

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/my_blog.git
    cd my_blog
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set up the database**:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the application**:
    ```sh
    flask run
    ```

## Usage

- **Home Page**: View recent blog posts.
- **Register/Login**: Create an account or log into an existing account.
- **Profile Page**: View and update your profile.
- **Create Post**: Write and publish a new blog post.
- **Edit/Delete Post**: Manage your existing blog posts.

## Folder Structure

my_blog/
├── instance/
│   └── site.db
├── my_blog/
│   ├── __init__.py
│   ├── models.py
│   ├── config.py
│   ├── forms.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── posts/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── account.html
│   │   └── post.html
│   └── static/
│       ├── main.css
│       └── profile_pics/
├── run.py
└── requirements.txt






