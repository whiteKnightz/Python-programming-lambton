class Address:
    def __init__(self, street_no, street_name, zip_code, city, country):
        """Initialize attributes to describe a Address."""
        self.street_no = street_no
        self.street_name = street_name
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def __str__(self):
        """String function for the class."""
        value = 'street number {street_no} named {street_name} in {city}, {country} with postal code {zip_code}'
        return value.format(street_no=self.street_no, street_name=self.street_name, city=self.city,
                            country=self.country, zip_code=self.zip_code)


class Customer:
    def __init__(self, cus_id, name, age, contact_no, address, program):
        """Initialize attributes to describe a Customer."""
        self.std_id = cus_id
        self.name = name
        self.age = age
        self.contact_no = contact_no
        self.address = address
        self.program = program

    def __str__(self):
        """String function for the class."""
        value = '{name} with customer id {std_id} is aged {age} and his contact number is {contact_no}. {name}\'s' + \
                ' address is: {address}'
        return value.format(name=self.name, std_id=self.std_id, age=self.age, contact_no=self.contact_no,
                            address=self.address)


cus_address = Address(400, "265 Yorkland Blvd", "ON M2J 1S5", "North York", "Canada")
cus_juan = Customer("C0810093", "Juan", 18, 90920289298, cus_address, "Platinum Plus")
print(f'\n\n\n\n{cus_juan}')
