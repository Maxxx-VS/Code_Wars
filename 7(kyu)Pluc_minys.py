def catch_sign_change(lst):
    count = 0
    znac = lst[0]
    if znac < 0:
        for i in lst:
            if znac < 0 and i < 0 or znac > 0 and i > 0:
                znac = i
            elif znac > 0 and i < 0 or znac < 0 and i > 0 or i == 0:
                count += 1
                znac = i
    elif znac > 0:
        for i in lst:
            if znac > 0 and i > 0 or znac < 0 and i < 0:
                znac = i
            elif znac < 0 and i > 0 or znac > 0 and i < 0 or i == 0:
                count += 1
                znac = i





    print (count)

catch_sign_change([1,-2,-7,-4,4,-2,0,-3,3])