# Homework

try:
    user_numb1 = input('Введите первое число: ') # вводим данные с клавиатуры
    user_numb2 = input('Введите первое число: ')
    result = int(user_numb1)/int(user_numb2)
except ValueError:
    print('Ошибка! Вы ввели строку')
except ZeroDivisionError:
    print('Ошибка! Деление на ноль')
else:
    print(f'Результат деления равен: {result}')
finally:
    print('Работа выполнена!')
