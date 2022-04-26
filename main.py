import requests


def main():
    # Todo:
    # 1. Wait for input
    #    - Handle bad input
    print("Input username:", end=" ")
    username = input()

    # 2. Create engine which checks different sites for username
    #    - Read file with urls and loop through
    # 3. Return result in a pretty way
    try:
        r = requests.get(f"https://www.instagram.com/{username}/?__a=1")
        if r.status_code == requests.codes.not_found:
            print(f"Username: {username} is available")
        else:
            print(f"Username: {username} is not available")
    except Exception as ex:
        print(f"Error occured: {ex}")


if __name__ == "__main__":
    main()
