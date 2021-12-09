from reader import read_file

read_file('day1')

# part 1

def num_increase(list_input):
    x = int(list_input[0])  # set x to first item on list
    z = 0  # num of increases
    for i in list_input:   # iterate list
        if int(i) > x:
            z += 1    # count increases
        x = int(i)    # reset x to current item
    print(z)

num_increase(read_file.content_list)
# part 2

second_list = []
window_size = 3

for i in range(len(read_file.content_list) - window_size + 1):
    t = read_file.content_list[i: i + window_size]
    tt = sum(map(int, t))
    second_list.append(tt)

num_increase(second_list)
