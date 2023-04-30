#1 Цикли
str = '+'
i = 0
while i < 10: #поки
    print(str)
    i = i + 1
#2
i = 0
while i < 10: #поки
    print(i)
    i = i + 2
#3
n = int(input('Число'))
s = 0
i = 1
while i <= n:
    s = s + i
    i = i + s
    print('s =',s)
#4!!!!
n=input('Введіть число =')
while type (n) !=int:
    try:
        n=int(n)
        print('Hello')
    except ValueError:
        print('Неправильно ввели число!')
        n = input('Введіть ціле число')
#5
a = int(input('Число'))
b = int(input('lllll'))
suma = 0
for i in range(a,b): #diaposon
    suma = suma + i
print(suma)
#6
n = int(input('Уведіть кількість доданків:'))
x = float(input('Перший доданок'))
s = x
for i in range(n-1): #i завжди = 0
    x += 10
    s += x
print(s)