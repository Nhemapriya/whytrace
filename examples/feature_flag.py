from whytrace import why
@why
def show_new_ui(user, flags):
    if flags["new_ui"] and user["beta"] and not flags["maintenance"]:
        print("Show new UI")
    else:
        print("Show old UI")

show_new_ui(
    user={"beta": True},
    flags={"new_ui": True, "maintenance": True}
)
