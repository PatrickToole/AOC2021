# read file
input_file = open('input_data\\2021-1a.txt', 'r')
content = input_file.read()
# convert to list and close
content_list = content.split('\n')
input_file.close()

# part 1


def num_increase(list_input):
    x = int(list_input[0])  # set x to first item on list
    z = 0  # num of increases
    for i in list_input:   # iterate list
        if int(i) > x:
            z += 1    # count increases
        x = int(i)    # reset x to current item
    print(z)


num_increase(content_list)


# part 2

second_list = []

window_size = 3

for i in range(len(content_list) - window_size + 1):
    t = content_list[i: i + window_size]
    tt = sum(map(int, t))
    second_list.append(tt)


num_increase(second_list)
