
# Validation service

# Registration service

# Response formatter


# Validation logic reused from previous steps
def validate_username(username):
    if len(str(username)) < 4:
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
        return False, "Password must contain a digit"
    return True, None

def validate_age(age):
    try:
        age_val = int(age)
        if not (13 < age_val < 120):
            return False, "Age not permitted"
        return True, None
    except (ValueError, TypeError):
        return False, "Age must be a valid number"

# Level 2.1 Implementation
def process_batch_users(user_list):
    success_list = []
    failure_list = []

    for user in user_list:
        errors = []
        
        # Run all validations and collect all errors for the user
        v_user, err_u = validate_username(user.get("username", ""))
        if not v_user: errors.append(err_u)
            
        v_email, err_e = validate_email(user.get("email", ""))
        if not v_email: errors.append(err_e)
            
        v_pass, err_p = validate_password(user.get("password", ""))
        if not v_pass: errors.append(err_p)
            
        v_age, err_a = validate_age(user.get("age", 0))
        if not v_age: errors.append(err_a)

        # Categorize user based on error collection
        if not errors:
            success_list.append(user)
        else:
            failure_list.append({
                "user": user,
                "errors": errors
            })

    # Return structured summary
    return {
        "total": len(user_list),
        "success_count": len(success_list),
        "failure_count": len(failure_list),
        "successful_users": success_list,
        "failed_users": failure_list
    }

# Input Data
users = [
    {"username": "Rishi", "email": "rishi@gmail.com", "password": "Rishi123@", "age": 23},
    {"username": "An", "email": "an@gmail.com", "password": "An123@", "age": 20},
    {"username": "Kunal", "email": "kunalgmail.com", "password": "Kunal@", "age": 25},
    {"username": "Aman", "email": "aman@gmail.com", "password": "aman1234", "age": 10},
    {"username": "Neha", "email": "neha@gmail.com", "password": "Neha123@", "age": 30}
]

# Execute and Print Result
import json
result = process_batch_users(users)
print(json.dumps(result, indent=4))
