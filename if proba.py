number = 23
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздровляем вы угадали')

elif guess < number:
    print('Загаданое число болше')
else:
    print('Загадоное число меньше')
