import random


# def contains(list_of_customers, filter):
#     for x in list_of_customers:
#         if filter(x):
#             return x
#     return None


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
        return_str = 'Customer Id - {id}: {num1},{num2},{num3},{num4},{num5},{num6}'
        return return_str.format(id=self.id, num1=self.num1, num2=self.num2, num3=self.num3, num4=self.num4,
                                 num5=self.num5, num6=self.num6)


class Lottery:
    def __init__(self, customers=[]):
        self.customers = customers
        self.lottery_numbers = []

    def buy_tickets(self, customer_id, num1, num2, num3, num4, num5, num6):
        self.customers.append(Customer(customer_id, num1, num2, num3, num4, num5, num6))

    def pick_lottery(self):
        lottery_numbers = []
        for i in range(1, 7):
            lottery_numbers.append(random.randint(1, 9))
        print(f'Lottery numbers are {lottery_numbers[0]}{lottery_numbers[1]}{lottery_numbers[2]}'
              f'{lottery_numbers[3]}{lottery_numbers[4]}{lottery_numbers[5]}')
        self.lottery_numbers = lottery_numbers
        self.check_jackpot_winner()
        self.check_second_jackpot_winner()

    def check_jackpot_winner(self):
        six_digit_winner = self.get_jackpot_winner(self.lottery_numbers[0], self.lottery_numbers[1],
                                                   self.lottery_numbers[2], self.lottery_numbers[3],
                                                   self.lottery_numbers[4], self.lottery_numbers[5])
        if six_digit_winner is not None and len(six_digit_winner) > 0:
            for cus in six_digit_winner:
                print(f'The winner of 100000000 is customer id: {cus.id}')
        else:
            print(f'There is no winner for 100000000.')

    def get_jackpot_winner(self, num1, num2, num3, num4, num5, num6):
        return [x for x in self.customers if
                (x.num1 == num1 and x.num2 == num2 and
                 x.num3 == num3 and x.num4 == num4 and
                 x.num5 == num5 and x.num6 == num6)]

    def check_second_jackpot_winner(self):
        five_digit_winner = self.get_second_jackpot_winner(self.lottery_numbers[0], self.lottery_numbers[1],
                                                           self.lottery_numbers[2], self.lottery_numbers[3],
                                                           self.lottery_numbers[4], self.lottery_numbers[5])
        if five_digit_winner is not None and len(five_digit_winner) > 0:
            for cus in five_digit_winner:
                print(f'The winner of 1000000 is customer id: {cus.id}')
        else:
            print(f'There is no winner for 1000000.')

    def get_second_jackpot_winner(self, num1, num2, num3, num4, num5, num6):
        return [x for x in self.customers if
                not (x.num1 == num1 and x.num2 == num2 and
                     x.num3 == num3 and x.num4 == num4 and
                     x.num5 == num5 and x.num6 == num6) and
                ((x.num1 == num1 and x.num2 == num2 and
                  x.num3 == num3 and x.num4 == num4 and
                  x.num5 == num5) or
                 (x.num1 == num1 and x.num2 == num2 and
                  x.num3 == num3 and x.num4 == num4 and
                  x.num6 == num6) or
                 (x.num1 == num1 and x.num2 == num2 and
                  x.num3 == num3 and
                  x.num5 == num5 and x.num6 == num6) or
                 (x.num1 == num1 and x.num2 == num2 and
                  x.num4 == num4 and
                  x.num5 == num5 and x.num6 == num6) or
                 (x.num1 == num1 and
                  x.num3 == num3 and x.num4 == num4 and
                  x.num5 == num5 and x.num6 == num6) or
                 (x.num2 == num2 and
                  x.num3 == num3 and x.num4 == num4 and
                  x.num5 == num5 and x.num6 == num6))
                ]


userList = []
lotteryGame = Lottery([])
for i in range(1, 1000000):
    value = str(random.randint(100000, 1000000))
    lotteryGame.buy_tickets(i, int(value[0]), int(value[1]), int(value[2]), int(value[3]), int(value[4]), int(value[5]))
lotteryGame.pick_lottery()

