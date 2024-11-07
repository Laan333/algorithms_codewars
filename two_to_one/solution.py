def longest(a1, a2):
    alphabet = [chr(i) for i in range(97, 123)]
    listed_data = []
    for i in alphabet:
        if i in a:
            print(f'{i} - a')
            listed_data.append(i)
        elif i in b:
            print(f'{i} - b')
            listed_data.append(i)
    return ''.join(listed_data)


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

dt = longest(a,b)

