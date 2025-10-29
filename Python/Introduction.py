import random
# input(), len(), print() these are some of the built-in functions in Python.
name = input("Enter your name: ")
# When you take input from the user, it accepts it as a string by default.
print(f"Hello, {name}! Welcome to the program.")
print("The length of your name is:", len(name))

# If-else statement example
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Loop example
print("Random numbers:", end=' ')
for i in range(5):
    print(random.randint(1, 10), end=' ')
print()  # for a new line after the loop output