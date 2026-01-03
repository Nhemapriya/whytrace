from whytrace import why

@why
def access_control(user, resource):
    if user["active"]:
        if resource["public"]:
            print("Access granted")
        elif user["role"] == "admin":
            print("Admin access")
        else:
            print("Access denied")
    else:
        print("Inactive user")

access_control(
    user={"active": True, "role": "user"},
    resource={"public": False}
)
