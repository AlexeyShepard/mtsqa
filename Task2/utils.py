import random

# Генерация случайного номера для формы
def random_number():
        phone_number = '9'

        for _ in range(9):
            phone_number += str(random.randint(0, 9))

        return phone_number