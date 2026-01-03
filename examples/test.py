from whytrace import why

@why
def check_user(user):
    if user["is_active"] and user["age"] > 18:
        if user["age"] > 21:
            return "ALLOW"
    else:
        return "DENY"

result = check_user({"is_active": False, "age": 16})
print("Result:", result)