from reader import read_file

read_file('day2')

# part 1


def part_1(input):
    f_value = 0
    d_value = 0
    for i in input:
        if 'forward' in i:
            f_value += int(i[-1])
        elif 'down' in i:
            d_value += int(i[-1])
        elif 'up' in i:
            d_value -= int(i[-1])

    result = f_value * d_value
    print(result)


part_1(read_file.content_list)

# part 2


def part_2(input):
    h_pos = 0
    depth = 0
    aim = 0

    for i in input:
        if 'forward' in i:
            x = int(i[-1])
            h_pos += x
            depth += (x * aim)
        elif 'down' in i:
            y = int(i[-1])
            aim += y
        elif 'up' in i:
            z = -int(i[-1])
            aim += z
    result = h_pos * depth
    print(result)


part_2(read_file.content_list)
