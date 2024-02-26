class Shop:
    stock = {}
    user_input = None

    def modificare_stock(self):
        print(''''Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire''')

        self.user_input = input(f'alege optiune:\n')
        if self.user_input =='2':
            shop.adauga_produs('Unt', 5, 100)
    def adauga_produs(self, produs, pret, stoc):
        self.stock.update({produs: (pret, stoc)})


shop = Shop()
# shop.modificare_stock()
# print(f'ai ales: {shop.user_input}')
# print(shop.stock)
Shop.adauga_produs(shop,'Unt', 5, 100)
# print(shop.stock)
