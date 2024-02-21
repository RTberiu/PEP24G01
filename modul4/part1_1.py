# def add_(x, y):
#     return x + y
# print(add_(3, 4))
#

# result = 1
# def factorial(x):
#     global result
#     for i in range(1, x+1):
#         result *= i
# factorial(4)
# print(result)

# result = 0
# def gauss(n):
#     global result
#     # result = 0
#     for i in range(1, n+1):
#         result += i
# gauss(100)
# print(result)
#
# print((100*(100+1))/2)
# 1.... 1/n
suma = 0
def sumafractii(n):
    global suma
    for i in range(1, n+1):
        suma += 1/i
    return suma

n = int(input())
print(sumafractii(n))
