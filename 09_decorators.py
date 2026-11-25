# Scenario: A college portal logs access to a protected student dashboard.
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            return "Access denied: please log in"
        return func(user, *args, **kwargs)
    return wrapper

@login_required
def view_dashboard(user):
    return f"Welcome, {user['name']}!"

print(view_dashboard({"name": "Asha", "logged_in": True}))
print(view_dashboard({"name": "Guest", "logged_in": False}))
