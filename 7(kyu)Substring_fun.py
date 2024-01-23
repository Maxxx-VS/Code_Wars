def nth_char(words):
    s = ""
    for i in range (len(words)):
        s += (f'{words[i][i]}')
    print(str(s))




nth_char(['Chad','Morocco','India','Algeria','Botswana','Bahamas','Ecuador','Micronesia'])