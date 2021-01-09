import unittest
import requests
import json
from app import hello
from unittest.mock import patch

class TestHelloApp(unittest.TestCase):

#  @classmethod
#  def setUpClass(cls):
#      mysql_my_proc = factories.mysql_proc(port=3306)
#      mysql_my = factories.mysql('mysql_my_proc')

#      cls.mysql = MYSQLD_FACTORY()
#      cls.db_conn = create_engine(cls.mysql.url()).connect()

#  def setUp(self):
#      self.mysql.start()
#      self.db_conn.execute("""CREATE TABLE `foo` (blah)""")

#  def test_hello(self):
#    self.assertEqual(hello(), '{"status": "success"}')

  @patch('requests.post')
  def test_post(self, mock_post):
      info = {"user_id": "value1", "items": "value2", "total_price": 5400}
      resp = requests.post("localhost:80", data=json.dumps(info), headers={'Content-Type': 'application/json'})
      mock_post.assert_called_with("localhost:80", data=json.dumps(info), headers={'Content-Type': 'application/json'})

if __name__ == '__main__':
  unittest.main()
