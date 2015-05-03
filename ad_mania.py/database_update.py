from config import Config
import logging
import xml.etree.ElementTree as ET
import mysql.connector
import requests

logger = logging.getLogger(__name__)

def shred_result(result_xml):
    result_dict = dict()
    root = ET.fromstring(result_xml)
    result_dict['records_returned'] = root.find('links').get('records-returned')
    return result_dict

def database_update():

    config=Config().config
    user = config['DB_LOGIN']
    password = config['DB_PW']
    host = config['DB_HOST']
    database = config['DB_NAME']
    cjauth = config['CJ_AUTH']
    cjurl = config['CJ_URL']

    conn = mysql.connector.connect(user=user, password=password, host=host, database=database)

    page_number = 0
    records_per_page = 100 # this is the max number allowed by the affiliate api per call.
    records_returned = records_per_page
    headers = {'authorization': cjauth}

    while records_returned == records_per_page:
        page_number += 1
        params = {'website-id': '7782886', 'link-type': 'banner', 'advertiser-ids': 'joined', 'page-number': page_number, 'records-per-page': records_per_page}

        result_xml = requests.get(cjurl, headers=headers, params=params)

        root = ET.fromstring(result_xml)
        records_returned = root.find('links').get('records-returned')

        for link in root.iter('link'):
            mysql_args = (
                link.find('advertiser-id').text,
                link.find('link-id').text,
                link.find('promotion-start-date').text,
                link.find('promotion-end-date').text,
                link.find('link-code-html').text)



if __name__ == '__main__':
    database_update()
# import sys
# print sys.path
#         cnx = mysql.connector.connect(user=self.config['dwlogin'], database='AdMania')
#         cursor = cnx.cursor()

# http://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html