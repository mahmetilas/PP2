with open('PP2/Practice6/file_handling/textfile.txt', 'a') as file:
    file.write('\nNow the file has more content!')
with open('PP2/Practice6/file_handling/textfile.txt') as file:
    for line in file:
        print(line, end='')

import shutil

shutil.copy('PP2/Practice6/file_handling/textfile.txt', 'PP2/Practice6/file_handling/backup.txt')