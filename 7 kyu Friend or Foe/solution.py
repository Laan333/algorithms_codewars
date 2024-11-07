def friend(x:list):
    best_friends:list = []
    for i in range(len(x)):
        if len(x[i]) == 4:
            best_friends.append(x[i])
    return best_friends

friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"])