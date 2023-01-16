hello_msg = print("Добро пожаловать на остров сокровищ!\nВаша миссия найти сокровище.")

choose_side = input("В какую сторону вы поплывёте? Налево или направо?	")
if choose_side.lower() == "направо":
    print("Игра окончена")
elif choose_side.lower() == "налево":
    choose_action = input("Плыть или ждать?	")
    if choose_action.lower() == "плыть":
        print("Игра окончена")
    elif choose_action.lower() == "ждать":
        choose_door = input("Выберите дверь? Красная, синяя или желтая?	")
        if choose_door.lower() == "синяя":
            print("Игра окончена")
        elif choose_door.lower() == "красная":
            print("Игра окончена")
        elif choose_door.lower() == "желтая":
            print("Вы выйграли!")