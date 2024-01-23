def sort_cards(cards):
    arr_num, arr_let = [], []
    #cards_str = "".join(cards)

    for i in cards:
        if i.isdigit():
            arr_num.append(i)
        else:
            arr_let.append(i)
    arr_num_sort = sorted(arr_num)
    arr_let_sort = sorted(arr_let)

    print(arr_num_sort)
    print(arr_let_sort)

    for i in arr_let_sort:
        if i == "A":
            arr_num_sort.insert(0, i)

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



sort_cards(list('39A5TT824Q7J6K'))


# ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
#
# def sort_cards(cards):
#     return sorted(cards, key=ranks.index)