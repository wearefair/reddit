from reddit.server import create_app


def main():
    reddit = create_app()
    reddit.init()
    reddit.run()


if __name__ == '__main__':
    main()
