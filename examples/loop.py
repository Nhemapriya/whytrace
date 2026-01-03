from whytrace import why

@why
def process(items, user):
    for i in items:
        if user["active"] and i > 3:
            print("Active user")
        elif user["banned"]:
            print("blocked")
            continue
        else:
            print("skip")


process(
    items=[1, 4, 7],
    user={"active": True, "banned": True},
)
