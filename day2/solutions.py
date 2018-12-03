file = open('input', "r")

data = file.readlines()

contains_2 = 0
contains_3 = 0

for line in data:

    has_checked_2 = False
    has_checked_3 = False

    for char in line:
        if line.count(char) == 2 and has_checked_2 is False:
            contains_2 += 1
            has_checked_2 = True

        elif line.count(char) == 3 and has_checked_3 is False:
            contains_3 += 1
            has_checked_3 = True


print(contains_2 * contains_3)

# part 2
same_string = ''

for string in data:
    for string_to_compare in data:
        correct_string = ''
        if string_to_compare is not string:
            for index, char in enumerate(string):
                if char == string_to_compare[index]:
                    correct_string += char
            if len(correct_string) > len(same_string):
                same_string = correct_string

print(same_string)


