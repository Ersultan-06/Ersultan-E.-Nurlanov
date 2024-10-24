def celect(numbers):
    result = 1
    for chislo in numbers:
        result *= chislo
    return result

my_list = [] 
a = int(input("Введите количество чисел: "))
for i in range(a) :
    d = int(input()) 
    my_list.append(d)

result = celect(my_list)

print("List celect is" , result)