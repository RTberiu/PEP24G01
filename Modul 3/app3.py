
print("1. Capuccino ... 4 lei")
print("2. Espresso ... 3.5 lei")
option = int(input("Ce optiune alegeti?  [1,2] : "))
coin = int(input("Introduceti o bacnota [5,10] : "))

# if optiune == 1:
#     if coin == 5:
#         rest = 5 - 4
#     elif coin == 10:
#         rest = 10 - 4
# elif optiune == 2:
#     if coin == 5:
#         rest = 5 - 3.5
#     elif coin == 10:
#         rest = 10 - 3.5

# for opt in "1,2".split(","):
#     if int(opt) == option:
#         product_value = 4
#         break
#     elif int(opt) == option:
#         product_value = 3.5
#         break
#     for possible_coin in "5,10".split(","):
#         if coin == int(possible_coin):
#             break
#         # else:
#         #     continue
#     else:
#         print("not a valid coin")
#
# print(f"Veti primi restul de {possible_coin - product_value} lei ")