def get_count(sentence):
    data_vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    num_vowels_in_text = ''
    for letter in sentence:
        if letter in data_vowels:
            num_vowels_in_text += letter
    return len(num_vowels_in_text)

dt = get_count('bcdfghjklmnpqrstvwxz y')
print(dt)