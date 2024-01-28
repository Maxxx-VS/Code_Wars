
def sort_array(source_array):
    sorted_array = [i for i in source_array if i % 2 != 0]
    sorted_array.sort()
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            sorted_array.insert(index, item)
    #return sorted_array
    print (sorted_array)

sort_array([5, 3, 2, 8, 1, 4])