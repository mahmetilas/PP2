import os

if os.path.exists("PP2/Practice6/file_handling/backup.txt"):
  os.remove("PP2/Practice6/file_handling/backup.txt")
else:
  print("The file does not exist")