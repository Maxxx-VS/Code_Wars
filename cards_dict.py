def sort_cards(cards):
    all_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    dict_all_cards = {i: all_cards[i] for i in range(len(all_cards))}
    dict_cards = {i: cards[i] for i in range(len(cards))}
    print (dict_all_cards)
    print(dict_cards)

















sort_cards(list('39A5T824Q7J6K'))