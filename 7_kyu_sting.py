def shorter_reverse_longer(a,b):
    if len(a) >= len(b):
        string = f"{b}{''.join(reversed(a))}{b}"
    else:
        string = f"{a}{''.join(reversed(b))}{a}"
    return string
shorter_reverse_longer("hello", "bau")