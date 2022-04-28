def get_config_rows():
    with open("url_config.txt") as f:
        return f.readlines()


def url_resolver(uri, username):
    return uri.replace("#####", username)
