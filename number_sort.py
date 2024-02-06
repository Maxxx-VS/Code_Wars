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

# пузырьковая
swap = True
c = 0


while swap:
    swap = False
    for i in range (len(arry) -1 ):
        if arry[i] > arry[i + 1]:
            arry[i], arry[i + 1] = arry[i + 1], arry[i]
            swap = True
print(arry)

# вставкой
def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        arr[pos] = cursor

    print(arr)

insertion_sort([1, 5, 6, 11, 2])