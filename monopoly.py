import os
import random
import platform

from collections import deque

number_of_participants = 10
money_per_person = 10
money_per_trade = 1


class Person:
    id = 0

    def __init__(self, money):
        self.money = money
        Person.id += 1
        self.id = Person.id
        
class Market:
    clean_command = 'cls' if platform.system() == 'Windows' else 'clear'

    def __init__(self, money_per_person, money_per_trade, number_of_participants):
        self.participants = [Person(money_per_person) for _ in range(number_of_participants)]
        self.pool_of_participants = deque(self.participants)
        self.money_per_trade = money_per_trade
        self.money_stock = money_per_person * number_of_participants

    def trade(self, person_1, person_2):
        if random.randint(0, 1) == 1:
            person_1.money += self.money_per_trade
            person_2.money -= self.money_per_trade
        else:
            person_2.money += self.money_per_trade
            person_1.money -= self.money_per_trade

    def run_market(self):
        random.shuffle(self.pool_of_participants)

        for _ in range(len(self.pool_of_participants) // 2):
            p_1, p_2 = self.pool_of_participants.popleft(), self.pool_of_participants.popleft()
            self.trade(p_1, p_2)

            if p_1.money != 0:
                self.pool_of_participants.append(p_1)
            
            if p_2.money != 0:
                self.pool_of_participants.append(p_2)

        os.system(self.clean_command)
        for person in self.participants:
            s_n = round(30 * person.money / self.money_stock)
            print(f"Person {person.id:>10} {'-' * s_n}")

    def execute(self):
        while len(self.pool_of_participants) > 1:
            self.run_market()


market = Market(money_per_person, money_per_trade, number_of_participants)
market.execute()
