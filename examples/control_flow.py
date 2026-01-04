from whytrace import why

@why
def early_exit(items):
    for i in items:
        if i < 0:
            break
        print(i)

early_exit([1, 2, -1, 4])
