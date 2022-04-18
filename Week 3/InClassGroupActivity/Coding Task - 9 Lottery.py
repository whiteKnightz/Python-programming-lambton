import random


def contains(list_of_customers, filter):
    for x in list_of_customers:
        if filter(x):
            print(x, 'contains')
            return True
    print('not contains')
    return False


class Customer:
    def __init__(self, id, num1, num2, num3, num4, num5, num6):
        """Initialize attributes to describe a Customer."""
        self.id = id
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
        self.num6 = num6

    def __str__(self) -> str:
        return_str = '{num1},{num2},{num3},{num4},{num5},{num6}'
        return return_str.format(num1=self.num1, num2=self.num2, num3=self.num3, num4=self.num4, num5=self.num5,
                                 num6=self.num6)


class Lottery:
    def __init__(self, customers=[]):
        self.customers = customers

    def buy_tickets(self, customer_id, num1, num2, num3, num4, num5, num6):
        self.customers.append(Customer(customer_id, num1, num2, num3, num4, num5, num6))

    def pick_lottery(self):
        list_num = list(range(1, 10))
        lottery_numbers = []
        for i in range(1, 7):
            lottery_numbers.append(random.randint(1, 9))
        self.customers.count()


myList = [Customer(1, 0, 0, 0, 0, 0, 9), Customer(2, 0, 0, 0, 0, 0, 2), Customer(3, 0, 0, 0, 0, 0, 3)]
# for cus in myList:
#     print(cus)
# filter_value = [x for x in myList if (x.num1 == 0 and x.num2 == 0 and x.num3 == 0 and x.num4 == 0 and x.num5 == 0 and
#                                       x.num6 == 1)]
if contains(myList, lambda x: x.num1 == 0 and x.num2 == 0 and x.num3 == 0 and x.num4 == 0 and x.num5 == 0 and
                              x.num6 == 1):
    print('Contains in list')
