import re
#Напишите программу Python, которая сопоставляет строку, содержащую «a», за которой следует ноль или более «b».

# findall — возвращает список, содержащий все совпадения
# sub — заменяет одно или несколько совпадений строкой
# split - Разделить строку по каждому пробелу
# search - Возвращает объект Match, если в любом месте строки есть совпадение.

test1 ="apple"
x=re.findall(r"\S*ab*\S*", test1)
print(x)
print("-----------------------------")

#Напишите программу на Python, которая соответствует строке, содержащей "a", за которой следуют два-три "b".

test1 ="apple aabbus abbberation"
x=re.findall(r"\S*ab{2,3}\S*", test1)
print(x)
print("-----------------------------")

#Напишите программу на Python для поиска последовательностей букв, соединенных подчеркиванием.

test1 ="Under_Score notunderscore"
x=re.findall(r"\S*_\S*", test1)
print(x)
print("-----------------------------")

#Напишите программу на Python для поиска последовательностей из одной заглавной буквы, за которой следуют строчные буквы.
test1 ="Hello world"
x=re.findall(r"\S*[A-Z][a-z]\S*", test1)
print(x)
print("-----------------------------")

#Напишите программу на Python, которая сопоставляет строку, содержащую «a», за которой следует что угодно, заканчивающееся на «b».
test1 ="apasd asdvsb"
x=re.findall(r"\S*a\w*b\S*", test1)
print(x)
print("-----------------------------")

#Напишите программу на Python для замены всех пробелов, запятых и точек на двоеточие.

test1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam lectus risus."
x = re.sub(r"[.',\s]", ":", test1)
print(x)
print("-----------------------------")

#Напишите программу на Python для преобразования строки в формате Snake в строку в формате Camel.
test1 = "Pine_apple"
x = re.sub(r'_([\w])', lambda x: x.group(1).upper(), test1)
print(x)
print("-----------------------------")

#Напишите программу на Python,для разделения строки по заглавным буквам
test1 = "Hello World."
x = re.findall(r'[A-Z][^A-Z]*', test1)
print(x)
print("-----------------------------")

#Напишите программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.

test1 = "RickAndMorty"
x = re.sub(r'(\w)([A-Z])', lambda x: x.group(1) + " " + x.group(2), test1)
print(x)
print("-----------------------------")


#Напишите программу на Python для преобразования заданной строки в CamelCase в SnakeCase.
test1 = "NeverGonnaGiveYouUp"
x = re.sub(r'(\w)([A-Z])', lambda x: x.group(1) + "_" + x.group(2), test1)
print(x)
print("-----------------------------")

