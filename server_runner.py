from web.app import app


def main():
    print("Starting web server on localhost and port 8080...")
    app.run(host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()
