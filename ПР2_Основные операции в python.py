# Задание №2
print('задача про календарь аборигенов')
d=str(input("Введите число ")) #вводим день рождения аборигена
m2=str(input("Введите номер месяца ")) #вводим месяц рождения аборигена. По нашему календарю
m=int(m2) #нужно преобразовать введенный нами номер месяца, на их календарь
if  m<=2: #получается, что их календарь сдвинут на 2. Если введенный нами месяц 1 или 2
    m=m+10 #к введенному месяцу нужно прибавить 10. Получим 11 и 12 месяцы по их календарю
else:
    m=m-2 #в противном случае, если мы ввели номер месяца от 3 до 12, необходимо будет отнять 2. Так получим 1-10 месяцы
x=str(input("Введите год ")) #вводим год рождения аборигена
c=x[0:2] #первые две цифры года = количеству столетий
y=x[2:len(x)] #остальные = количество лет
day=int(d)+((13*m-1)//5)+int(y)+(int(y)//4+int(c)//4-2*int(c)+777) #подставляем в формулу, преобразуя строковые данные в числовые
print(day%7) #выводим ответ, узнав остаток от деления на 7 получившегося из формулы значения



# Задание №3
print('работа со строкой')
stroka=str(input())
print('третий символ строки : ', stroka[2]) #третий символ строки имеет индекс 2
print('предпоследний символ : ', stroka[-2]) #предпоследний символ - это второй символ с конца строки
print('первые 5 символов: ', stroka[0:5]) #используя срезы, выводим первые 5 символов. 0 - начало, 5 - конец
print('вся строка, кроме последних двух символов: ', stroka[0:-2]) #0 - начало, первый элемент, -2 - конец среза, 2й элемент с конца строки
print('все символы с четными индексами: ', stroka[::2]) #мы можем не указывать начальное и конечное значение, т.к. по умолчанию возьмется вся строка, от ее первного элемента до последнего. Указываем только шаг - 2
print('все символы с нечетными индексами: ', stroka[1:len(stroka):2]) #здесь уже нужно указать начальное и конечное значение, т.к. берется не вся строка, а все значения, кроме первого, с индексом 0. Так же указываем шаг
print('строка в обратном порядке: ',stroka[::-1]) #чтобы вывести строку в обратном порядке, нужно установить шаг -1. Т.е. пойдем с первого с конца элемента строки
print('длина строки: ', len(stroka)) #узнаем длину данной строки

