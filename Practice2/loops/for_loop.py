fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

for x in range(6):
  print(x)

for x in range(2, 6): #[2, 3, 4, 5]
  print(x)

for x in range(2, 30, 3): #Increment the sequence with 3 (default is 1):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement