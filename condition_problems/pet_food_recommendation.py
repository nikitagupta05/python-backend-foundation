pet = input("Enter pet species (Dog/Cat) : ")
age = int(input("Enter the age of a pet : "))

if (pet == "Dog"):
    if (age < 2):
        print("puppy food")
    else:
        print("Adult dog food")
elif (pet == "Cat"):
    if (age > 5):
        print("Senior cat food")
    else:
        print("Junior cat food")

else:
    print("Invalid pet type")