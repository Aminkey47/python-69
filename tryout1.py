print("Hello welcome to Aminkey Coffee Shop")

name = input("What's is your name?\n")

print("Holaaa " + name + ",thank you so much for coming to our coffee shop")

menu = ("Espresso , mocha , latte ,  banana tea , shah kawow , Cappucino , bilalilim")

print(name + ",what would you like from our menu today? We have:\n \n \n \n" + menu)

order = input("Please enter your order here: \n")

price = 8

quantity = input("How many  " + order + "  would you like \n")

total = price * int(quantity)

print("Sounds Great " + name + ",we'll have your " + quantity + " " + order + " ready for you in a moment")

print("Your total is:$" + str(total) )

