# Find The Parity Outlier 6kyu

a = [2, 4, 0, 100, 4, 11, 2602, 36]
odd, even = [], []

for i in a:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)

if len(odd) > 1:
    c = even[0]
else:
    c = odd[0]
print(c)


# def romanToInt(s: str) -> int:
#     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     num = 0
#
#     for i in range(len(s) - 1):
#         if roman[s[i]] < roman[s[i + 1]]:
#             num += roman[s[i]] * -1
#             continue
#
#         num += roman[s[i]]
#
#     num += roman[s[-1]]
#
#     print(num)
# romanToInt("MMMDCCCLXXXVIII")
