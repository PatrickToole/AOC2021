from reader import read_file

read_file('day3')



def part1(input):
    bit_len = len(input[0])
    cont_len = len(input)
    targ = cont_len/2

    gamma_list = []
    epsilon_list = []
    for x in range(bit_len):
        val = 0
        for i in range(cont_len):
            val += int(input[i][x])
        if val > targ:
            gamma_list.append(1)
            epsilon_list.append(0)
        else:
            gamma_list.append(0)
            epsilon_list.append(1)

    gamma = int(''.join(map(str, gamma_list)),2)
    epsilon= int(''.join(map(str, epsilon_list)),2)

    print(gamma*epsilon)

part1(read_file.content_list)