# password = 7788
# for attempt in range(10000):
#     passwordin = int(input("introduceti parola: "))
#     if password == passwordin:
#         print("access granted")
#         break
#     else:
#         print("WRONG PASSWORD")

password = 7788
while True:
    passwordin = int(input("introduceti parola: "))
    if password == passwordin:
        print("access granted")
        break
    else:
        print("WRONG PASSWORD")
