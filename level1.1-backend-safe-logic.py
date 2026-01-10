def register_user(username, email, password, age):
    if (len(username) < 4):
        print("Username must be of least 4 characters")
    
    elif("@" not in email or "." not in  email):
        print("Email is not valid")
    
    elif(len(password) < 8):
        print("Password must be of least 8 characters")
    
    elif not any(char.isdigit() for char in password):
        print("not valid passwored")
    
    try:  #used try-except with changing the data type of age variable to integer no matter if its float or boolean they would be changed but others can't be
        age = int(age)
        if not(13 < age < 120):
            print("age not permitted")
    except ValueError:
        print("Age must be a valid number")
        return
        
    else:
        print("User registered successfully")




# Fail-Fast Logic

# Validation stops at first failure

# Clear error messages

# No crashes

# No undefined behavior
