# Creating a set
animals = {'cat', 'dog', 'rabbit'}
print(animals)  # Output: {'cat', 'dog', 'rabbit'}

# Adding items to the set
animals.add('parrot')  # Adds 'parrot' to the set
print(animals)  # Output: {'cat', 'dog', 'rabbit', 'parrot'}

# Removing items from the set
animals.remove('dog')  # Removes 'dog' from the set
print(animals)  # Output: {'cat', 'rabbit', 'parrot'}

# Checking if an item is in the set
print('rabbit' in animals)  # Output: True
print('dog' in animals)  # Output: False

# Iterating through the set
for animal in animals:
    print(animal)
# Output (order may vary):
# cat
# rabbit
# parrot

# Getting the length of the set
print(len(animals))  # Output: 3

# Clearing the set (removing all items)
animals.clear()
print(animals)  # Output: set()
