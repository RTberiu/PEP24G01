def user_provided_word():
    user_input = input("Type a word: ")
    for letter in user_input:
        yield letter

with open("result.txt",'w') as file:
    for letter in  user_provided_word():
        file.write(f"{letter[0]}:{letter[1]} \n")
