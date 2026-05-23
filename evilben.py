#we are learning about if and else statements in python and how to use them in a real life situation. We are going to create a simple coffee shop program that will take the customer's name, their order, and the quantity of their order, and then calculate the total price of their order. We will also use if and else statements to check if the customer's order is valid and if they have enough money to pay for their order. Let's get started!

print("Hello welcome to Coffe zone ")

name = input("What is your name?\n")

if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "yes" :
     print("You're not welcome here Evil Ben !! Get Out!!! ")
     exit()
    else :
      print("Oh , so you're one of those good Bens. Come on in!!!")
else:
    print("Hello " + name + ",thank you so much for coming in today.\n\n\n")







#if name == "Ben":
    #print("You're not welcome here Evil Ben !! Get Out!!! ")
    #choice_1 = input("Are you evil or nice?")
    #if choice_1 == "evil":
        #print("Bye bye Israel")
    #else:
       # print("Sorry boyz")    
#elif name == "Ben" and choice_1 == "nice" or name != "Ben":
   # print("Hello" + name + ",thank you so much for coming in today.\n\n\n")














