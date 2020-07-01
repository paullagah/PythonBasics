file = open("teams.txt", "w")

for n in range(0):
    newline = "This is a new line"
    file.write(newline)

file = open("teams.txt", "r")
lines = file.readlines()
print(lines)

file.close()