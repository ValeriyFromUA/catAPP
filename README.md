![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Django](https://img.shields.io/badge/Django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)


# CatAPP

This is a web application inspired by Instagram, but with a focus on cats. Users can upload pictures of their favorite cats, view other users' photos, like them, and delete their own posts.

Technologies
The application is developed using:

- Django
- SQLite
- Bootstrap


## Installation

1. Clone the repository to your local machine: ```https://github.com/ValeriyFromUA/catAPP.git```
2. Create a virtual environment
3. Install the required packages by running: ``` poetry install ```
4. Createdatabase and update the DATABASES configuration in settings.py, add Your ```SECRET_KEY``` in .env file
5. Apply the database migrations.
6. Start the development server: ```python manage.py runserver```
7. Open your browser and go to ```http://localhost:8000/``` to access the application.

That's it! You should now be able to use CatAPP to share and view pictures of cats.
