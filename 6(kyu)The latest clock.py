def latest_clock(a, b, c, d):
    res = [a, b, c, d]
    res_1 = []
    for i in res:
        if i == 0 or i == 1 or i == 2:
            res_1.append(i)
            res.remove(i)

    print(res)
    print(res_1)




latest_clock(1, 9, 8, 3)