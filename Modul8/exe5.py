class Clasa:
    an = None
    def __init__(self, lista_nume_data):
        self.dictionar = {}
        for entity in lista_nume_data[:]:
            if not self.an:
                self.an = entity.split('/')[1].split('-')[0]
                self.dictionar.update({entity.split('/')[0]: entity.split('/')[1].strip()})
                lista_nume_data.remove(entity)
            else:
                if self.an == entity.split('/')[1].split('-')[0]:
                    self.dictionar.update({entity.split('/')[0]: entity.split('/')[1].strip()})
                    lista_nume_data.remove(entity)
                else:
                    pass

        self.elevi_info = self.elevi_info.copy()
    def __str__(self):
        return self

    def __next__(self):
        new_info = dict(map(lambda item: (item[0], datetime.datetime(int(item[1].split("-")[0]),
                                                                    int(item[1].split("-")[1]),
                                                                    int(item[1].split("-")[2]))),
                            self.elevi_info.items()))

    def __str__(self):
        return(str(self.elevi.info))


with open('elevi.txt') as file:
    elevi = file.readlines()
classes = []
while elevi:
    classes.append(Clasa(elevi))

for class_ in classes:
    class_.next_birthday()

