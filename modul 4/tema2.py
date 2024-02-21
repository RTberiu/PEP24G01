carti = input("Cate carti doresti sa adaugi : ")

lista_carti = []
for i in range(int(carti)):
    print("Cartea", i + 1)
    nume = input("Numele Cartii: ")
    autor = input("Autorul: ")
    an = input("Anul p ublicarii: ")
    carte = {"nume": nume, "autor": autor, "an": an}
    lista_carti.append(carte)
print("Cartile sunt :")
for carte in lista_carti:
    print(carte)