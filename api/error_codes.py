

INVALID_REQUEST={
    "status": "error",
    'code':'INVALID_REQUEST',
    'message':'Invalid request. Please provide all required fields: username, email, password, full_name.'
}

USERNAME_EXISTS={
    "status": "error",
    'code':'USERNAME_EXISTS',
    'message':'The provided username is already taken. Please choose a different username.'
}

EMAIL_EXISTS={
    "status": "error",
    'code':'EMAIL_EXISTS',
    'message':'The provided email is already registered. Please use a different email address.'
}

INVALID_PASSWORD={
    "status": "error",
    'code':'INVALID_PASSWORD',
    'message':'The provided password does not meet the requirements. Password must be at least 8 characters long and contain a mix of uppercase and lowercase letters, numbers, and special characters.'
}

INVALID_AGE={
    "status": "error",
    'code':'INVALID_AGE',
    'message':'Invalid age value. Age must be a positive integer.'
}

GENDER_REQUIRED={
    "status": "error",
    'code':'GENDER_REQUIRED',
    'message':'Gender field is required. Please specify the gender (e.g., male, female, non-binary).'
}

INTERNAL_SERVER_ERROR={
    "status": "error",
    'code':'INTERNAL_SERVER_ERROR',
    'message':'An internal server error occurred. Please try again later.'
}

INVALID_CREDENTIALS={
    "status": "error",
    'code':'INVALID_CREDENTIALS',
    'message':'Invalid credentials. The provided username or password is incorrect.'
}

MISSING_FIELDS={
    "status": "error",
    'code':'MISSING_FIELDS',
    'message':'Missing fields. Please provide both username and password.'
}

INTERNAL_ERROR={
    "status": "error",
    'code':'INTERNAL_ERROR',
    'message':'Internal server error occurred. Please try again later.'
}

INVALID_KEY={
    "status": "error",
    'code':'INVALID_KEY',
    'message':'The provided key is not valid or missing.'
}

INVALID_VALUE={
    "status": "error",
    'code':'INVALID_VALUE',
    'message':'The provided value is not valid or missing.'
}

KEY_EXISTS={
    "status": "error",
    'code':'KEY_EXISTS',
    'message':'The provided key already exists in the database. To update an existing key, use the update API.'
}


INVALID_TOKEN={
    "status": "error",
    'code':'INVALID_TOKEN',
    'message':'Invalid access token provided'
}

KEY_NOT_FOUND={
    "status": "error",
    'code':'KEY_NOT_FOUND',
    'message':'The provided key does not exist in the database.'
}