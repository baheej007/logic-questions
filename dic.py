file = open("data.txt", "r")
print(file.readline())   # Reads first line
print(file.readlines())  # Reads all lines as a list
file.close()