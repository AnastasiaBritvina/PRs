'''Задача. Создать класс для часов. Должна быть возможность установить время при создании объекта.
Также необходимо реализовать методы, с помощью которых можно добавлять по одной минуте/секунде или по одному часу к текущему
времени. Помнить, что значения минут и секунд не могут превышать 59, а часов 23.

Задача . Реализуйте три класса «Квадрат», «Круг» и «Прямоугольник». В каждом классе должен быть реализован метод для расчета
площади. Перепишите код так, что бы реализация метода не зависела от класса (используется парадигма «полиморфизм»).
Для демонстрации работы создайте для каждого объект. Объекты объедините в список. Обойдите список циклом и для каждого класса
вызовите один и тот же метод для вывода площади.

Реализовать аналогичный код для расчета объема трех фигур. '''

'''Полиморфизм
Полиморфизм - разное поведение одного и того же метода в разных классах. Например, мы можем сложить два числа, и можем сложить 
две строки. При этом получим разный результат, так как числа и строки являются разными классами.
можем вызвать одну функцию, но для разных классов она будет работать по-разному.
'''

print('задача 1')
class Minutes:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def clock(self, other):
        if self.minutes > 58:
            other.hours = other.hours + 1
            self.minutes = 0
        else:
            self.minutes = self.minutes + 1
        print ('минуты: ', self.minutes)

class Hours:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def clock(self, other):
        if self.hours > 23:
            self.hours = 0
        else:
            other.minutes = other.minutes + 1
        print('часы: ', self.hours)

m1 = Minutes(10,59)
h1 = Hours(10,59)
m1.clock(h1)
h1.clock(m1)


print('задача 2')
print('площади фигур')
class Square:
    def __init__(self, name, side_of_square):
        self.side_of_square = side_of_square
        self.name = name
    def calc (self):
        return ('площадь фигуры: ', self.name, self.side_of_square ** 2)

class Round:
    def __init__(self, name, radius):
        self.radius = radius
        self.name = name
    def calc (self):
        return ('площадь фигуры: ', self.name, 3.14 * (self.radius ** 2))

class Rectangle:
    def __init__(self, name, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2
        self.name = name
    def calc (self):
        return ('площадь фигуры: ', self.name, self.side_1 * self.side_2)

square_1 = Square('квадрат', 3)
round_2 = Round('круг', 2)
rectangle_3 = Rectangle('прямоугольник', 4, 6)

list_1 = [square_1, round_2, rectangle_3]
for i in list_1:
    print(i.calc())

print('объемы фигур')
class Square_V:
    def __init__(self, name, side_of_square):
        self.side_of_square = side_of_square
        self.name = name
    def calc_v (self):
        return ('объем фигуры: ', self.name, self.side_of_square ** 3)

class Round_V:
    def __init__(self, name, radius):
        self.radius = radius
        self.name = name
    def calc_v (self):
        return ('объем фигуры: ', self.name, 4/3 * 3.14 * (self.radius ** 3))

class Rectangle_V:
    def __init__(self, name, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = name
    def calc_v (self):
        return ('объем фигуры: ', self.name, self.side_1 * self.side_2 * self.side_3)

square_V = Square_V('куб', 2)
round_V = Round_V ('шар', 3)
rectangle_V = Rectangle_V ('параллелепипед', 3, 1, 5)


list_v = [square_V, round_V, rectangle_V]
for j in list_v:
    print(j.calc_v())