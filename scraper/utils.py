def normalize_string(s: str):
    replace_chars = "\n\r\t,;"

    for char in replace_chars:
        s = s.replace(char, ' ')

    return s
