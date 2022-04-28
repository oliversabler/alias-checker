import requests
from utils import get_config_rows, url_resolver


def get_username_input():
    # Todo: Handle bad input
    print("Input username:", end=" ")
    return input()


def alias_checker():
    username = get_username_input()
    config_rows = get_config_rows()
    for row in config_rows:
        name, url = row.split(";")
        r = requests.get(url_resolver(url, username))
        # Todo: Return result in a pretty way
        if r.status_code == requests.codes.not_found:
            print(f"Username: {username} is available @ {name}")
        else:
            print(f"Username: {username} is not available @ {name}")
