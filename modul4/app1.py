def cpass():
    requires_chars = ["!", "@", "%"]
    pas = input("Introduceti parola: ")
    print(pas)
    condition_not = False
    if len(pas) < 7:
        print("insuficient password ")
        condition_not = True
        # cpass()
    # else:
    for character in requires_chars:
        if character in pas:
            break
    else:
            print("Parola trebuie sa contina : ! @ %")
            condition_not = True
            # cpass()

    for character in range(10):
        if str(character) in pas:
            break
    else:
        print("Parola trebuie sa contina numere")
        condition_not = True
    if condition_not:
        cpass()

    # if __name__ == "__main__":

cpass()

# my_str = "abcd1232"
# check_chars = ['2', '!']
# for char in check_chars:
#     if char in my_str:
#         print(f"success, found {char}")
#         break
# else:
#     print(f"could not find: {check_chars}")


# my_str = "abcd1232"
# check_chars = range(10)
# for char in check_chars:
#     if str(char) in my_str:
#         print(f"success, found {char}")
#         break
# else:
#     print(f"could not find: {check_chars}")