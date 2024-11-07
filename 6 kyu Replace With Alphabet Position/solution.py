def generate_alphabet_and_nums():
    alphabet = [chr(i) for i in range(97, 123)]
    nums = [i for i in range(1, 27)]
    return alphabet, nums

def alphabet_position(text:str):
    alphabet, nums = generate_alphabet_and_nums()
    full_text = ''
    for i in range(len(text)):
        if text[i].lower() in alphabet:
            find_index = alphabet.index(text[i].lower())
            full_text += str(nums[find_index])
            full_text += ' '

    return full_text.rsplit()
alphabet_position("The sunset sets at twelve o' clock.")