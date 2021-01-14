
## order class to which requires the user who ordered and the restaurant 
## from where the item was ordered and the actual items ordered
## here user,restaurant and items are are object of user , restaurant and items class

class Order:
	def __init__(self, user, restaurant, items):
		self.user = user
		self.restaurant = restaurant
		self.items = items
		self.status = "Success"

    ## function to check the status of the order 
	def check_status(self):
		return self.status
    ## function to update the status of the order
	def update_status(self, key):
		self.status = key

	