import re


def normalize_string(s: str):
    replace_chars = "\n\r\t,;"

    for char in replace_chars:
        s = s.replace(char, ' ')

    return s


def camel_to_snake(s: str):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()
