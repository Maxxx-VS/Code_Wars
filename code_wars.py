data = {'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
summa = 0
roman = 'MDCLXVI'

for i in range(len(roman) - 1):
    if data[roman[i]] < data[roman[i + 1]]:
        summa += data[roman[i]] * -1
        continue

    summa += data[roman[i]]

summa += data[roman[-1]]

return summa







