def encode_LZW(input_file, output_file):
    with open(input_file, 'r') as file_in:
        data = file_in.read()

    dictionary = {chr(i): i for i in range(256)}
    s = ''
    encoded_data = []
    next_code = 256

    for char in data:
        c = char
        if s+c in dictionary:
            s = s+c
        else:
            encoded_data.append(dictionary[s])
            dictionary[s+c] = next_code
            next_code += 1
            s = c

    encoded_data.append(dictionary[s])
    with open(output_file, 'w') as file_out:
        file_out.write(' '.join(str(code) for code in encoded_data))

def decode_LZW(input_file, output_file):
    with open(input_file, 'r') as file_in:
        data = file_in.read()

    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    encoded_data = data.split(' ')
    decoded_data = ''
    
    s = None
    for input_code in encoded_data:
        k = int(input_code)
        entry = dictionary[k]
        decoded_data += entry

        if(s != None):
            dictionary[next_code] = s + entry[0]
            next_code += 1

        s = entry

    with open(output_file, 'w') as file_out:
        file_out.write(decoded_data)

import os

def check_file_size(file_path):
    return os.path.getsize(file_path)

input_file_path = 'input.txt'
encoded_file_path = 'encoded.txt'
decoded_file_path = 'decoded.txt'

encode_LZW(input_file_path, encoded_file_path)
decode_LZW(encoded_file_path, decoded_file_path)

print('Size of input file:', check_file_size(input_file_path), 'bytes')
print('Size of encoded file:', check_file_size(encoded_file_path), 'bytes')
print('Size of decoded file:', check_file_size(decoded_file_path), 'bytes')