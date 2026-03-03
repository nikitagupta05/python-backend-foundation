password = input("Enter your password: ")

password_length = len(password)

if (password_length < 6):
    strength = "Weak password"
elif (password_length <= 10):
    strength = "Medium password"
else:
    strength = "Strong password"

print("Password strength is : ", strength)
