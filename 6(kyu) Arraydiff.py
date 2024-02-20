def array_diff(a, b):

    if a == []:
        return (a)

    elif b == []:
        return (a)

    else:
        for i in sorted(a):
            for j in sorted(b):
                if i == j:
                    a.remove(i)
                    break





    return (a)

array_diff([1,2,3], [1, 2])



