arr = [1,2,3,3,3,5]
ex_arr = [2,3,4,1,5]
arr_return = []
for i in ex_arr:
    for j in arr:
        if i == j:
            arr_return.append(j)
print(arr_return)

# def example_sort(arr, example_arr):
#     return sorted(arr, key=example_arr.index)










#
# swap = True
# c = 0
#
#
# while swap:
#     swap = False
#     for i in range (len(arry) -1 ):
#         if arry[i] > arry[i + 1]:
#             arry[i], arry[i + 1] = arry[i + 1], arry[i]
#             swap = True
# print(arry)