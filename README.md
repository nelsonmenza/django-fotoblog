# Django Photo Blog

This project is a simple Photo Blog built with Django, designed for the main purpose of understanding and learning the Django web framework.

## Description

The Django Photo Blog project is a web application that allows users to sign up, upload profile photos, share photo blog entries, and interact with other users. It emphasizes core Django concepts, user authentication, and image upload functionalities, as well as creating, viewing, and editing blog posts.

**Please note:** This project is still a work in progress, and additional functionality and improvements are planned for the future. This project is based on the OpenClassrooms course: https://openclassrooms.com/en/courses/7107341-intermediate-django.

## Features

- User Registration: Users can create an account by providing their credentials.
- User Authentication: Secure authentication is implemented using Django's built-in authentication system.
- Profile Photo Upload: Registered users can upload their profile photos.
- Blog Entry Creation: Users can create blog entries, each associated with a photo.
- Home Page: The home page displays a collection of photos and blog entries.
- Photo Upload: Users can upload photos and associate them with blog entries.
- Edit and Delete Blog Entries: Users can edit or delete their blog entries.

## Installation and Setup

1. Clone the project repository to your local machine:

   ```bash
   git clone [repository_url]
   ```

2. Navigate to the project directory:

   ```bash
   cd [Project Directory]
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

4. Install project dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

**Note:** Keep in mind that this project is still under development, and more features will be added in the future.

## Usage

- Visit the project's main page and register a new account or log in using an existing one.
- Upload a profile photo for your user account.
- Create and share blog entries, each associated with a photo.
- View and edit your blog entries.
- Stay tuned for more updates and functionality as the project continues to evolve.

## Project Structure

- **`authentication`**: Django app for user authentication and profile photo upload.
- **`blog`**: Django app for creating, viewing, and editing blog entries and photo uploads.
- **`media`**: Directory for storing user-uploaded photos.
- **`static`**: Directory for CSS and other static files.
- **`templates`**: Contains HTML templates used for rendering views.
- **`forms.py`**: Contains the forms used for user registration, profile photo upload, blog entry creation, and photo uploads.
- **`models.py`**: Defines the data models for users, blog entries, and photos.
- **`urls.py`**: Defines URL patterns for both the authentication and blog apps.
- **`views.py`**: Contains view functions for user registration, profile photo upload, blog creation, photo upload, blog viewing, and blog editing.
- **`fotoblog`**: Project directory containing settings and configuration files.

By including the "media" and "static" directories in the project structure, users can upload photos and access static resources like CSS files. The "fotoblog" project directory contains the project-specific settings and configuration. Please ensure that the necessary Django settings for media and static files are properly configured in your project's settings.
