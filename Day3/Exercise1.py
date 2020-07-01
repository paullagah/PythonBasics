file = open("teams.txt", "w")
teams = ["Celtic", "Rangers", "Hearts", "Hibs", "Morton", "Cali-Thistle"]

for line in range (0,6):
    newteam = "Team Added: " + str(teams[line]) + "\n"
    file.write(newteam)

file = open("teams.txt", "r")

print(file.readline())
file.readline()
file.readline()
print(file.readline())

file.close()
