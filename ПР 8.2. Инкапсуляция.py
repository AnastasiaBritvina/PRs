'''Задача 1. Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и изменение данных реализуются через
вызовы методов. В объектно-ориентированном программировании принято имена методов для извлечения данных начинать со слова
get (взять), а имена методов, в которых свойствам присваиваются значения, – со слова set (установить).
Например, getField, setField.

Задача 2. Создать классы для травоядного животного и травы. Животное должно уметь поедать траву, если испытывает голод,
в противном случае отказываться от лакомства. Трава должна обладать питательностью, в зависимости от которой животное будет
насыщаться.

Задача 3. Создать класс для часов. Должна быть возможность установить время при создании объекта. Также необходимо
реализовать методы, с помощью которых можно добавлять по одной минуте/секунде или по одному часу к текущему времени. Помнить,
что значения минут и секунд не могут превышать 59, а часов 23.'''

'''Инкапсуляция
Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным). 
Инкапсуляция делает некоторые из компонент доступными только внутри класса.

Инкапсуляция в Python работает лишь на уровне соглашения между программистами о том, какие атрибуты являются общедоступными, 
а какие — внутренними.

Одиночное подчеркивание в начале имени атрибута говорит о том, что переменная или метод не предназначен для использования 
вне методов класса, однако атрибут доступен по этому имени.

Python 3 предоставляет 3 уровня доступа к данным:

публичный (public, нет особого синтаксиса, publicBanana);
защищенный (protected, одно нижнее подчеркивание в начале названия, _protectedBanana);
приватный (private, два нижних подчеркивания в начала названия, __privateBanana).

'''

# 1 задача
class Users:
    def __init__(self, id, name, password):
        self.__id = id
        self.__name = name
        self.__password = password
        self.password_of = []
        self.new_name = []
    def getField(self):
        print(self.id, self.name, self.password)
    def check(self):
        self.password_of = str(input('Введите пароль: '))
        if self.password_of == self.__password:
            print('Пароль введен верно')
        else:
            print('Пароль введен неверно')
    def setField(self):
        self.new_name = str(input('Введите новое имя: '))
        self.name = self.new_name
        print('Ваше прежнее имя: ', self.__name)
        print('Имя успешно изменено на: ', self.name)

user1 = Users(12345, 'Bob', '16524N')
#user1.getField() - при попытке получить данные возникает ошибка, т.к. они скрыты

user1.check() # тем не менее, функции выполняются, т.к. она только обрабатывает данные, а не выводит их
user1.setField()

#задача 2
class Animal:
    def __init__(self, an_name, need_for_food):
        self.an_name = an_name
        self.need_for_food = need_for_food

    def is_an_hungry(self):
        if self.need_for_food == 'да':
            print(self.an_name,':  голоден')
        else:
            print(self.an_name,':  сыт')


class Grass:
    def __init__(self, gr_name, value):
        self.gr_name = gr_name
        self.value = value

    def give_food(self, animal):
        if animal.need_for_food == 'да':
            print('Вы покормили :', animal.an_name, '.', 'Теперь уровень его сытости составляет :', self.value)
        else:
            print(animal.an_name, ': не хочет кушать')

animal1 = Animal('панда','да')
animal2 = Animal('Жираф','нет')

grass1 = Grass('бамбуковый стебель', '80')
grass2 = Grass('листья', '60')

animal1.is_an_hungry()
grass1.give_food(animal1)

animal2.is_an_hungry()
grass2.give_food(animal2)


#задача 3
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
