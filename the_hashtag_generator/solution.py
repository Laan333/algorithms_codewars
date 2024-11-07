def generate_hashtag(s:str):
    if s:
        new_str = s.title().strip().split()
        hshtag = f"#{''.join(new_str)}"
        if len(hshtag) > 140:
            return False
        return hshtag
    else:
        return False

print(generate_hashtag('Loooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))