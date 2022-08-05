from random import randint


lst1 = []
while not lst1:
    try:
        lst1 = list(map(int, input('Enter whole numbers separated by spaces: ').split()))
    except:
        continue

lst2 = [randint(-25, 50) for _ in range(len(lst1))]
res_lst = [x+y for x, y, in zip(lst1, lst2)]
print(f'Your list: {lst1}')
print(f'Random list: {lst2}')
print(f'Sum list: {res_lst}')
