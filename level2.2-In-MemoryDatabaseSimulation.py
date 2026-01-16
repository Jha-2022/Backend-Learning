# Store Regiistered User
# Prevent duplicate emails
# Enforce uniquiness
# Think like a database

users = [
    {"username": "Rishi", "email": "rishi@gmail.com", "password": "Rishi123@", "age": 23}, # Valid -> Stores
    {"username": "Neha", "email": "neha@gmail.com", "password": "Neha123@", "age": 30},   # Valid -> Stores
    {"username": "Rishi2", "email": "rishi@gmail.com", "password": "Rishi222@", "age": 25}, # Duplicate Email -> Fails
    {"username": "Aman", "email": "aman@gmail.com", "password": "aman1234", "age": 10},   # Invalid Age -> Fails
    {"username": "Neha2", "email": "neha@gmail.com", "password": "Neha222@", "age": 28}   # Duplicate Email -> Fails
]

USER_DB = []

def vaidate_username(username):
  if(len(username)<4):
    return "Username must be of atleast 4 characters"
  return None

def validate_email(email):
  if "@" not in email or "." not in email:
    return "Invalid email format"
  return None

def validate_password(password):
  if len(password)<8:
    return "invalid password"
  if not any(char.isdigit() for char in password):
    return "pasword must contain atleast 1 digit"
  return None

def validate_age(age):
  try:
    age = int(age)
    if not (13 < age < 120):
      return "Age must be between 13 and 120"
  except ValueError:
    return  "Envalid Age"

  return None

def email_exists(email):
  for user in USER_DB:
    if user["email"] == email:
      return True
  return False


def register_user(user_date):
  errors = []

  err = validate_useranme(user_data["username"])
  if err: errors.append(err)

  err = validate_email(user_data["email"])
  if err: errors.append(err)

  err = validate_password(user_data["password"])
  if err: errors.append(err)

  err = validate_age(user_data["age"])
  if err: errors.append(err)


  if not any("email" in e for e in errors):
    if email_exists(user_data["email"]):
      errors.append("Email already registered")

  if errors:
    return {
      "sucess": False,
      "user":user_data,
      "errors":errors
    }

USER_DB.append(user_data):
return{
    "sucess":True,
    "message":"User stored"
}


def process_batch(user_list):
  results = {
    "total":len(users_list),
    "stored_users": 0,
    "failed_users": [],
    "database_snapshot":[]
  }

  for user in users_list:
      outcome = register_user(user)

      if outcome["success"]:
        results["stored_users"] += 1

      else:
        results["failed_users"].append({
          "user":outcome["user"],
          "errors": outcome["errors]
        })
  results["database_snapshot"] = USER_DB
  return results



final_output = process_batch(users)
import json
print(json.dump(final_output, indent=2))
