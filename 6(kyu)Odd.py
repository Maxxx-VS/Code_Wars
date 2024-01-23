def solve(s):
    count = 0
    iter = len(s)
    for i in range (len(s)):
        n = int(s[i])
        if n % 2 != 0:
            count += i+1
    print(count)







solve("1347")