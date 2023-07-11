def compressed(input_file, output_file):
    with open(input_file, 'r') as file_in:
        text = file_in.read()
    compressed_text = ''
    count = 1
    current_char = text[0]
        
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed_text += str(count) + current_char
            current_char = text[i]
            count = 1
        
    compressed_text += str(count) + current_char
    with open(output_file, 'w') as file_out:
        file_out.write(compressed_text)

def decompressed(input_file, output_file):
    with open(input_file, 'r') as file_in:
        text = file_in.read()

    decompressed_text = ''
    count = ''

    for char in text:
        if char.isdigit():
            count += char
        else:
            decompressed_text += int(count) * char
            count = ''
    
    with open(output_file, 'w') as file_out:
        file_out.write(decompressed_text)

import os

def check_file_size(file_path):
    return os.path.getsize(file_path)

input_file = 'input.txt'
compressed_file = 'compressed.txt'
compressed(input_file, compressed_file)

decompressed_file = 'decompressed.txt'
decompressed(compressed_file, decompressed_file)

print('Size of input file:', check_file_size(input_file), 'bytes')
print('Size of compressed file:', check_file_size(compressed_file), 'bytes')
print('Size of decompressed file:', check_file_size(decompressed_file), 'bytes')