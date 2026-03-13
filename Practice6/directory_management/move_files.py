import shutil

source = "PP2/Practice6/directory_management/Drectry/sometext.txt"
destination = "PP2/Practice6/directory_management/Drectry/SubDrec"

shutil.move(source, destination)
# shutil.copy()

print("File moved")