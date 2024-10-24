def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

startstring = input("Введите строку: ")

if is_palindrome(startstring):
    print("Слово является палиндромом.")
else:
    print("Слово не является палиндромом.")
