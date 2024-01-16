#def flatten_and_sort(array):
array = ["dog", "food", "a", "of"]
# array_new = []
# for i in array:
#     array_new.append(i)
# print(array_new)

https://github.com/Maxxx-VS/CodeWars.git

# swap = True
# c = 0
# while swap:
#     swap = False
#     for i in range (len(array_new) -1 ):
#         if array_new[i] > array_new[i + 1]:
#             array_new[i], array_new[i + 1] = array_new[i + 1], array_new[i]
#             swap = True
#
# print(array_new)

for i in range(1, len(array)):
    index = i
    while len(array[index - 1]) > len(array[index]) and index > 0:
        array[index], array[index - 1] = array[index - 1], array[index]
        index -= 1
print(array)