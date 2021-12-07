# read file
input_file = open('input_data\\2021-2a.txt', 'r')
content = input_file.read()

content_list = content.split('\n')
input_file.close()
    
f_value = 0
d_value = 0

for i in content_list:
    if 'forward' in i:
        f_value += int(i[-1])
    elif 'down' in i:
        d_value += int(i[-1])
    elif 'up' in i:
        d_value -= int(i[-1])

result = f_value * d_value
print(result)
