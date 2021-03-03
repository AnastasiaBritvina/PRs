'''Реализовать три  произвольных класса с констуркторами и деструкторами.
Привести пример использования еще трех произвольных "волшебных" методов'''
#1
class Persons:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def what_is_your_name(self):
        print(self.name)
    def __str__(self):
        return 'Имя: {}, возраст: {}'.format(self.name, self.age)
    def __del__ (self):
        print("Удаление: " + self.__str__())

person1 = Persons ('Vasya', 10)
person1.what_is_your_name()
print(person1)



#2
class Phones:
    def __init__(self, screen, buttons):
        self.screen = screen
        self.buttons = buttons
    def numb_of_buttons(self):
        print("for this phone: ", self.buttons)
    def __len__(self):
        return len(self.screen)
    def __del__(self):
        print("Удаление: " + self.__str__())

phone1 = Phones('touch screen', 3)
phone2 = Phones('touch screen', 2)
phone3 = Phones('not a touch screen', 20)

print(len(phone1))



#3
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def price_of_coffee (self):
        print(self.name, self.price)
    def __add__(self, other):
        print ('Сумма равна:', self.price+other.price)
    def __del__(self):
        print("Удаление: " + self.__str__())

coffee1 = Coffee('Латте', 250)
coffee1.price_of_coffee()
coffee2 = Coffee('Капучино', 200)
coffee2.price_of_coffee()
coffee1+coffee2

