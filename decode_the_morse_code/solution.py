dict_with_morse = {}


def decode_morse(morse_code):
    # Убираем лишние пробелы в начале и конце
    words = morse_code.strip().split("   ")  # Разбиваем на слова
    decoded_message = []

    for word in words:
        decoded_word = ''.join(MORSE_CODE[char] for char in word.split(" ") if char)
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)
print(decode_morse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))