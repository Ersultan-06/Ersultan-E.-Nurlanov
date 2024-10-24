import time
import threading
import math
def sqroot(number, delay):
    time.sleep(delay / 1000) 
    result = math.sqrt(number)
    #строка выводит результат в форматированной строке, отображая число, время задержки и квадратный корень.
    print(f"Квадратный корень из {number} после {delay} миллисекунд: {result}")

# Ввод времени задержки и числа
input_number = int(input("Введите число: "))
delay_time = int(input("Введите время задержки в миллисекундах: "))

# Создаем и запускаем поток
thread = threading.Thread(target=sqroot, args=(input_number, delay_time))
thread.start()

# Ожидаем завершения потока
thread.join()
