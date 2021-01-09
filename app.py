# [START order-persistor-app]
from flask import Flask
from flask import request
import pymysql

app = Flask('order-persistor')

@app.route('/', methods = ['POST'])
def hello():
    payload = request.get_json()
    connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='root',
                             db='ase_assignment')
    print(payload)

    try:
        with connection.cursor() as cursor:
            sqlQuery = "INSERT INTO Orders VALUES ('"+ payload['user_id'][0:10] +"', '"+ payload['user_id'][0:10] +"', '"+ payload['items'] +"', "+ str(payload['total_price']) +", null);"
            cursor.execute(sqlQuery)

        connection.commit()
    finally:
        connection.close()

    return '{"status": "success"}'

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80)
# [END order-persistor-app]
