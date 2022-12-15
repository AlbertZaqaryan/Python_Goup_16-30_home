# ---------------------------------------------
# 64
# prices = 4.95, 9.95, 14.95, 19.95, 24.95
# for i in prices:
#     print(f'{i} --- {round(i - (i * 60 / 100), 2)}')
# ---------------------------------------------
# 65
# for i in range(0, 101, 10):
#     print(f'{i} -- {round(((i - 32) / 9) * 5, 2)}')
# ---------------------------------------------
# 66
# import math

# s = 0
# while True:
#     number = float(input('Enter number: '))
#     if number == 0:
#         if s % 5 >= 2.5:
#             print(s)
#             print(math.ceil(s))
#             break
#         elif s % 5 < 2.5:
#             print(math.floor(s))
#             break
#     else:
#         s += number

# ---------------------------------------------
# ----------------- CHIN GA CHUNG -------------
# import random

# user_points = 0
# pc_points = 0
# while True:
#     if user_points == 3:
#         print('Win user end game!!!!')
#         break
#     elif pc_points == 3:
#         print('Win pc end game!!!!')
#         break
#     user = input('Enter Rock/Paper/Scissors: ')
#     pc = random.choice(('Rock', 'Paper', 'Scissors'))
#     if (user == 'Rock' and pc == 'Scissors') or (user == 'Paper' and pc == 'Rock') or (user == 'Scissors' and pc == 'Paper'):
#         user_points += 1
#         print(f'Win user\nuser points = {user_points}, pc points = {pc_points}\nuser = {user}, pc = {pc}')
#     elif (pc == 'Rock' and user == 'Scissors') or (pc == 'Paper' and user == 'Rock') or (pc == 'Scissors' and user == 'Paper'):
#         pc_points += 1
#         print(f'Win pc\nuser points = {user_points}, pc points = {pc_points}\nuser = {user}, pc = {pc}')
#     else:
#         continue
# ---------------------------------------------
# 67

# for i in range(100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} - fizz buzz')
#     elif i % 5 == 0:
#         print(f'{i} - buzz')
#     elif i % 3 == 0:
#         print(f'{i} - fizz')
# ---------------------------------------------
# a = int(input('Enter number1: '))
# b = int(input('Enter number2: '))
# c = int(input('Enter number3: '))
# print(f'min - {min(a, b, c)} mean - {(a + b + c) - min(a, b, c) - max(a, b, c)} max - {max(a, b ,c)}')
# ---------------------------------------------
# number = int(input('Enter number: '))
# s = ''
# while number != 1:
#     s += str(number % 2)
#     number = number // 2
# print(f'{number}{s[::-1]}')
# ---------------------------------------------
