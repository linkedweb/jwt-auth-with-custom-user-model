# Django JWT Authentication with Custom User Model Example

This is a simple project to help demonstrate setting up jwt authentication with a custom user model.

In order to test out this project:

- clone the repository
- run: python3 -m venv venv
- then activate the virtual environment: source venv/bin/activate (MacOS) or .\venv\Scripts\activate.bat (Windows)
- run: pip install -r requirements.txt
- run: python manage.py migrate
- run: python manage.py runserver

Then you can open up postman to test creating and retrieving a user:

- localhost:8000/api/accounts/create with a POST request will create a user
  - you will need to pass the following data to the request: first_name, last_name, email, password
- localhost:8000/api/accounts/user with a GET request will retrieve the user
  - you will first need to hit localhost:8000/api/token/ with a POST request passing the email and password to get an access token
  - then you can pass an authorization header in the /api/accounts/user request to retrieve the user, the header will look like the following:
    - Authorization: Bearer your_access_token_value
