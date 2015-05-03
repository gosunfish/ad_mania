import requests
import xml.etree.ElementTree as ET
# from utils import show_table_metadata
# import mysql.connector

# conn = mysql.connector.connect(user='scott', password='tiger',
#                                  host='127.0.0.1',
#                                  database='employees')
#
#
# cnx = mysql.connector.connect(user='scott', database='employees')
# cursor = cnx.cursor()
#
# tomorrow = datetime.now().date() + timedelta(days=1)
#
# add_employee = ("INSERT INTO employees "
#                "(first_name, last_name, hire_date, gender, birth_date) "
#                "VALUES (%s, %s, %s, %s, %s)")
# add_salary = ("INSERT INTO salaries "
#               "(emp_no, salary, from_date, to_date) "
#               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
#
# data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
#
# # Insert new employee
# cursor.execute(add_employee, data_employee)
# emp_no = cursor.lastrowid
#
# # Insert salary information
# data_salary = {
#   'emp_no': emp_no,
#   'salary': 50000,
#   'from_date': tomorrow,
#   'to_date': date(9999, 1, 1),
# }
# cursor.execute(add_salary, data_salary)
#
# # Make sure data is committed to the database
# cnx.commit()
#
# cursor.close()
# cnx.close()
#
# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# cur = db.cursor()
#
# # Use all the SQL you like
# cur.execute("SELECT * FROM YOUR_TABLE_NAME")
#
# # print all the first cell of all the rows
# for row in cur.fetchall() :
#     print row[0]
# https://linksearch.api.cj.com/v2/link-search?website-id=7782886
#https://linksearch.api.cj.com/v2/link-search?website-id=7782886&advertiser-ids=joined
cjauth = '00aa8d712ad8cabc98c48fb9b2c04102732807d5cc70b0a259a000462f7d4e2b7eae27335c7f953f50cc59920e96592fc610f8cfd6c01c4d4daa801df1a0989cf7/00850f58ad2ef9eceddadcaeea306807bb440de8d5594dd53bcb42ab7f3d6991303ab12ba2fd37cd13ecf29c8b067eac114048c0d2478d533ef8e097add4f0de21'
url = 'https://linksearch.api.cj.com/v2/link-search'
headers = {'authorization': cjauth}
page_number = 2
params = {'website-id': '7782886', 'advertiser-ids': 'joined', 'page-number': page_number, 'records-per-page': 10}

r = requests.get(url, headers=headers, params=params)

#r = requests.get('https://support-services.api.cj.com/v2/link-sizes?',headers=headers)
# print r.text
myxml = r.text

print myxml
print '======================================='


root = ET.fromstring(myxml)
print root.tag
for child in root:
    print child.tag, child.attrib
    for child1 in child:
        print child1.tag, child1.attrib
        for child2 in child1:
            print child2.tag, child2.text

print '****************************************'
for html in root.iter('link-code-html'):
    print html.text

print '++++++++++++++++++++++++++++++++++++++++'
for link in root.iter('link'):
    print link.find('advertiser-id').text
    print link.find('link-id').text
    print link.find('promotion-start-date').text
    print link.find('promotion-end-date').text
    print link.find('link-code-html').text

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
root = ET.fromstring(myxml)
print 'TOTAL MATCHED: ', root.find('links').get('total-matched')






