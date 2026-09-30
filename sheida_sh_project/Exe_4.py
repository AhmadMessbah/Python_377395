names = []

while True:
    name = input("Enter a name: ")

    if name == "exit":
        break

    names.append(name)

names.sort()
for name in names:
    print(name)