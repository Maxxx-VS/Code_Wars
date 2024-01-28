def catch_sign_change(lst):
    count = 0
    for i in range (len(lst)-1):
        if lst[i] >= 0 and lst[i+1] < 0 or lst[i] < 0 and lst[i+1] >= 0:
            count += 1
    print (count)

catch_sign_change([1,-2,-7,-4,4,-2,0,-3,3])