result='abc'.__iter__()
print(type(result))

print(id(result))
print(id(result.__iter__()))

print(next(result))
print(result.__next__())
print(result.__next__())
# print(result.__next__())

result="abc"
iterator = result.__iter__()
for i in result:
    print(i)

# number = 5
# for i in number:
#     print(i)
# class Number:
#     def __init__(self,number):
#         self.number = number
#
#     def __iter__(self):
#         return range(self.number).__iter__()
#
# n = Number(5)
# for i in n:
#     print(i)

class Number(float):
    def __init__(self,number):
        self.number = number

    def __iter__(self):
        return NumberIterator(self.number)

class NumberIterator:


    def __init__(self, number):
        self.number = number
        self.number_list = []
        for i in range(self.number):
            self.number_list.append(i+1)
        self.number_list.sort(reverse=True)
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return self.number_list.pop()
        except IndexError:
            raise StopIteration
        return result

n = Number(5)

for i in n:
    print(i)

print(n + 5)