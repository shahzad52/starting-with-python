# A lambda function to add 10 to the input
add_ten = lambda x: x + 10

# Usage
result = add_ten(5)
print(result)  # Output: 15
# Using lambda to square each element in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # Output: [1, 4, 9, 16]
