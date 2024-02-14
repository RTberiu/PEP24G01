def putere():
    result = None
    while True:
        user_Data1 = input('Introduce nr 1:')
        # user_Data2 = input('Introduce nr 2:')
        if user_Data1 in ["q", "Q"]:
            return result
        num1 = int(user_Data1)
        num2 = int(input("Introduce nr 2: "))
        result = num1 ** num2
        # return result
        # break
print(putere())