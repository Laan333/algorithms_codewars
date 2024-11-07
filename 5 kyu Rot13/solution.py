def generate_alphabt() -> list[str]:
    alphabet_lower:list = [chr(i) for i in range(97, 123)] * 2
    alphabet_higher:list = [chr(i) for i in range(65, 91)] * 2
    return alphabet_lower + alphabet_higher


def rot13(message:str) -> str:
    alphabet:list = generate_alphabt()
    full_str = ''
    for letter in message:
        if letter in alphabet:
            index_in_list = alphabet.index(letter)
            full_str += alphabet[index_in_list + 13]
        else:
            full_str += letter
    return full_str
rot13('A bB zZ 1234 *!?%')