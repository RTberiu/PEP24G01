lista = input("Introduceti lista de task:")
lista_task = lista.split(",")
print(lista_task)
no_duplicates = []
for task in lista_task:
    if task not in no_duplicates:
        no_duplicates.append(task)
print(no_duplicates)
