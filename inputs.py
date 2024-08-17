# String Input
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Integer Input
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

# Float Input
height = float(input("Enter your height in meters: "))
print("Your height is " + str(height) + " meters.")

# List Input
numbers = input("Enter numbers separated by spaces: ").split()
print("You entered the numbers: " + str(numbers))

# Boolean Input
is_student = input("Are you a student? (yes/no): ")
is_student = True if is_student.lower() == 'yes' else False
print("Student status: " + str(is_student))