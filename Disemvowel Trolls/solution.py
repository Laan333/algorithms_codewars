
def disemvowel(string_):
    needed_letters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(needed_letters)):
        string_ = string_.replace(needed_letters[i], '')
    return string_

disemvowel('This website is for losers LOL!')