def to_weird_case(words):
    splited_words = words.split(' ')
    final = ""
    for peace in range(len(splited_words)):
        final += ' '
        for letter in range(len(splited_words[peace])):
            if letter % 2 == 0:
                final += splited_words[peace][letter].capitalize()
            else:
                final += splited_words[peace][letter].lower()
    return final.lstrip()


to_weird_case('Weird string case')