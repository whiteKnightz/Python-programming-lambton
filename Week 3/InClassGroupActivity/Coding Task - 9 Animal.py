def add_seperator(msg):
    """Seperator to use before each question"""
    print("\n" * 5)
    print(msg)
    print("-" * 50)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_make_noise(self):
        print(f'{self.name} can make loud noise.')

    def can_run(self):
        print(f'{self.name} can run.')

    def can_eat(self):
        print(f'{self.name} can eat anything.')


class Dog(Animal):
    def __init__(self, name, age, breed, height):
        super().__init__(name, age)
        self.breed = breed
        self.height = height

    def can_make_noise(self):
        super().can_make_noise()
        print(f'{self.name} is a dog and it barks.')

    def can_run(self):
        super().can_run()
        print("Dog can run very fast.")

    def can_eat(self):
        super().can_eat()
        print("Dog prefer to eat meat.")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def can_make_noise(self):
        print(f'{self.name} is a cat and it meows.')

    def can_run(self):
        super().can_run()
        print("Cats are very fast.")

    def can_eat(self):
        print("Cat prefer to eat meat, especially fish.")


add_seperator("Tommy the dog")
tommy_dog = Dog("Tommy", 8, "Husky", 100)
tommy_dog.can_make_noise()
tommy_dog.can_eat()
tommy_dog.can_run()

add_seperator("Garfield the dog")
garfield_dog = Cat("Garfield", 8, "Orange")
garfield_dog.can_eat()
garfield_dog.can_make_noise()
garfield_dog.can_run()
