#lets start a coffe shop together! we are going to build a coffee shop using some python stuff

#lets build a robot barista

print("Hello, welcome to Zeina coffee!!!!!!!")

#lets ask the user what their name is 
name = input("What is your name?\n")

print("Hello " + name + ", thank you so much for coming in today!")

menu = "Camel milk tea, Espresso, Cow Milk tea, Latte, Mocha , Cappucinuo, Frappucino "

print(name + ", what would you like from our menu today? We have.\n \n \n \n" + menu)

order = input("Please enter your order here: \n")

if order == "Frappucino" :
    price = 13
elif order == "Camel milk tea" :
    price = 10
elif order == "Espresso" :
    price = 9  
elif order == "Latte" :
    price = 7
    cream = input("Would you like to add Whipped cream to your latte? \n")

    if cream.lower() == "yes" :
        price = 11
    else:
        price = 7
elif order == "Mocha" :
    price = 11
elif order == "Cow Milk tea" :
    price = 4
elif order == "Cappucinuo" :
    price = 6


quantity = input("How many " + order + " would you like? \n")

print("The price of one  " + order + " is " + str(price))

total = price * int(quantity)

print("Thank you.Your total is: $" + str(total))

print("Sounds good! " + name + ",we'll have your " + quantity + " " + order + " ready for you in a moment!")

