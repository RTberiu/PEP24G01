str1 = "hello world"
print(type(str1))
int1 = 100
print(type(int1))
none = None
print(type(none))

result = str1.capitalize()
print("Return string:", type(result))

str1 = "hello world {} {}"
result = str1.format("test","test2")
print("Formatted string:", result)

str1 = "hello world"
result = str1.center(20, "#")
print("Centered Formatted string:", result)

print('/\\'.center(10))
print('/  \\'.center(10))
print('/____\\'.center(10))