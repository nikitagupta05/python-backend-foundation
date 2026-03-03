distance = int(input("Enter a distance : "))

if (distance < 3):
    transport= "Walk"
elif (distance <= 15):
    transport = "Bike"
elif (distance > 15):
    transport = "Car"

print("AI recommends you the transport of : ", transport)