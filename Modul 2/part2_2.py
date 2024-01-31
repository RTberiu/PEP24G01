#string format
#method format
my_str = "text {}"
print(my_str.format('''example'''))
my_str = "text {1} {0}"
print(my_str.format('example1', 'example2'))
my_str = "text {ex1} {ex2}"
print(my_str.format(ex1='example1', ex2='example2'))
#print(my_str.format(2))


#formatted string
ex1 = "example1"
ex2 = "example2"
print(f"text2 {ex1}")
print(f"text2 {2}")
print(f"text2 {ex1} {ex2} {ex1}")


#len function
ex1 = "example"
print(len(ex1))


#idex of string

hello = "hello world"
   #0 -> 10
print(hello[2])
print(hello[2:7]) #last index not included
print(hello[0:12:2]) #not all versions of python 3
print(hello[::2])

#hello = 'h e l l o w o r l d'
print(hello[::-1]) #de la coada la cap
print(hello[-5:-1:1])
print("negative step")
print(hello[-5:-10:-1])





