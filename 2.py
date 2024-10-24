def counter(input_string):
    uppercase_count = 0
    lowercase_count = 0
    
    for char in input_string:
        if char.isupper():
            uppercase_count +=1
        elif char.islower():
            lowercase_count +=1
    
    return uppercase_count, lowercase_count

startstring = input("Введите строку: ")
uppercase_count, lowercase_count = counter(startstring)

print("Amount of lowercase letters :", uppercase_count)
print("Amount of uppercase letters :", lowercase_count)
