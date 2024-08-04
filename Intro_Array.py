# Creating a list
animals = ['cat', 'dog', 'rabbit']
print(animals)  # Output: ['cat', 'dog', 'rabbit']

# Accessing list items
print(animals[0])  # Output: cat
print(animals[1])  # Output: dog
print(animals[-1])  # Output: rabbit (last item)

# Modifying list items
animals[1] = 'hamster'
print(animals)  # Output: ['cat', 'hamster', 'rabbit']

# Adding items to the list
animals.append('parrot')  # Adds 'parrot' to the end of the list
print(animals)  # Output: ['cat', 'hamster', 'rabbit', 'parrot']

# Removing items from the list
animals.remove('hamster')  # Removes 'hamster' from the list
print(animals)  # Output: ['cat', 'rabbit', 'parrot']

# Removing items by index
del animals[2]  # Removes the item at index 2 ('parrot')
print(animals)  # Output: ['cat', 'rabbit']

# Popping items from the list (removes and returns the last item)
last_animal = animals.pop()
print(last_animal)  # Output: rabbit
print(animals)  # Output: ['cat']

# Recreating the list for further examples
animals = ['cat', 'dog', 'rabbit']

# Getting the length of the list
print(len(animals))  # Output: 3

# Checking if an item is in the list
print('dog' in animals)  # Output: True

# Iterating through the list
for animal in animals:
    print(animal)
# Output:
# cat
# dog
# rabbit

# Slicing lists
print(animals[1:3])  # Output: ['dog', 'rabbit'] (from index 1 to 2)
print(animals[:2])  # Output: ['cat', 'dog'] (from start to index 1)
print(animals[1:])  # Output: ['dog', 'rabbit'] (from index 1 to end)

# Copying a list
animals_copy = animals[:]
print(animals_copy)  # Output: ['cat', 'dog', 'rabbit']
