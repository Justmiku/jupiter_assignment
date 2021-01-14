import unittest
from mykhana import Mykhana
from restaurant import Restaurant
from user import User
from item import Item
from order import Order

khana=Mykhana()
class TestFde(unittest.TestCase):

	def test_register(self):
		print('test_restaurant_register')
		limit=2
		Moti_Mahal=Restaurant("Moti Mahal",limit)
		self.assertEqual(khana.register_restaurant(Moti_Mahal), 'restaurant Moti Mahal added')

	def test_user_register(self):
		print('test_user_register')
		Miku=User('Miku',"9122681413","sudhna,jharkhand")
		self.assertEqual(khana.register_user(Miku),'user Miku added')

		suraj=User('suraj',"9122681413","sudhna,jharkhand")
		self.assertEqual(khana.register_user(suraj),'user suraj added')

	def test_user_delete(self):
		print('test_user_delete')
		suraj=User('suraj',"9122681413","sudhna,jharkhand")
		khana.register_user(suraj)
		self.assertEqual(khana.delete_user(suraj),'user removed')




if __name__ == '__main__':
    unittest.main()
