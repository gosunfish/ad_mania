from ad_mania import app
from flask import url_for, redirect, render_template, request, Markup
from mysql.connector import MySQLConnection, Error
import json
import logging

logger = logging.getLogger(__name__)


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('ads'))


@app.route('/ads', methods=['GET'])
def ads():
    website = request.args.get('website', 'earthtravelers.com')
    user = app.config['DB_LOGIN']
    password = app.config['DB_PW']
    host = app.config['DB_HOST']
    database = app.config['DB_NAME']

    conn = MySQLConnection(user=user, password=password, host=host, database=database)
    conn.autocommit = True
    cursor = conn.cursor()
    args = (website,)
    try:
        cursor.callproc('AdMania.prc_GetAds', args)
    except Error as e:
        print e

    # In order to handle multiple result sets being returned from a database call,
    # mysql returns results as a list of lists.
    # Therefore, even if there is only one result set, you still have to get it from the list of lists.
    for result in cursor.stored_results():
        row_set = result.fetchall()

    result_set = []
    for row in row_set:
        result_set.append(row[0].decode().replace('##DOMAIN_ID##', '7782886'))

    cursor.close()
    conn.close()

    return render_template('T1.html',resultsSET=result_set)



