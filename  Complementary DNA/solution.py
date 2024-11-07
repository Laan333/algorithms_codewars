def DNA_strand(dna):
    dict_of_data = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    dna_new = ''
    for i in range(len(dna)):
        if dna[i] in list(dict_of_data.keys()):
            dna_new += dict_of_data[dna[i]]
        else:
            dna_new += dna[i]
    return dna_new


test = DNA_strand('ATTGC')
print(test)