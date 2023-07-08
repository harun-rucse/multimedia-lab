from decimal import Decimal, getcontext
from collections import Counter

getcontext().prec = 30

def generate_probability_range(symbols):
    symbol_count = Counter(symbols)
    prob_range = {}
    low = Decimal(0)

    for symbol, count in symbol_count.items():
        prob = Decimal(count) / Decimal(len(symbols))
        high = low + prob
        prob_range[symbol] = (low, high)
        low = high

    return prob_range

def encode(symbols, prob_range):
    low = Decimal(0)
    high = Decimal(1)
    range_width = Decimal(1)

    for symbol in symbols:
        symbol_low, symbol_high = prob_range[symbol]

        low = low + range_width * symbol_low
        high = low + range_width * symbol_high
        range_width = high - low
        # print(symbol, low, high)

    return (low, high)

def decode(encoded_message, prob_range, message_length):
    low, high = encoded_message
    message = ''

    for i in range(message_length):
        for symbol, symbol_range in prob_range.items():
            symbol_low, symbol_high = symbol_range
            symbol_width = symbol_high - symbol_low

            if low >= symbol_low and high <= symbol_high:
                message += symbol
                high = (high - symbol_low) / symbol_width
                low = (low - symbol_low) / symbol_width
                break
    
    return message


with open('input.txt', 'r') as file_in:
    input_str = file_in.read()

prob_range = generate_probability_range(input_str)
encoded_message = encode(input_str, prob_range)
decoded_message = decode(encoded_message, prob_range, len(input_str))


with open('encoded.txt', 'w') as file_out:
    file_out.write(str(encoded_message))

with open('decoded.txt', 'w') as file_out:
    file_out.write(decoded_message)
