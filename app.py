# [START order-persistor-app]
from flask import Flask
import pymysql

app = Flask('order-persistor')

@app.route('/', methods = ['PUT'])
def hello():
    connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='ase_assignment')

    try:
        with connection.cursor() as cursor:
            sqlQuery = "INSERT INTO Orders VALUES ('order_id_1', 'user_id_1', 'Toothbrush,soap,wallet', 150, null)"
            cursor.execute(sqlQuery)
            #result = cursor.fetchall()

    finally:
        connection.close()

    return '{"status": "success"}'

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80)
# [END order-persistor-app]
