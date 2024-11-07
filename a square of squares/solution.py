#
# def is_valid_walk(walk:list[str]):
#     dict_of_minus_operations = {'s':'n', 'n':'s', 'e':'w', 'w':'e'}
#     pos = 0
#     if len(walk) == 10:
#         gen_massives = [walk[i:i + 2] for i in range(0, len(walk), 2)]
#         for i in range(len(gen_massives)):
#             pos += 1
#             if dict_of_minus_operations[gen_massives[i][0]] == gen_massives[i][1]:
#                 pos -= 1
#             print(dict_of_minus_operations[gen_massives[i][0]] == gen_massives[i][1])
#             print(gen_massives)
#         if pos != 0:
#             return False
#         else:
#             return True
#     else:
#         return False

# def is_valid_walk(walk:list[str]):
#     dict_of_minus_operations = {'s':-1, 'n':1, 'e':1, 'w':-1}
#     pos = 0
#     last_symbol:str
#     last_symbol = ""
#     if len(walk) == 10:
#         for i in range(len(walk)):
#             pos += dict_of_minus_operations[walk[i]]
#             print(dict_of_minus_operations[walk[i]])
#         if pos == 0:
#             return True
#         else:
#             return False

def is_valid_walk(walk:list[str]):
    print(walk.count('w'), walk.count('e'), walk.count('s'), walk.count('n'))
tst = is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
print(tst)