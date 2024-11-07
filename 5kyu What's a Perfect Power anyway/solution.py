

def isPP(n):
    power = 2
    num = 2
    on = True
    good_answers = []
    while on:
        data = num ** power #возводим в степень
        if data == n:#находим одинаковое число
            print(f'{num} ** {power}')
            good_answers.append([num, power])
        power += 1
        if data > n:
            power = 2
            num += 1
        if num > n ** 0.5:
            print('End')
            break
    if good_answers:
        return good_answers[0]
    else:
        return None

dt = isPP(81)
print(dt)