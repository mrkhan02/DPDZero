
# Backend system 

This project demonstrates how to create APIs for custom user authentication using JWT (JSON Web Token).

## Table of Contents

- [Project Overview](#project-overview)
- [DB Schema](#db-schema)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Project Overview

This project provides a basic setup for a Django Rest Framework project with custom user authentication using JWT. It includes the following features:

- Custom User Model for registration and authentication.
- JWT token-based authentication.
- API endpoints for user registration, login, and protected resource access.
- CRUD APIs for managing items.

## DB Schema
```
+-------------------------+     +-----------------------+
|         User            |     |        Item           |
+-------------------------+     +-----------------------+
| id         (PK)         |     | id            (PK)    |
| username                |     | key                   |
| email                   |     | value                 |
| full_name               |     +-----------------------+     
| age                     |     
| gender                  |     
| password                |
+-------------------------+

```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mrkhan02/DPDZero.git
   cd DPDZero
   
2. Create a virtual environment and activate it:

    ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install project dependencies:
    ```bash
    pip install -r requirements.txt
4. Configure my.cnf
    ```bash
    database = **
    user = **
    password = **
    default-character-set = utf8

    replace ** with your credential 

5. Apply database migrations:
    ```bash
    python manage.py migrate
6. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
7. Run the development server:
    ```bash
    python manage.py runserver

## Usage

1. Register a user using the registration API endpoint.
2. Obtain an access token by logging in using the login API endpoint.
3. Use the access token for protected API endpoints.
4. Explore and interact with the CRUD APIs for managing Data.

### API Documentation
 - Registration API: /api/register/
-  Token API: /api/token/
- Access token is required for protected endpoints.
- Data APIs: /api/data/
Refer to the [API Documentation](https://dpdzero.notion.site/Take-home-assignment-Software-Developer-a1354d18891744fa9fc84815f040c76d#694d7900382a43fbbe54bafa95e2628a) for more details about available endpoints and their usage.
