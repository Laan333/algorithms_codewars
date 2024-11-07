import re



# def create_phone_number(n):
#     change_types = [str(i) for i in n]
#     first_letters = change_types[:3]
#     seconds_letters = change_types[3:6]
#     third_letters = change_types[6:10]
#     return (f"({''.join(first_letters)}) {''.join(seconds_letters)}-{''.join(third_letters)}")


def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)




print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))