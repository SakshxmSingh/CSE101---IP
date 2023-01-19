x = input("Did you qualify for jee adv? (yes/no) ")
if x.lower() == "yes":
    y = int(input("Enter jee adv rank: "))
    if y < 2000:
        print("Congrats! You get iit-d")
    else:
        print("You dont get iit-d")
        z = int(input("Enter jee mains rank: "))
        if z < 10000:
            print("Congrats! You get iiit-d")
        else:
            print("You dont get iiit-d")


elif x.lower() == "no":
    y = int(input("Enter jee mains rank: "))
    if y < 10000:
        print("Congrats! You get iiit-d")
    else:
        print("You dont get iiit-d")

else:
    print("Enter valid answer")
