import unittest
from app import hello

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

  def test_hello(self):
    self.assertEqual(hello(), '{"status": "success"}')

if __name__ == '__main__':
  unittest.main()
