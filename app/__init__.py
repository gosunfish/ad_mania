__version__ = '0.0.1'

import argparse
from flask import Flask


# This is where you would use mock to replace database with local data of some sort for testing.
# import database
# database.__call__=lambda x:x

# This 'app' is a variable containing an instance of Flask
app = Flask(__name__)


def application():
    parser = argparse.ArgumentParser()
    parser.add_argument("--esconn", help="Elastic Search Connection String")
    args = parser.parse_args()
    app.config["ES"]=args.esconn

    return app


def main():
    app = application()
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()