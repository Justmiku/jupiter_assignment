

# here write all the scenarios 

#like create a mykhana object and add restaurants and users; perform an order placement, track and update order status

from mykhana import Mykhana
from restaurant import Restaurant
from user import User
from item import Item
from order import Order

khana=Mykhana()


## Register your restaurant here
##----------------------------*********-----------------------------
## 1. create restaurant object from restaruant

limit=2
Moti_Mahal=Restaurant("Moti Mahal",limit)

## 2. Add the items to menu


naan=Item('naan',30,'indian')
Moti_Mahal.add_menu_item(naan)

chicken=Item('chicken',250,'indian')
Moti_Mahal.add_menu_item(chicken)

panner=Item('panner',200,'indian')
Moti_Mahal.add_menu_item(panner)

panner_kadhai=Item('panner kadhai',210,'indian')
Moti_Mahal.add_menu_item(panner_kadhai)

palak_panner=Item('palak panner',180,'indian')
Moti_Mahal.add_menu_item(palak_panner)

## register the restaurant
print(khana.register_restaurant(Moti_Mahal))




## Add new restaurant

limit=3
Jain_Foods=Restaurant("jain foods",limit)

## Add menu items
Dosa=Item('Dosa',50,'indian')
Jain_Foods.add_menu_item(Dosa)

Burger=Item('Burger',60,'western')
Jain_Foods.add_menu_item(Burger)

Sandwich=Item('Sandwich',70,'western')
Jain_Foods.add_menu_item(Sandwich)

Milk_shake=Item('Milk_shake',30,'indian')
Jain_Foods.add_menu_item(Milk_shake)

Golgappe=Item('Golgappe',20,'indian')
Jain_Foods.add_menu_item(Golgappe)

## Register the restaurant
print(khana.register_restaurant(Jain_Foods))



## Add new restaurant
limit=4
Novelty=Restaurant("Novelty",limit)

Chicken_pot_pie=Item('Chicken pot pie',250,'indian')
Novelty.add_menu_item(Chicken_pot_pie)

Fried_chicken=Item('Fried chicken',160,'western')
Novelty.add_menu_item(Fried_chicken)

Chicken_soup=Item('Chicken soup',70,'indian')
Novelty.add_menu_item(Chicken_soup)

Meatloaf=Item('Meatloaf',130,'western')
Novelty.add_menu_item(Meatloaf)

Lasagna=Item('Lasagna',200,'western')
Novelty.add_menu_item(Lasagna)

## Register the restaurant

print(khana.register_restaurant(Novelty))





##----------------------------*********-----------------------------

## Register user here
print(' ')

Miku=User('Miku',"9122681413","sudhna,jharkhand")
print(khana.register_user(Miku))


suraj=User('suraj','8920345689','gujrat')
print(khana.register_user(suraj))

sanay=User('sanay','123456789','dhanbad,jharkhand')
print(khana.register_user(sanay))




##----------------------------*********-----------------------------

## Get user details here
print(' ')
print(Miku.get_user())
print(' ')


##----------------------------*********-----------------------------
## Get list of all restaurants here 
print(' ')
print("This is the list of all the restaurants")
khana.get_all_restaurant()
print(' ')

##----------------------------*********-----------------------------
## Get list of all users here
print(' ')
print("This is the list of all the users")
khana.get_all_user()
print(' ')


##----------------------------*********-----------------------------
## Get menu of a restaurant
Moti_Mahal.show_menu()
# Novelty.show_menu()


##----------------------------*********-----------------------------
## order food here

items=[naan,panner]
ord1=khana.place_order(Miku,Moti_Mahal,items)
items=[Burger,Sandwich]
ord2=khana.place_order(Miku,Jain_Foods,items)
items=[chicken,palak_panner]
ord3=khana.place_order(sanay,Moti_Mahal,items)

## By upper order the order limit of Moti_mahal is complete so it cannot accept more orders
items=[panner_kadhai]
khana.place_order(suraj,Moti_Mahal,items)



##----------------------------*********-----------------------------
## User can see all the food it has ordered
print(' ')
Miku.get_all_orders()


##----------------------------*********-----------------------------
## Restaruant can see all the ordered food
print(' ')
Moti_Mahal.get_all_orders()

## check the status and change the status of the orders
print(ord1.check_status())
print(khana.out_for_delivery(ord1))
print(ord1.check_status())
print(khana.delivered(ord1))
print(ord1.check_status())
##  Now since the order is delivered the order limit of moti_mahal is reduced by one
## and thus it can now accept orders which we can see from below code.

items=[panner_kadhai]
khana.place_order(suraj,Moti_Mahal,items)


