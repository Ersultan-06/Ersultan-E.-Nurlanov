x = "is Good"

def myfunc():
  global x
  x = "Good"

myfunc()

print("Python is " + x)