# This function checks if you are tall enough and how much you need to pay depending your age 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster :-)")
    age = int(input("What is your age? "))
    if age <= 10:
        print("Please pay $5")
    elif age <= 16:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride.")
    

# This function will check if you want photo taken as well and will calculate the final bill

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
 