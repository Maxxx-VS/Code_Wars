def sort_cards(cards):
    arr_num, arr_let = [], []
    cards_str = "".join(cards)
    for i in cards_str:
        if i.isdigit():
            arr_num.append(i)
        else:
            arr_let.append(i)
    arr_num_sort = sorted(arr_num)
    arr_let_sort = sorted(arr_let)
    for i in arr_let_sort:
        if i == "A":
            arr_num_sort.insert(0, i)
            del arr_let_sort[0]
    for i in arr_let_sort:
        if i == 'T':
            arr_num_sort.append(i)
    for i in arr_let_sort:
        if i == 'J':
            arr_num_sort.append(i)
    for i in arr_let_sort:
        if i == 'Q':
            arr_num_sort.append(i)
    for i in arr_let_sort:
        if i == 'K':
            arr_num_sort.append(i)



    print(arr_num_sort)



sort_cards(list('39A5T824Q7J6K'))