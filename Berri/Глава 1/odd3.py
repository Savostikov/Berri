word = "бутылка"
for beer_num in range(20, 0, -1):
    print(beer_num, word, "в стене бутылок")
    print(beer_num, word, "пива")
    print("возьми одну")
    print("пусти по кругу")
    if beer_num == 1:
        print("не осталось пива в стене бутылок")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "бутылку"
        print(new_num, word, "в стене бутылок.")
    print()    
