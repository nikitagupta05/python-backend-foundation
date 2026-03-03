n = int(input("Enter a number: "))

sum = 0

for i in range(1,n+1):
    if (i % 2 == 0):
        sum = sum + i
print(f"sum of the {n} number is : {sum}")
