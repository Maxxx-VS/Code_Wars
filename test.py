arry = [5,1,2,3,4]
swap = True
c = 0


while swap:
    swap = False
    for i in range (len(arry) -1 ):
        if arry[i] > arry[i + 1]:
            arry[i], arry[i + 1] = arry[i + 1], arry[i]
            swap = True
print(arry)
print(arry_set)

for i in range (len(arry_set)):
    if arry[i] != arry_set[i]:
        c += 1
print (c)

