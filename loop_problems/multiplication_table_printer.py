n = int(input("Enter a number : "))

print(f"Multiplication table of {n} is : ")

for i in range(1,11):
    if (i == 5):
        continue
    else:
        print(f"{n} X {i} = {n*i}")