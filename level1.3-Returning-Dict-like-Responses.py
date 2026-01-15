def validate_username(username):
    if len(username) < 4:
        return False, "Username must be at least 4 characters"
    return True, None


def validate_email(email):
    if "@" not in email or "." not in email:
        return False, "Invalid email format"
    return True, None


def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit"
    return True, None


def validate_age(age):
    try:
        age = int(age)
        if not (13 < age < 120):
            return False, "Age must be between 13 and 120"
        return True, None
    except ValueError:
        return False, "Age must be a number"


def register_user(username, email, password, age):
    valid, error = validate_username(username)
    if not valid:
        return {"success": False, "message": error}

    valid, error = validate_email(email)
    if not valid:
        return {"success": False, "message": error}

    valid, error = validate_password(password)
    if not valid:
        return {"success": False, "message": error}

    valid, error = validate_age(age)
    if not valid:
        return {"success": False, "message": error}

    return {"success": True, "message": "User registered successfully"}
