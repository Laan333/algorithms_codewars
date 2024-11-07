ones = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9
}

teens = {
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19
}

tens = {
    "ten": 10, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
}

# Словари для больших чисел
large_numbers = {
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000
}
all_numbers = [tens, teens, ones]


def parse_int(string):
    splited_string = string
    total = 0
    current = 0
    if '-' in string:
        splited_string = string.replace('-', ' ')
    splited_string = splited_string.split(' ')
    for i in range(len(splited_string)):
        print(f'Текущее слово {splited_string[i]}')

        for j in range(len(all_numbers)):
            if splited_string[i] in list(all_numbers[j].keys()):
                current += all_numbers[j][splited_string[i]]
        if splited_string[i] in list(large_numbers.keys()):
            if splited_string[i] == 'thousand' or splited_string[i] == 'million':
                current *= large_numbers[splited_string[i]]
                total += current
                current = 0
            elif splited_string[i] == 'hundred':
                current *= large_numbers[splited_string[i]]
    total += current
    return total





number = parse_int('two hundred thousand three')
print(number)