__version__ = '0.0.1'

import argparse
from database_update import DatabaseUpdate
import logging
# logger = logging.getLogger(__name__)
# logger.info(u'Starting AdMania')


# This is where you would use mock to replace database with local data of some sort for testing.
# import database
# database.__call__=lambda x:x


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dblogin", help="Login for mysql database.")
    parser.add_argument("--dbpw", help="Password for mysql database.")
    parser.add_argument("--dbhost", help="Host name for mysql database.")
    parser.add_argument("--cjauth", help="cj affiliate platform authentication code.")
    args = parser.parse_args()
    config = {}
    config['DB_LOGIN'] = args.dblogin
    config['DB_PW'] = args.dbpw
    config['DB_HOST'] = args.dbhost
    config['CJ_AUTH'] = args.cjauth
    return config

def main():
    config = get_config()
    db = DatabaseUpdate(config)
    db.run()


if __name__ == "__main__":
    main()