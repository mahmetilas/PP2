open("PP2/Practice6/file_handling/textfile.txt", 'x')
with open('PP2/Practice6/file_handling/textfile.txt', 'w') as file:
    file.write("Woops! I have deleted the content!")
with open('PP2/Practice6/file_handling/textfile.txt', 'r') as file:    
    print(file.readline())
    file.close()
