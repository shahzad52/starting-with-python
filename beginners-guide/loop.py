# Define a list
elements = ['apple', 'banana', 'cherry', 'date']

# Using a for loop
print("Using a for loop:")
for item in elements:
    print(item)

# Using a while loop
print("\nUsing a while loop:")
index = 0
while index < len(elements):
    print(elements[index])
    index += 1

# Using list comprehension
squared_numbers = [x**2 for x in range(5)]
print("\nSquared numbers using list comprehension:")
print(squared_numbers)

# Using enumerate to access index and value
print("\nUsing enumerate to access index and value:")
for index, item in enumerate(elements):
    print(f"Index {index}: {item}")
