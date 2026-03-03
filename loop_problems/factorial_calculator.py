
"""using for loop"""

# number = int(input("Enter a number : "))
# fact = 1

# for i in range(number,0,-1):
#     fact = i * fact      

# print(f"Factorial of {number} is : {fact}")





"""using while loop"""

number = int(input("Enter a number : "))
fact = 1


while (number > 0):
    fact = fact * number 
    number = number - 1

print("Factorial is : ", fact)