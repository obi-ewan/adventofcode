from collections import defaultdict
import operator

file = open('input', "r")
data = file.readlines()

sdata = sorted(data)

guard_data = defaultdict(list)
on_duty_id = 0
minute_asleep = 0
minute_awake = 0

for line in sdata:

    if '#' in line:
        on_duty_id = ''.join([s for s in line[line.find('#'): (line.find('#')+8)] if s.isdigit()])

    if 'asleep' in line and on_duty_id != 0:
        minute_asleep = line.split(' ')[1][-3:-1]

    if 'wakes' in line and on_duty_id != 0:
        minute_awake = line.split(' ')[1][-3:-1]

        minutes_asleep = int(minute_awake) - int(minute_asleep)

        try:
            guard_data[on_duty_id][0] += minutes_asleep
        except IndexError:
            guard_data[on_duty_id].append(minutes_asleep)

        for minute in range(int(minute_asleep), int(minute_awake)):
            guard_data[on_duty_id].append(minute)


guard_longest_asleep = dict()

for guard in guard_data:
    d = guard_data[guard]

    if not guard_longest_asleep:
        guard_longest_asleep.update({guard: d[0]})

    for _, k in enumerate(guard_longest_asleep):
        if d[0] > guard_longest_asleep[k]:
            guard_longest_asleep = {guard: d[0]}


print(guard_longest_asleep)

for _, k in enumerate(guard_longest_asleep):
    d = guard_data[k]

    times = {minute: d.count(minute) for minute in d}
    occurs_most = max(times.items(), key=operator.itemgetter(1))[0]
    occurs_rate = max(times.items(), key=operator.itemgetter(1))[1]

    print(occurs_most)


# p2
most_common = defaultdict(list)

part2_data = guard_data

for guard in part2_data:
    d = part2_data[guard][1:]

    times = {minute: d.count(minute) for minute in d}
    occurs_most = max(times.items(), key=operator.itemgetter(1))[0]
    occurs_rate = max(times.items(), key=operator.itemgetter(1))[1]

    print(str(occurs_most) + " " + str(occurs_rate))

    if not most_common:
        most_common.update({guard: [occurs_most, occurs_rate]})

    for _, k in enumerate(most_common):
        if occurs_rate > most_common[k][1]:
            most_common = {guard: [occurs_most, occurs_rate]}
            print(most_common)


print(most_common)