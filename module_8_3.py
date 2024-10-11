class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if Car.__is_valid_vin(vin) is True:
            self.__vin = vin
        if Car.__is_valid_numbers(numbers) is True:
            self.__numbers = numbers

    def __is_valid_vin(vin):
        if isinstance(vin, int):
            if 1000000 <= vin <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Некорректный тип vin номер')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')

    def __is_valid_numbers(numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
