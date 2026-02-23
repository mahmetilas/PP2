# Create a generator that generates the squares of numbers up to some number N.
def Square(num):
    for i in range(1, num + 1):
        yield i**2

num = int(input())

for x in Square(num):
    print(x)
print('\n')
# ---------------------------------------------------------------------------------------------------------------
# Write a program using generator to print the even numbers between 0 and n in
# comma separated form where n is input from console.
def Odd(num):
    for i in range(num+1):
        if(i%2!=0):
            yield i

num = int(input())

for x in Odd(num):
    print(x)
print('\n')
# ---------------------------------------------------------------------------------------------------------------
# Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.
def fun(num):
    for i in range(num+1):
        if(i%3==0 and i%4==0):
            yield i

num = int(input())

for x in fun(num):
    print(x)
print('\n')
# ---------------------------------------------------------------------------------------------------------------
# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" 
# loop and print each of the yielded values.
def func(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input())
b = int(input())

for x in func(a, b):
    print(x)
print('\n')
# ---------------------------------------------------------------------------------------------------------------
# Implement a generator that returns all numbers from (n) down to 0.
def func(num):
    n = reversed(range(num+1))
    for i in n:
        yield i

a = int(input())

for x in func(a):
    print(x)
print('\n')