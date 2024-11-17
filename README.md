# Forum Application

A simple forum application built using Flask for the backend, HTML for the structure, and CSS for styling. This application allows users to register, log in, create posts, like posts, delete posts, and update their profiles.

## Features

- User Registration
- User Login
- Create Posts
- Like Posts
- Delete Posts
- Update Profile

## Requirements

- Python 3.x
- Flask

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/forum-app.git
    cd forum-app
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install Flask
    ```

## Running the Application

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to access the forum application.

## Project Structure


## File Descriptions

- **app.py**: The main Flask application file containing routes and logic.
- **static/style.css**: CSS file for styling the application.
- **templates/home.html**: Template for the home page.
- **templates/register.html**: Template for the registration page.
- **templates/login.html**: Template for the login page.
- **templates/dashboard.html**: Template for the dashboard page.
- **README.md**: This README file.

## Usage

### Registration

1. Navigate to the registration page by clicking "Register" on the home page.
2. Fill out the registration form and submit to create a new account.

### Login

1. Navigate to the login page by clicking "Login" on the home page.
2. Fill out the login form and submit to log in to your account.

### Creating Posts

1. After logging in, navigate to the dashboard.
2. Fill out the post form and submit to create a new post.

### Liking Posts

1. On the dashboard, click the "Like" button next to a post to like it.

### Deleting Posts

1. On the dashboard, click the "Delete" button next to a post to delete it.

### Updating Profile

1. You can add a form or link on the dashboard to navigate to a profile update page (not included in the basic setup but can be added).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

