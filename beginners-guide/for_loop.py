# Define a list of numbers
numbers = [1, 2, 3, 4, 5]
# we are using for loop for iterating through the list
# Using a simple for loop to iterate through the list
print("Using a simple for loop:")
for number in numbers:
    print(number)


---------------------------------
# Define a list of temperatures
temperatures = [72, 85, 90, 65, 79]

# Using a for loop with a conditional statement
print("\Using a for loop with a conditional statement:")
for temp in temperatures:
    if temp > 80:
        print(f"{temp}°F - It's hot!")
    else:
        print(f"{temp}°F - It's moderate.")

