def add_seperator(msg):
    """Seperator to use before each question"""
    print("\n" * 5)
    print(msg)
    print("-" * 50)


class Restaurant:
    def __init__(self, name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe a restaurant."""
        print(f'{self.name} serves {self.cuisine_type} cuisine type.')

    def open_restaurant(self):
        """Message the restaurant is open."""
        print(f'{self.name} is open now.')

    def show_number_served(self):
        """Show number of customer served."""
        print(f'{self.number_served} numbers of customer are served in {self.name}.')

    def set_number_served(self, number_served):
        """Set number of customer served."""
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        """Increment number of customer served."""
        self.number_served += increment_number


def first_question():
    add_seperator("9-1. Restaurant")
    grand_restaurant = Restaurant('Le Grande Place', 'French')
    print(f'Restaurant Name:\t{grand_restaurant.name}.\nCuisine Type:\t\t{grand_restaurant.cuisine_type}.\n\n')
    grand_restaurant.describe_restaurant()
    grand_restaurant.open_restaurant()


first_question()


def second_question():
    add_seperator("9-2. Three Restaurants")
    french_restaurant = Restaurant('Le Grande Place', 'French')
    french_restaurant.describe_restaurant()
    italian_restaurant = Restaurant('Ristorante Sotto Sotto', 'Italian')
    italian_restaurant.describe_restaurant()
    spanish_restaurant = Restaurant('Patria', 'Spanish')
    spanish_restaurant.describe_restaurant()


second_question()


class User:
    def __init__(self, f_name, l_name, age, contact_no, profession):
        """Initialize attributes to describe a User."""
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.contact_no = contact_no
        self.profession = profession
        self.login_attempts = 0

    def describe_user(self):
        """Describe a User."""
        print(
            f'Name: {self.f_name} {self.l_name}\nAge: {self.age}\nprofession: {self.profession}\nContact No.: {self.contact_no}')

    def increment_login_attempt(self):
        """Increment the login attempt."""
        self.login_attempts += 1

    def reset_login_attempt(self):
        """Reset the login attempt."""
        self.login_attempts = 0

    def show_login_attempt(self):
        """Show the login attempt."""
        print(f'There are {self.login_attempts} login attempts.')


def third_question():
    add_seperator("9-3. Users")
    ab_user = User('Abhishek', 'Satyal', 26, 98143387955, 'Software Developer')
    ab_user.describe_user()


third_question()


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()  # titleCased value

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def set_odometer(self, odometer_reading):
        """Set value for odometer_reading."""
        self.odometer_reading = odometer_reading

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


def fourth_question():
    add_seperator("Modify the given code.")
    my_new_car = Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    my_new_car.set_odometer(50)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(11)
    my_new_car.read_odometer()


fourth_question()


def fifth_question():
    add_seperator("9-4. Number Served")
    grand_restaurant = Restaurant('Le Grande Place', 'French')
    grand_restaurant.show_number_served()
    """Set number of customer served as 40"""
    grand_restaurant.set_number_served(40)
    grand_restaurant.show_number_served()
    """Increment the number of customer served by 12"""
    grand_restaurant.increment_number_served(12)
    grand_restaurant.show_number_served()


fifth_question()


def sixth_question():
    add_seperator("9-5. login Attempts")
    ab_user = User('Abhishek', 'Satyal', 26, 98143387955, 'Software Developer')
    """Show login attempts."""
    ab_user.show_login_attempt()
    """Login attempt 6 times."""
    for i in range(6):
        ab_user.increment_login_attempt()
    """Show login attempts."""
    ab_user.show_login_attempt()
    """Reset login attempts."""
    ab_user.reset_login_attempt()
    """Show login attempts."""
    ab_user.show_login_attempt()


sixth_question()
