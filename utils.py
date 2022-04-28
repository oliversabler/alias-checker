def get_endpoints():
    with open("endpoints.txt") as f:
        return f.readlines()


def url_resolver(uri, username):
    return uri.replace("#####", username)
