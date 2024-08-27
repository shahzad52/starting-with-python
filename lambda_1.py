# A lambda function to add 10 to the input
add_ten = lambda x: x + 10

# Usage
result = add_ten(5)
print(result)  # Output: 15
# Using lambda to square each element in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # Output: [1, 4, 9, 16]
# Using lambda to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6]
# Sorting a list of tuples based on the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
