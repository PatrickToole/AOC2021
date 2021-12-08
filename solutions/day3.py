# read file
input_file = open('input_data\\2021-3a.txt', 'r')
content = input_file.read()
# convert to list and close
content_list = content.split('\n')
input_file.close()

bit_len = len(content_list[0])
cont_len = len(content_list)
targ = cont_len/2

gamma_list = []
epsilon_list = []

for x in range(bit_len):
    val = 0
    for i in range(cont_len):
        val += int(content_list[i][x])
    if val > targ:
        gamma_list.append(1)
        epsilon_list.append(0)
    else:
        gamma_list.append(0)
        epsilon_list.append(1)

gamma = int(''.join(map(str, gamma_list)),2)
epsilon= int(''.join(map(str, epsilon_list)),2)

print(gamma*epsilon)
