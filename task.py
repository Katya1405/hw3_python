# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

someList = [2, 5, 1, 9, 0, 5]
sum = 0
for i in range(len(someList)):
    if i % 2 != 0:
        sum += someList[i]
print(sum)


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

someListt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = []
for i in range(len(someListt)//2):
    newList.append(someListt[i]*someListt[-i-1])
print(newList)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.


listt = [1.1, 1.2, 3.1, 5, 10.01]
neewList = []
for i in listt:
    neewList.append(i-int(i))
result = max(neewList)-min(neewList)
print(format(result, '.2f'))

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input())
string = ''
while number > 0:
    string += str(number % 2)
    number //= 2
newString = ''.join(reversed(string))
print(newString)
