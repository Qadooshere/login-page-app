# login.py
def login(username, password):
    if username == "admin" and password == "123":
        return "Login successful"
    return "Invalid credentials"

# Example usage
print(login("admin", "123"))
