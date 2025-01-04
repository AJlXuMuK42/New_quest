# name=input('Введите ваше имя: ')
# if name == 'Gangster':
#     print('Ну привет, ковбой!')
# else:
#     print('Приветствую,', name)
number=int(input('Введите число: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 == 0:
    print('Buzz')
else:
    print('Число неверное')



