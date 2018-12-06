file = open('input', "r")
data = file.readlines()[0].strip()


# pt1
new_data = []

for i, c in enumerate(data):
    new_data.pop() if new_data and c == new_data[-1].swapcase() else new_data.append(c)

print(len(new_data))


# pt2
alphabet = 'abcdefghijklmnopqrstuvwxyz'
polymers = {}

for char in alphabet:
    new_data = []
    cdata = data.replace(char.lower(), '').replace(char.upper(), '')

    for i, c in enumerate(cdata):
        new_data.pop() if new_data and c == new_data[-1].swapcase() else new_data.append(c)

    polymers[char] = len(new_data)

print(polymers[min(polymers, key=polymers.get)])









