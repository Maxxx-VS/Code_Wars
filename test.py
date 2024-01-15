def flick_switch(lst):
    flag = True
    arry = []
    for i in lst:
        if i != 'flick':
            arry.append(flag)
        else:
            if flag == True:
                flag = False
                arry.append(flag)
            else:
                flag = True
                arry.append(flag)

    print(arry)

flick_switch(['codewars', 'flick', 'code', 'wars'])