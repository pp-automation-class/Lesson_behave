
# Homework

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False

    def authenticate(self):
        # just for demo: password must be "12345"
        if self.password == "12345":
            self.logged_in = True
            print(f"{self.username} logged in successfully.")
        else:
            print("Invalid credentials.")


class AdminLogin(Login):
    def authenticate(self):
        if self.password == "admin":
            self.logged_in = True
            print(f"Admin {self.username} logged in with full access.")
        else:
            print("Admin login failed.")


class UserLogin(Login):
    def authenticate(self):
        if self.password == "user":
            self.logged_in = True
            print(f"User {self.username} logged in with limited access.")
        else:
            print("User login failed.")


# --- Usage ---
admin = AdminLogin("Alice", "admin")
admin.authenticate()

user = UserLogin("Bob", "user")
user.authenticate()

guest = Login("Charlie", "12345")
guest.authenticate()
