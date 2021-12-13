def read_file(input):
    input_file = open(f'input_data\\{input}.txt', 'r')
    content = input_file.read()
    # convert to list and close
    read_file.content_list = content.split('\n')
    input_file.close()
    

def read_file2(input):
    data_file = open(f'input_data\\{input}.txt', 'r')
    data = data_file.read()
    read_file2.data = data
    data_file.close()