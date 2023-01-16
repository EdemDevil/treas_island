hello_msg = print("Добро пожаловать на остров сокровищ!\nВаша миссия найти сокровище.")

choose_side = input("В какую сторону вы поплывёте? Налево или направо?	").lower()
if choose_side == "направо":
    print("Игра окончена")
elif choose_side) == "налево":
    choose_action = input("Плыть или ждать?	").lower()
    if choose_action == "плыть":
        print("Игра окончена")
    elif choose_action == "ждать":
        choose_door = input("Выберите дверь? Красная, синяя или желтая?	").lower()
        if choose_door == "синяя":
            print("Игра окончена")
        elif choose_door == "красная":
            print("Игра окончена")
        elif choose_door == "желтая":
            print("Вы выйграли!")
