# Using lambda to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6]
# Sorting a list of tuples based on the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]
