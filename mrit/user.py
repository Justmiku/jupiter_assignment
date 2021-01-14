from mykhana import Mykhana
## user class that has a name of the user , phone number of the user and the 
## address of the user
class User:
	def __init__(self, name, phone, address):
		self.name = name
		self.phone = phone
		self.address = address
		self.orders = []

	def get_user(self):
		return {"name": self.name, "phone":self.phone, "address":self.address}

	def update_user(self,name=None,phone=None,address=None):
		if name:
			self.name = name

		if phone:
			self.phone = phone

		if address:
			self.address = address

    ## Function prints all the items ordered by a user
	def get_all_orders(self):
		print('Items ordered by the user are:')
		for ordr in self.orders:
			for itm in ordr.items:
				print(itm.name)
