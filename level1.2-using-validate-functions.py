def validate_username(username):
    username = str(username)
    if(len(username) < 4):
        return False, "Username must be at least 4 characters"
    else:
        return True, None 
    
def validate_email(email):
    if("@" not in email or "." not in email):
        return False, "Invalid email format"
    else:
        return True, None
        
def validate_password(password):
    if(len(password) < 8):
        return False, "password must be of 8 characters atleast"
    elif not any(char.isdigit() for char in password):
        return False, "Password must be at least 8 characters and contain a digit"
    else:
        return True, None 
 
def validate_age(age):
    try:
        age = int(age)
        if not(13 < age < 120):
            return False, "Invalid age"
        else:
            return True, None 
    except ValueError:
          return False, "Invalid age"
          
          
def register_user(username, email, password, age):
    valid, error = validate_username(username)
    if not valid:
        print(error)
        return
    
    valid, error =  validate_email(email)
    if not valid:
        print(error)
        return
        
    valid, error = validate_password(password)
    if not valid:
        print(error)
        return
        
    valid, error = validate_age(age)
    if not valid:
        print(error)
        return
        
    print("User registered successfully")
    
register_user("Rishi", "rishijha0910@gmail.com", "Rishi1234@", 20)
