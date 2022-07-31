def print_sep(sep, sep_len):
    return sep * sep_len

sep = print_sep('*', 100)
text = 'Hello {} Func {}'.format(sep, sep)

print(text)