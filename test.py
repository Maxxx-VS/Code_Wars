arry = ['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']
swap = True
c = 0


while swap:
    swap = False
    for i in range (len(arry) -1 ):
        if arry[i] > arry[i + 1]:
            arry[i], arry[i + 1] = arry[i + 1], arry[i]
            swap = True
print(arry)





