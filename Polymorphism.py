class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")


def demonstrate_fly(bird):
    bird.fly()


sparrow = Bird()
penguin = Penguin()

demonstrate_fly(sparrow)  # Output: Bird can fly
demonstrate_fly(penguin)  # Output: Penguin cannot fly
