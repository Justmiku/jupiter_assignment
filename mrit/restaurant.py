## Restaurant class which has a name, a menu list, and limit which it can
## process at max at a time
class Restaurant:

	def __init__(self,name,limit):
		self.name = name
		self.limit = limit
		self.menu = []
		self.orders = []
    
    # use the below function to add items to the menu
	def add_menu_item(self, item):
		self.menu.append(item)

	# use the below function to see the menu of the restaurant
	def show_menu(self):
		for itm in self.menu:
			print(itm.name,itm.price, itm.cuisine)

    # Function to update existing menu item
	def update_menu_item(self, item, new_item):
		if item in self.menu:
			self.menu[self.menu.index(item)]= new_item


    # function prints all the orders ordered from this restaurant
	def get_all_orders(self):
		print('Ordered items from the restaurant are: ')
		for ordr in self.orders:
			for itm in ordr.items:
				print(itm.name)

	
