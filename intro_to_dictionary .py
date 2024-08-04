# Creating a dictionary
animals = {'cat': 'meow', 'dog': 'bark', 'cow': 'moo'}
print(animals)  # Output: {'cat': 'meow', 'dog': 'bark', 'cow': 'moo'}

# Accessing dictionary items
print(animals['cat'])  # Output: meow
print(animals['dog'])  # Output: bark

# Modifying dictionary items
animals['dog'] = 'woof'
print(animals)  # Output: {'cat': 'meow', 'dog': 'woof', 'cow': 'moo'}

# Adding items to the dictionary
animals['lion'] = 'roar'
print(animals)  # Output: {'cat': 'meow', 'dog': 'woof', 'cow': 'moo', 'lion': 'roar'}

# Removing items from the dictionary
del animals['cow']  # Removes the item with key 'cow'
print(animals)  # Output: {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}

# Checking if a key exists in the dictionary
print('cat' in animals)  # Output: True

# Iterating through the dictionary key-value pairs
for animal, sound in animals.items():
    print(f"The {animal} goes {sound}")
# Output:
# The cat goes meow
# The dog goes woof
# The lion goes roar

# Getting the length of the dictionary
print(len(animals))  # Output: 3
