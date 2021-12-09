def read_file(input):
    input_file = open(f'input_data\\{input}.txt', 'r')
    content = input_file.read()
    # convert to list and close
    read_file.content_list = content.split('\n')
    input_file.close()
    

