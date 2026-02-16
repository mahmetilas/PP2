def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()
# --------------------------------------------------------------------------------------------------------------------------
# valid function names
# calculate_sum()
# _private_function()
# myFunction2()
# --------------------------------------------------------------------------------------------------------------------------
# Without functions, you would have to write the same calculation code repeatedly:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
# --------------------------------------------------------------------------------------------------------------------------
# With function
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))