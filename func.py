#1

list_1 = ['name', 'age', '1', '19']

def reverse(value):
    f_part = value[:len(value)//2][::-1]
    s_part = value[len(value)//2:][::-1]
    return f_part + s_part    
print(reverse(list_1))
    
#2
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = 11
print("Fibonacci:")
for i in range(1,n):
    print(fibonacci(i),end = ',')

print()
print()
#3
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def plus_minus(x,y):
    print(plus(x,y),minus(x,y))
plus_minus(12,2)

print()

#4
a = input('Введите название файла: ')
def new_file(n):
    file_name = f'{a}.txt'
    with open(file_name,'w') as tx:
        return 'Файл создан'
tx2 = new_file(a)
print(tx2)
print()

#5
from random import choice
from re import L
def gen_number():
    first_nums = '0444'
    for i in range(6):
        first_nums+=choice(['1','4','5','7','9','0'])
    return first_nums
print(gen_number())  
print()

#6
list_temp = [1,2,3,4,5,6,7,8,9]
def odd_nums(l):
    l2 = []
    for i in l:
        if i % 2 != 0:
            l2.append(i)
    return l2
print(odd_nums(list_temp))

7
s1 = {1,2,3,4,5,6,7,8}
def prim_set(s):
    if len(s) == 0:
        return s
    s.pop()    
    return prim_set(s)
print(prim_set(s1))