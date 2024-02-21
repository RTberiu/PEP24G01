my_list = ["Masa", 5, "Scaun", 4.5, [5,6,7],8]
for obj in my_list:
    print(f"Tipul obiectului{obj}este {type(obj)}")
    if type(obj) == list:
        for inner_obj in obj:
            print(f"tipul obiectlui{inner_obj}este{type(inner_obj)}")