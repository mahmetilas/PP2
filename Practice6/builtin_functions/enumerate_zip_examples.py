fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(name, score)

value = 10
if isinstance(value, int):
    print("This is an integer")
# ================================================================
num = "25"
num_int = int(num)
print(num_int + 5)

age = 20
text = "Age: " + str(age)
print(text)

numbers = ["1", "2", "3", "4"]
numbers_int = list(map(int, numbers))
print(numbers_int)