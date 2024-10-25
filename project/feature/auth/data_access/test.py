import unittest
from unittest.mock import MagicMock
from project.feature.auth.data_access.ormsqlachemy import OrmSqlAlchemy
from project.feature.auth.data_access.mock import MockDataAccess
class TestDataAccess(unittest.TestCase):
 def setUp(self):
    real_data_access=OrmSqlAlchemy()
    self.mock_data_access=MockDataAccess(real_data_access)
 def test_create(self):
   email="jawad"
   password="jawad"
   self.mock_data_access.create_auth=MagicMock(return_value={
     "email":"jawad",
     "password":"jawad"
   })
   result=self.mock_data_access.create_auth(email,password)
   self.assertEqual(result["email"],"jawad")
   self.assertEqual(result["password"],"jawad")
   self.mock_data_access.create_auth.assert_called_with(email,password)

if __name__=="__main__":
  unittest.main()


