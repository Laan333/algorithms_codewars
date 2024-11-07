def printer_error(s:str):
    alphabet = [chr(i) for i in range(97, 110)]
    errors = [s[i] for i in range(len(s)) if s[i] not in alphabet]
    return f'{len(errors)}/{len(s)}'

s="aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(s))