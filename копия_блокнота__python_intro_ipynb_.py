# -*- coding: utf-8 -*-
"""Копия блокнота "python_intro.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f_pC4B67YcUVbErZHvCITzEGucPrVaP5

сперва лучше заглянуть в [перезентацию](https://github.com/nstsj/python_for_CL/blob/master/class1/dpo_1.pdf)

**Начинаем кодить:**

*the simplest way:* питон можно использовать как калькулятор
"""

2+3 # запустите эту ячейку

"""## основные операции с числами 
*(попробуйте сделать их в ячейке с кодом, подставляя вместо **x** и **y** какие-нибудь числа. Порядок операций можно задавать скобочками)*

x + y	Сложение

x - y	Вычитание

x * y	Умножение

x / y	Деление

x // y	Получение целой части от деления

x % y	Остаток от деления

-x	Смена знака числа

abs(x)	Модуль числа

x ** y	Возведение в степень

### сравнение:
== "равно" x == y (*x* равен *y*)

!= "не равно" x != y (*x* не равен *y*)

\> "меньше"

< "больше"

\>= "меньше или равно"

<= "больше или равно"
"""

# уруруррур
# (22+10)/3-15%2



# пример
(22+10)/3-15%2
# в каком порядке выполняются операции?

# придумайте ваш пример в этой ячейке и запустите ее

"""Порой для вычислений нам нужно сохранить результат. Для этого есть **переменные**. Переменные хранят ваши данные, мы *присваиваем им значение* через знак ="""

a = 5 
# мы создали переменную а и присвоили ей значение 5

"""Переменные бывают разных типов, мы сегодня поговорим о числах и строках.

* Переменные с типом "строка" обозначаются как str(сокращение от string)

* Числовые переменные делятся на два подтипа:
** int для целых чисел (45)
** float для дробных (45.821)

Проверить тип переменной можно с помощью функции ```type()```
где в скобках будет ваша переменная
"""

var=23
type(var)

# создаем переменную, присваиваем значение
var = 23
type(var) #проверяем ее тип

"""Если Вы работаете в PyCharm, то без функции 
```print()``` 
ваши команды не выведутся на печать (только исполнятся внутри интерпретатора). Если код срабатывает без ошибок, но результат не появляется, напишите 
```print()```, и поместите в скобки то, что хотите вывести на печать (это может быть переменная или функция)
"""

print(var) #выводим на печать значение, присвоенное переменной var
print(type(var)) # выводим на печать функцию, которая покажет тип переменной var

# создадим другую переменную, с другим типом
var2 = 34.09
type(var2) # проверяем тип

# создадим третью, с другим типом
var3 = "meow" # не забудьте, что строки пишутся в кавычках, двойных или одинарных
type(var3) # проверяем тип

"""## операции с переменными

с числовыми переменными можно делать все то, что мы делали с числами в первых ячейках (складывать, умножать, возводить в степень и тд)
"""

var+var2 #сложили первую и вторую переменную, т.к. они числовые

var2+var3 
# а здесь появляется ошибка, т.к. мы не можем складывать и вычитать и делить переменные разных типов (строку и число)

var*var3 #однако мы можем умножать строку на число (или на переменную, в которую сохранили число)
#  мы умножили строку "meow" на число 23, таким образом у нас появилась новая длинная строка, где meow повторяется 23 раза
print(var*var3)

"""Также мы можем пересохранять значения переменных"""

print(var) #функция print выводит на печать то, что мы запишем в ее скобках, у нас - переменная со значением 23
var = 2 # сохранили новое значение в уже существующую переменную var
print(var)
var = var * 10 # пересохраняем новое значение, которое равно старому, умноженному на 10
print(var)

line1 = "мама мыла "
line2 = "раму "
concat = line1+line2
concat1 = line2+line1

print(concat)
print(concat1)
len(concat)

a = 1
b = 3
f=a+b
print(f)

"""пересохранения переменных - это удобно, но будьте осторожны, когда мы придем к теме циклов, там этим лучше не злоупотреблять

### операции со строками

1. строки можно *конкатенировать*, присоединять друг к другу
"""

line1 = "я позвал в кино " # создали первую переменную
line2 = "этих людей " # создали вторую

concat = line2+line1 # новая переменная, в нее сохраним результат конкатенации первых двух переменных
another_concat = line1+line2 # а это еще одна, мы снова конкатенируем, но в обратном порядке (!)

# результаты! 
print(concat)
print(another_concat)

"""2. Выясняем длину строки функцией ```len()```"""

len(line1)

print(var*line1)



"""3. Дублирование строки (умножение на число)"""

# можно просто задав условия (строку и количество раз для повторения) в print()
print("добрый вечер "*2)

# можно то же самое, но сохранив строку в переменную
line1 = "привет "
print(line1*4)

# можно - сохранив все в переменные
line1 = "ну как дела "
count = 3
result = line1*count #здесь мы умножили строку на число и сохранили результат в переменную result
print(result)

"""4. доступ по индексу

строка  - это *итерируемый* объект (мы можем пройтись по каждому из его элементов). Мы можем работать с элементами строки. Для этого нам понадобятся **индексы**, номерá элемента. Индекс записывается в квадратных скобках [ ]

**!!** нумерация элементов начинается с 0, т.е. первый элемент имеет индекс [0]. 

Легкое правило запоминания - индекс всегда на 1 меньше чем настоящий номер элемента
"""

new = "психолингвистика"
print(new[0]) # хотим напечатать первый элемент в сторке
print(new[3]) # печатаем 4й элемент
print(new[-1])# хотим последний элемент, он же первый с конца

"""4.1. Извлечение среза

Иногда вам может понадобиться не вся последовательность элементов, а какой-то ее кусочек. Такой кусочек называниется **срез** (англ. slice)

Оператор извлечения среза: [x:y], гдк **x** – начало среза, а **y** – окончание;

Обратите внимание, что символ с номером **y** в срез не входит.

По умолчанию первый индекс равен 0, а второй - длине строки.
"""

print(new) # сначала напечатаем строку целиком

print(new[2:5]) #а теперь напечатаем элементы строки, с третьего по шестой

#можем сохранить слайс/срез в новую переменную
piece = new[5:-1] # сохраним элементы с шестого до последнего
print(piece) # давайте напечатаем сохраненное на предыдущем шаге

print(new[:3]) # напечатаетм слайс/срез элементов с первого до четвертого, четвертый не включая

print(new[3:]) # напечатаетм слайс/срез элементов с четвертого и до конца

print(new[:]) # напечатаетм слайс/срез элементов, но так как они не заданы, они берутся по дефолту - первый и последний

"""4.2. можно задать шаг, с которым нужно извлекать срез/слайс. Шаг обозначается третьим в квадратных скобках
    [начало:конец:шаг]
"""

# напечатаем строку с первого до последнего элемента(т.к. индексы не заданы), но шаг в обратном порядке
print(new[::-1]) 

# с первого до последнего элемента(т.к. индексы не заданы), шаг в прямом порядке, через три
print(new[::3])

# напечатаем строку с третьего до последнего элемента(т.к. индексы не заданы), но шаг в обратном порядке
print(new[2::-1])

"""Мы можем работать с элементами строк:"""

test = "подоконник"

print (test) # посмотрим на изначальное слово
print(test[:2]) # напечатаем срез/слайс из 1 и 2 элементов (технически, это с 1 по 3, 3 не включая) 
print(test[-3:-1]) # напечатаем срез/слайс элементов с последнего до третьего с конца
test = test[:2]+test[-3:-1] # конкатенируем их, (пере)сохраним в переменную
print(test) # печатаем значение переменной


# позапускайте ячейку несколько раз. Попробуйте объяснить, что происходит с результатами :)

"""# дополнительное
    мы об этом не говорили, но вот, что еще можно делать со строками:

5. делим строку методом ```split()```
"""

x = "Mr Johnson, you never stay in Paris, do you?"
print(x.split()) # если в скобках не задан разделитель, то разбивает по пробелам
print(x.split(',')) # сделаем разделителем запятую

# в результате получается список! Мы поговорим о списках на следующем занятии

"""6. меняем регистр"""

x = "Mr Johnson, do you live in London?"
print(x.upper()) # Преобразование строки к верхнему регистру
print(x.lower()) # Преобразование строки к нижнему регистру
print(x.capitalize()) # Переводит первый символ строки в верхний регистр, а все остальные в нижний
print(x.swapcase()) # Переводит символы нижнего регистра в верхний, а верхнего – в нижний
print(x.title()) # Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний

"""7. удаляем пробельные символы"""

x = "    В этой строке было слишком много пробелов    "
print(x.lstrip())	# Удаление пробельных символов в начале строки
print(x.rstrip())	# Удаление пробельных символов в конце строки
print(x.strip())	# Удаление пробельных символов в начале и в конце строки

"""8. состоит ли строка из.. (каждый из методов возвращает True или False, в зависимости оттого, выполняется ли условие)"""

x = "Hello"
print(x.isdigit())	# Состоит ли строка из цифр
print(x.isalpha())	# Состоит ли строка из букв
print(x.isalnum())	# Состоит ли строка из цифр или букв
print(x.islower())	# Состоит ли строка из символов в нижнем регистре
print(x.isupper())	# Состоит ли строка из символов в верхнем регистре
print(x.isspace())	# Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))
print(x.istitle())	# Начинаются ли слова в строке с заглавной буквы

"""## домашнее задание: 
(можно выполнять прям в ячейках, или скопировав код в 
PyCharm)
"""

# задание 1
# какие из этих строк можно конкатенировать? Какие умножать? Какие вычитать? Запишите все результаты, которые у Вас получились
a = 23
b = 34.02
c = "python is cool, "
d = "you are cool, too"
print(a+b)
print (a*b)
print (a-b)
print(a*c)
print (a*d)
concat=(c+d)
print (concat)

# задание 2
"""
Придумайте такую строку (на любом знакомом Вам языке),чтобы она состояла из трех других (повторы строки разрешены).
Напишите код. Если вы можете сделать это более, чем одним способом, напишите все способы
"""
a = "тучи, "
b = "тучи, "
c = "а тучи как люди"
concat = (a+b+c)
print(concat)
concat1 = (a*2+c)
print(concat1)
concat2 = (b*2+c)
print(concat2)
concat3 = (b+a+c)
print(concat3)

# задание 3
"""
Как из слова "апельсин" сделать слово "спаниель" ? 
Подсказка: вам помогут срезы и операции с индексами
"""
word = "апельсин"
word1 = (word[5])
word2 = (word[1])
word3 = (word[0])
word4 = (word[7])
word5 = (word[6])
word6 = (word[2:5])
print(word1+word2+word3+word4+word5+word6)

# задание 4 (выполняется по желанию)
"""элементы в переменной text преобразуйте в нижний регистр, а затем запишите наоборот, с последнего элемента по первый"""
text = "WOW,NOEL SEES LEON"

text = "WOW,NOEL SEES LEON"
text1=(text.lower())
print(text1[::-1])