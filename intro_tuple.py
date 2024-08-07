# Creating a tuple
animals = ('cat', 'dog', 'cow')
sounds = ('meow', 'bark', 'moo')
animal_sounds = (animals, sounds)
print(animal_sounds)  # Output: (('cat', 'dog', 'cow'), ('meow', 'bark', 'moo'))

# Accessing tuple elements
print(animal_sounds[0][0])  # Output: cat
print(animal_sounds[1][1])  # Output: bark

# Modifying tuples (not directly possible, creating new tuple instead)
# Since tuples are immutable, we cannot modify them directly. We can create a new tuple if needed.
new_animal_sounds = (animals, ('meow', 'woof', 'moo'))
print(new_animal_sounds)  # Output: (('cat', 'dog', 'cow'), ('meow', 'woof', 'moo'))

# Adding elements to a tuple (not directly possible, creating new tuple instead)
# Tuples are immutable, so we create a new tuple with additional elements.
extended_animals = animals + ('lion',)
extended_sounds = sounds + ('roar',)
extended_animal_sounds = (extended_animals, extended_sounds)
print(extended_animal_sounds)  # Output: (('cat', 'dog', 'cow', 'lion'), ('meow', 'bark', 'moo', 'roar'))

# Removing elements from a tuple (not directly possible, creating new tuple instead)
# Tuples are immutable, so we create a new tuple with the desired elements.
reduced_animals = ('cat', 'dog', 'lion')
reduced_sounds = ('meow', 'woof', 'roar')
reduced_animal_sounds = (reduced_animals, reduced_sounds)
print(reduced_animal_sounds)  # Output: (('cat', 'dog', 'lion'), ('meow', 'woof', 'roar'))

# Checking if an element exists in the tuple
print('cat' in animals)  # Output: True

# Iterating through the tuple elements
for animal, sound in zip(animals, sounds):
    print(f"The {animal} goes {sound}")
# Output:
# The cat goes meow
# The dog goes bark
# The cow goes moo

# Getting the length of the tuple
print(len(animals))  # Output: 3
