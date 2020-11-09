add = input("Введите пароль:")
result = 0

try:
    result = 21/len(add)#строка добавлена потому-что без нее не выводится ошибка ZeroDivisionError
    result = 21/len(int(add))#строка должна стоять под условием выше, т.к программа работает последовательно
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except TypeError:
    print ('Ваш пароль состоит только из цифр')
except ValueError:
    print('Требования к паролю соблюдены')

