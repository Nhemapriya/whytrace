from whytrace import why

@why
def counter_demo():
    count = 0
    for _ in range(3):
        count += 1
        if count > 1:
            print("Threshold reached")

counter_demo()
