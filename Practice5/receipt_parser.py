print('============\n============')
import re

mat1 = False
with open("raw.txt", "r", encoding="utf-8") as file:
    for line in file:
        if re.search('^ab*$', line):
            # print(line)
            mat1 = True

if mat1:
    print("Match")
else:
    print("No match")
# ================================================================================================================
print('============\n============')
import re

mat2 = False
with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if re.search('^ab{2,3}$', line):
            # print(line)
            mat2 = True

if mat2:
    print("Match")
else:
    print("No match")
# ================================================================================================================
print('============\n============')
import re

mat3 = False
with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if re.search('^[a-z]+(_[a-z]+)+$', line):
            print(line)
            mat3 = True

if mat3:
    print("Match")
else:
    print("No match")
# ================================================================================================================
print('============\n============')
import re

mat4 = False
with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if re.search('^[A-Z]([a-z]+)$',line):
            # print(line)
            mat4 = True

if mat4:
    print("Match")
else:
    print("No match")
# ================================================================================================================
print('============\n============')
import re

mat5 = False
with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if re.search('^a.*b$',line):
            print(line)
            mat5 = True

if mat5:
    print("Match")
else:
    print("No match")
# ================================================================================================================
print('============\n============')
import re

with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        x = re.sub(r'[ ,.]', ':',line)
        print(x, end='')
# ================================================================================================================
print('============\n============')
import re

def snake_to_camel(text):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)

with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line
        print(snake_to_camel(parts), end='')
# ================================================================================================================
print('============\n============')
import re
lst = []
with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        x = re.split('[A-Z]',line)
        lst.extend(x)
print(lst, end='')
# ================================================================================================================
print('============\n============')
import re

def insert_spaces(text):
    return re.sub(r'(?<!^)([A-Z])', r' \1', text)

with open('raw.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(insert_spaces(line), end='')
# ================================================================================================================
print('============\n============')
import re

def camel_to_snake(text):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()

text = input("Enter camelCase string: ")
print(camel_to_snake(text))