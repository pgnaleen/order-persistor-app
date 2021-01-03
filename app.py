# [START catalog-reader-app]
from flask import Flask
import pymysql

app = Flask('catalog-reader')

@app.route('/')
def hello():
    connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='ase_assignment')

    requestBody='{"items": ['

    try:
        with connection.cursor() as cursor:
            # Read from database
            sqlQuery = "SELECT item_name, price FROM Catalog"
            cursor.execute(sqlQuery)
            result = cursor.fetchall()

            for row in result:
                 print(row)
                 requestBody += '{"itemName":"'+row[0]+'","itemPrice":'+ str(row[1]) +'},'
    finally:
        connection.close()

    requestBody = requestBody[:-1]
    requestBody += ']}'

    return requestBody

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80)
# [END catalog-reader-app]
