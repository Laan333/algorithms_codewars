def generate_alphabt() -> tuple:
    alphabet:list = [chr(i) for i in range(97, 123)]
    points = range(1,len(alphabet))
    return alphabet, points


def high(x:str):
    alphabet, points = generate_alphabt()
    splited_list = x.split(' ')
    all_scores:list = []
    full_word_score = 0
    for i in range(len(splited_list)):
        for j in range(len(splited_list[i])):
            get_letter = splited_list[i][j]
            get_score_letter = alphabet.index(get_letter) + 1
            full_word_score += get_score_letter
        all_scores.append(full_word_score)
        full_word_score = 0
    max_score = max(all_scores)
    index_max_score = all_scores.index(max_score)
    return splited_list[index_max_score]

dt =high('bb d')