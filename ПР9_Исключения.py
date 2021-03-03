print('задача 1')
try:
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))
except (ValueError, NameError):
    print('была введена строка, нужно вводить числа')
else:
    print(a,"x2 + ", b,"x + ", c," = 0")
    d=b**2-4*a*c
    sqd=d** (1/2)
finally:
    print('ok')
    if d>0:
        print("уравнение имеет 2 корня, т.к. дискриминант больше 0")
        try:
            x1 = (b * (-1) + sqd) / (2 * a)
            x2 = (b * (-1) - sqd) / (2 * a)
        except ZeroDivisionError:
            print('деление на 0')
        else:
            print("x1 =", x1)
            print("x2 =", x2)
        finally:
            print('ok')
    elif d==0:
        print("уравнение имеет 1 корень, т.к. дискриминант равен 0")
        try:
            x=(b*(-1)+sqd)/(2*a)
        except ZeroDivisionError:
            print('деление на 0')
        else:
            print("x =", x)
        finally:
            print('ok')
    else:
        print("уравнение не имеет корней, т.к. дискриминант меньше 0")

print('задача 2')
s = str(input('Введите строку: '))
if len(s)>10:
    print(s[0:10])
else:
    print(s)

try:
    print(s[9])
except IndexError:
    print('значение не найдено')
finally:
    print('ok')

print('задача 3')
class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = Users('Maria',14)
try:
    user1.show_name()
except AttributeError:
    print('метод не найден')
finally:
    print('ok')

print('задача 5')
# raise - принудительный вызов исключения
try:
    a='привет'
    raise ValueError ('значение в этом случае не может быть строкой')
except:
    ValueError
    print('значение в этом случае не может быть строкой')

print('задача 6')
class Users:
    def __init__(self, name):
        self.name = name
        self.age = []
    def fill_age (self):
        try:
            self.age = int(input('Введите возраст: '))
            if self.age < 0:
                raise ValueError('Значение не может быть отрицательным')
        except ValueError:
            print('Значение не может быть отрицательным')
        else:
            print(self.age)

user1 = Users('Maria')
user1.fill_age()



