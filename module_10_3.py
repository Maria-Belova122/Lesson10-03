# ЗАДАНИЕ ПО ТЕМЕ "Блокировки и обработка ошибок"

import threading
from time import sleep
from random import randint


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    # Пополнение счета
    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            # randint(a,b) - Выводит случайное число от a до b включительно
            sum_credit = randint(50, 500)  # Сумма пополнения счета
            self.balance += sum_credit
            print(f'Пополнение: {sum_credit}. Баланс: {self.balance}')
            sleep(0.001)

    # Списание со счета
    def take(self):
        for i in range(100):
            sum_debit = randint(50, 500)  # Сумма списания со счета
            print(f'Запрос на {sum_debit}')
            if sum_debit <= self.balance:
                self.balance -= sum_debit
                print(f'Снятие: {sum_debit}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

# Создаём потоки и передаем в потоки сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
# Запускаем потоки
th1.start()
th2.start()
# Ждём завершения потоков
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
