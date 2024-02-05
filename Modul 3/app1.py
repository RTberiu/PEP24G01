cnp = input('introdu primele 7 cifre din CNP: ')

sex = cnp[0]
an = cnp[1:3]

if sex == "1" or sex == "2":
    an_nastere = int("19" + an)
    print(an_nastere)
elif sex == "5" or sex == "6":
    an_nastere = int("20" + an)
    print(an_nastere)
else:
    print("valoare incorecta pentru cnp:")

an_curent = 2024
varsta = an_curent - an_nastere
print(varsta)
if varsta >= 18:
    print("ai peste 18 ani: ")
else:
    print("Nu aveti peste 18 ani")