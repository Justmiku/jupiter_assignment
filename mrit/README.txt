The whole project has been done in python 3.7 using object oriented design principle and to write test unittest library of python has been used.

There are 5 different classes namely:
1. item :- contains details of the food item such as name, price etc

2. user :- contains the details of the user who will order food , it contains 
           information related to user such as name , phone number,order details and address.

           this class has methods which are used to get_user, update_user,and get_all_ordered items by the user

3. restaurant :- contains the details of the restaurant such as name, menu 
                 list, order list and limit of the restaurant.
                 The class has methods which are for add_menu_items, show_menu , update_menu and get_all_orders

4. order :- this class is used to create order object which has user name , 
            restaurant name and the items ordered

5. Mykhans :- this is the main class which uses the properties of many
              classes and has all the important functinality such as register restaurant , register user and order food etc


main.py file is the main file which is handled by admin where a restaurant can be added, user can be added and the status of the food items can be changed , in it all the functionlity has been implemented.

HOW TO RUN THE CODE

1. save all the 7 .py file and run main.py , it has already many fucntionlity implemented which were asked. Looking at the output of the code makes things more clear.

2. main.py is highly commented and it has different section to test different fucntionality.



*******	 OUTPUT OF THE MAIN.PY FILE  *********

restaurant Moti Mahal added
restaurant jain foods added
restaurant Novelty added
 
user Miku added
user suraj added
user sanay added
 
{'name': 'Miku', 'phone': '9122681413', 'address': 'sudhna,jharkhand'}
 
 
This is the list of all the restaurants
Moti Mahal
jain foods
Novelty
 
 
This is the list of all the users
Miku
suraj
sanay
 
naan 30 indian
chicken 250 indian
panner 200 indian
panner kadhai 210 indian
palak panner 180 indian
Order successfully placed!!
Order successfully placed!!
Order successfully placed!!
restaurant at limit
 
Items ordered by the user are:
naan
panner
Burger
Sandwich
 
Ordered items from the restaurant are: 
naan
panner
chicken
palak panner
Success
None
Out for Delivery
None
Delivered
Order successfully placed!!
[Finished in 0.2s]