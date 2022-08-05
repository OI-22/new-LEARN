number = 23
guess = int(input('Введите целое число : '))

if guess == number :
    print('Поздровляю, вы угадали')
    print('(Хотя и не выиграл никакого приза)')
elif guess < number :
    print('Нет, загаданое число больше')
else :
    print('Нет, загадоное число меньше')
