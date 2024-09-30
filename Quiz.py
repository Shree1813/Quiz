# Test yourself quiz!

# Question 1 - Assigning Variables
x = 10  # assigned an x variable equal to 10
y = 3   # assigned an y variable equal to 3
print(x * y)  # Multiplication
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x / y)  # Division


# Question 2 - Lists
my_list = list(range(0, 101, 2))  # Create the list
print(my_list)

print(my_list[0:10])  # Printing the first ten elements of the list

print(len(my_list))  # Finding the length of the list

my_list.append("Hello")  # Appending a value to this list - can be any type!
print(my_list)


# Question 3 - If Statement
number = 835
if number % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 5")


# Question 4 - For Loop
for i in range(6):    # Remember we use 6 because the range command takes up to value n-1
    print(i)

