from order import Order

### Mykhana class which contains a list of all registered restaurant
### list of all users and list of all order objects
class Mykhana:

	def __init__(self):
		self.restaurants = []
		self.users = []
		self.orders = []
    
    ## function registers a new restaurant
	def register_restaurant(self, rest):  
		self.restaurants.append(rest)
		return "restaurant {} added".format(rest.name)

    ## fucntion registers a new user
	def register_user(self, usr):  
		self.users.append(usr)
		return "user {} added".format(usr.name)

    ## function to delete an existing user
	def delete_user(self, usr):
		if usr in self.users:
			self.users.pop(self.users.index(usr))

		return "user removed"
    
    ## function to get all the registered users
	def get_all_user(self):
		for usr in self.users:
			print(usr.name)

    ## function to get all the registered restaurants
	def get_all_restaurant(self):
		for res in self.restaurants:
			print(res.name)

	def search_restaurant(self, key):
		
		for rest in self.restaurants:
			if key == rest.name:       
				return rest

		return None
    

    ## function used to order the food, it needs user , restaruant and the list of items ordered
	def place_order(self, usr, rest, items):

		if rest.limit > 0: ## checks if the number of current order does not exeed the limit of the restaurant
			order = Order(usr,rest,items)
			self.orders.append(order)         

			usr.orders.append(order) ## whenever an order is palced it is added to the particular user order list
			rest.orders.append(order) ## And similarly to the restaurant order list as well
			rest.limit -= 1  ## reduces by 1 when a new order is palaced

			print("Order successfully placed!!")

			return order
		else:
			print("restaurant at limit") ## if limit is full
			return None

    ## fucntion to change the status
	def out_for_delivery(self, order):

		order.update_status("Out for Delivery")

		order.restaurant.limit += 1

	def delivered(self, order):
		order.update_status("Delivered")


