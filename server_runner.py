from web.app import app


def main():
    print("Starting web server on port 8080...")
    app.run(port=8080)


if __name__ == '__main__':
    main()
