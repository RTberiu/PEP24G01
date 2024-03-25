#generator
# r = range(11)
# print(type(r))
#
# result_generator = (_ for _ in range(3))
# print(type(result_generator))
# print(next(result_generator))
# print(next(result_generator))
# print(next(result_generator))
# # print(next(result_generator))
#
# result_generator = (_ for _ in range(1000000000))

# def my_generator():
#     for _ in range(3):
#         yield 3
#
# # print(type(my_generator))
# # print(type(my_generator()))
#
# generator = my_generator()
# # generator.__next__()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# file operations

result = open("Modul8/example.py", "rt")
#print(result.read())
print(result.readlines())
result.flush() # write to disk
result.close() # no more write operation can be done

with open("Modul8/example.py", "rt") as file:
    output = result.readlines()
print(output)

with open("Modul8/example.py", "wt") as file:
    file.write("\n #comment")

with open("Modul8/test.txt",'rb') as file:
    output = file.read()

print(type(output))
print(output)

with open("Modul8/Cap8_Lab1,pdf","rb") as file:
    output = file.read()
print(output)