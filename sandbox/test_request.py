import requests
import xml.etree.ElementTree as ET



url = 'https://linksearch.api.cj.com/v2/link-search'
headers = {'authorization': '00aa8d712ad8cabc98c48fb9b2c04102732807d5cc70b0a259a000462f7d4e2b7eae27335c7f953f50cc59920e96592fc610f8cfd6c01c4d4daa801df1a0989cf7/00850f58ad2ef9eceddadcaeea306807bb440de8d5594dd53bcb42ab7f3d6991303ab12ba2fd37cd13ecf29c8b067eac114048c0d2478d533ef8e097add4f0de21'}
params = {'website-id': '7782886', 'keywords': '250x250', 'link-type': 'banner', 'advertiser-ids': 'joined'}

r = requests.get(url, headers=headers, params=params)

#r = requests.get('https://support-services.api.cj.com/v2/link-sizes?',headers=headers)
print r.text

# import sys
# print sys.path


