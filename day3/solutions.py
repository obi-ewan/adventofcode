file = open('input', "r")
data = file.readlines()

useable_data = {}

for line in data:
    short_line = line.replace('@ ', '')
    id, position, dimensions = short_line.split(' ')
    useable_data[id.strip('#')] = [position.strip(':'), dimensions.strip('\n')]
    b = 2

grid_width = 0
grid_height = 0

for key in useable_data:
    item = useable_data[key]
    width = int(item[0].split(',')[0]) + int(item[1].split('x')[0])
    if width > grid_width:
        grid_width = width

    height = int(item[0].split(',')[1]) + int(item[1].split('x')[1])
    if height > grid_height:
        grid_height = height


matrix = [['*'] * (grid_height + 1) for i in range((grid_width + 1))]


# find overlapping claims
for key in useable_data:
    item = useable_data[key]

    row_start = int(item[0].split(',')[1])
    row_end = row_start + int(item[1].split('x')[1])

    column_start = int(item[0].split(',')[0])
    column_end = column_start + int(item[1].split('x')[0])

    for row in range(row_start, row_end):
        for column in range(column_start, column_end):
            cell = matrix[row][column]
            if cell == "*":
                matrix[row][column] = key
            elif cell in useable_data.keys():
                matrix[row][column] = "x"

total = 0

for row in matrix:
    total += row.count('x')

print(total)

# find unique claim
unique_data = useable_data.copy()

for key in useable_data:
    item = useable_data[key]

    row_start = int(item[0].split(',')[1])
    row_end = row_start + int(item[1].split('x')[1])

    column_start = int(item[0].split(',')[0])
    column_end = column_start + int(item[1].split('x')[0])

    for row in range(row_start, row_end):
        for column in range(column_start, column_end):
            cell = matrix[row][column]
            if cell == 'x':
                try:
                    unique_data.pop(key)
                except KeyError:
                    continue


print(unique_data)



