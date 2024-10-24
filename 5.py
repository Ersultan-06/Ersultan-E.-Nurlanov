def proverka(tuple):
    return all(tuple)
#all -> функция-проверка на истинность всех элемнтов тупла(кортежа)
example = [] 
a = int(input("Введите количество элементов: "))
for i in range(a) :
    d = int(input()) 
    example.append(d)
print(proverka(example))
