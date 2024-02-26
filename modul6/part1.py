class Car:
    brand = 'Dacia'
    fuel_support = [95, 98]
    color = 'white'
    doors = 4
    #cars_built = []

    def __init__(self, doors=4):
        self.doors = doors
        print('starting construction:')

    def change_car_color(self, color):
        print(f'changing car {self.brand}')
        self.color = color

    def change_car_color_input(self):
        print(f'changing car {self.brand}')
        self.color = input('set new car color:')

car = Car(2)
print(car.brand)
car.brand = 'BMW'
car.fuel_support.append(101)
print(car.brand)
print(car.fuel_support)
car.change_car_color('red')
print(car.color)
print(f'Car doors {car.brand} nr of door is : {car.doors}')
car.change_car_color_input()
print(car.color)

car2 = Car()
print("New car", car2.brand)
print("New fuel", car2.fuel_support)
car2.change_car_color('blue')
print(car2.color)
print(f'Car doors {car2.brand} nr of door is : {car2.doors}')
car2.change_car_color_input()
print(car2.color)
# x = [1,2,3]
# x.append(4)
# print(x)