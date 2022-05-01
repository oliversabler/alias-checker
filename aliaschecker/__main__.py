def main():
    try:
        from aliaschecker.engine import alias_checker

        alias_checker()
    except Exception as ex:
        print(f"Error occured: {ex}")


if __name__ == "__main__":
    import sys

    sys.exit(main())

# Todo:
#   - Twitter https://developer.twitter.com/en/docs/labs/tweets-and-users/quick-start/get-users
#   - Snapchat
#   - TikTok
#   - Github
#   - Hackernews
#   - Reddit
