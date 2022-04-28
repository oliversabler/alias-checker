from engine import alias_checker


def main():
    try:
        alias_checker()
    except Exception as ex:
        print(f"Error occured: {ex}")


if __name__ == "__main__":
    main()

# Todo:
#   - Twitter https://developer.twitter.com/en/docs/labs/tweets-and-users/quick-start/get-users
#   - Snapchat
#   - TikTok
#   - Github
#   - Hackernews
#   - Reddit
