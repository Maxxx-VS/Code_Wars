
def count_bits(n):
    count = 0
    n1 = ""
    while n > 0:
        n1 = str(n % 2) + n1
        n = n // 2
    for i in n1:
        if i == '1':
            count += 1
    print(count)




count_bits(1234)

