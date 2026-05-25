#we are learning logical operators like not and and or 

#we hate israel USA and hungary hadi kama oban ametolea

print("Hi welcome to Carniege Melon University!\n" )

name = input("What is you name?\n")
nationality = input("what is your nationality?\n")


if nationality in ["Israeli", "American", "Hungarian"]:
    Gaza = input("Do you support Palestine?\n").lower()
    good_deeds = int(input("How many good deeds have you done?\n")) 
    if Gaza == "no"  and  good_deeds < 5 :
        print("Go find somewhere else to study you prat!!!!!!!\n")
    else:
        print("Thats nice " + name + ", so you are one of those good " + nationality + ". We will review your documents and contact you")
else:
    print("We will look through your application and we will contact you when we are done reviewing you documents")