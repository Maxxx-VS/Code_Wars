data = {'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
summa = 0
arr = []
# roman = str(input(("Введите римскую цифру: ")).upper()) # MDCLXVI #MM
roman = 'MMMCMXCIX'
roman_revers = roman[::-1]

for element in roman_revers:
    for key, value in data.items():
         if element == key:
             print(value)
             arr.append(value)
print (arr)



# for key, value in data.items():
#     for element in roman_revers:
#         print(data.fromkeys(element, value))
#         #print(element)
#         #print(data.values())
#         #print(data.items())
#         #print(data.keys())






        # print (roman_revers[element], "--->", element)
        # if roman_revers[element] == 'X' and roman_revers[element + 1] == "I":
        #     roman_revers[element] = 0




