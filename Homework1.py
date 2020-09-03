# Task 1
# "1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран."
print('Hello, master Nikolay! =)')
# числа являются неизменяемыми значениями
print (5 % 5)
my_int = 10 ** 3000 # целое число неограниченной точности
my_cmplx = 3+4j  # комплексное число
print(type(my_cmplx))
print(type(my_int))
# print(type(my_cmplx + my_int))  #OverflowError: int too large to convert to float
#print(type(my_int / 3))  #OverflowError: integer division result too large for a float
print(type(''))  #пустая строка
print(float('3.14e-10'))  #вещественное число
print(type(3.14e-10))
print(type([0, 1, 2]))  #список - последовательность
print(type({0, 1, 2}))  #множество
print(type({}))  # пустой словарь
print(type(dict())) #пустой словарь
print(type(True))
print(type(None))
print(bool(None)) #
a = 9
b = 9
c = 13
print((a > b) and (b < c))
num_1 = int(input('Please, enter any number: '))
print("You've entered number:", num_1)

# Task 2
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

# time = int(input('Enter time in seconds: '))
# hours = time // 3600
# minutes = (time // 60) - (hours * 60)
# seconds = time % 60
# print(f'{hours:02}:{minutes:02}:{seconds:02}')

# Task 3
#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Please, enter any digit: ')
print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')

# Task 4
#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num_user = int(input('Hello, dear! Please, Enter any number: '))
current_max = 0
num = num_user  # отдельная переменная для хранения оставшейся части

while num > 0:
    digit = num % 10  # отделяем последнюю цифру
    if digit > current_max:
        current_max = digit
        if current_max == 9:  # Необязательно, максимальное число в любом случае 9
            break
    num = num // 10  # отсекаем от числа последнюю цифру

print('The maximum digit is:', current_max)

# Task 5
#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = float(input('Input operating income: '))
costs = float(input('Input costs: '))

result = revenue - costs

if result > 0:
    print('Сompany profit is: ', result)
    print('Profit margin is: ', result / revenue)
    people = int(input('Input staff number: '))
    print(f'Profit per employee: {result / people:.2f}')
elif result < 0:
    print('We are in the red! ->', result)
else:
    print('We are in 0')

# Task 6
#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров
# a и b и выводить одно натуральное число — номер дня.

while True:
    days = 1
    A_start_km = int(input('First day result: '))
    B_last_km = int(input('Target result: '))
    if A_start_km > B_last_km:
        print('Dear, first day result shall be < target result')
    else:
        while A_start_km < B_last_km:
            A_start_km += A_start_km * 0.1
            days += 1
        print('Athlete will achieve the target in {} days.'.format(days))
        break