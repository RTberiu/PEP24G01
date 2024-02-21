from modul4.app3 import medie

nume = input ("Introduceti numele elevului")
note = input("Introduceti notele elevului separate print virgula")
# print(note.split(","))

grades = []
for number in note.split(","):
    try:
        grades.append(float(number))
    except ValueError:
        print(f"{number}is not a grade")

assert grades, "No grades were provided"
print(grades)