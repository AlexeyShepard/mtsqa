import random

# Генерация случайного номера телефона для формы
def random_number():
        phone_number = '901'

        for _ in range(7):
            phone_number += str(random.randint(0, 9))

        return phone_number