class Coffee:
#Вводим название класса
    def __init__(self, name, price): #свойства
#Определяем свойства
        self.name = name
        self.price = price
    def show_name(self): #методы
#Метод, показывающий название кофе
        nameOfCoffee ='Название этого кофе: ', self.name
        print(nameOfCoffee)
    def evening_discount(self):
#Отображение стоимости кофе с учетом вечерней скидки в 10%
        dis=(self.price-(self.price/100*10))
        print('Цена кофе с учетом скидки составит ', dis)

coff1 = Coffee('Капучино', 200)
coff2 = Coffee('Латте', 250)

coff1.show_name()
coff1.evening_discount()

coff2.show_name()
coff2.evening_discount()

input()
