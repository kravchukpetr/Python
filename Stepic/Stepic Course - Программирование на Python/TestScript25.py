lst = input().split(' ')
n = input()
counter = 0
flag = True
for i in lst:
    if i == n:
        print(counter, ' ', end='')
        flag = False
    counter += 1
if flag:
    print('Отсутствует')
