from whytrace import why

@why
def access_api(request):
    if not request["authenticated"]:
        print("401 Unauthorized")
    elif request["rate_limited"] and not request["internal"]:
        print("429 Too Many Requests")
    elif request["internal"] or request["role"] == "service":
        print("Access granted")
    else:
        print("403 Forbidden")


access_api(
    request={
        "authenticated": True,
        "rate_limited": True,
        "internal": False,
        "role": "service",
    }
)
