print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 333

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("")
bool([])
bool({})
bool(())
bool(set())  
bool(0)
bool(0.0)
bool(None)
bool(False)

class myclass():
  def __len__(self):  #its like len()
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))