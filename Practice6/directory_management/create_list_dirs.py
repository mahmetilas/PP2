import os

# os.mkdir()
os.makedirs('PP2/Practice6/directory_management/Drectry/SubDrec', exist_ok=True)
open('PP2/Practice6/directory_management/Drectry/sometext.txt', 'x')
open('PP2/Practice6/directory_management/Drectry/SubDrec/sometext2.txt', 'x')
print('directory created')

print(os.listdir('PP2/Practice6/directory_management/Drectry'))

folder = "PP2/Practice6/directory_management"

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(root, file)
            print(full_path)