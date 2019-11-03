file = open("inputJ2.txt", "r")
line = file.readline()

# python makes this very easy with the count() function
##happy = line.count(":-)")
##sad = line.count (":-(")
#
happy = 0
sad = 0
for i in range(len(line) - 2):
    if line[i:i + 3] == ":-)":
        happy = happy + 1
    elif line[i:i + 3] == ":-(":
        sad = sad + 1

if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")
