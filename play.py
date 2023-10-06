def choose_action():
    print("Выберите действие:")
    print("1. Осмотреть комнату")
    print("2. Искать ключи")
    print("3. Решить головоломки")
    action = input("Введите номер действия: ")
    return action

room_items = ["стул", "стол", "шкаф", "книга", "замок"]

keys = {"дверь в комнату": False, "дверь в коридор": False, "дверь на улицу": False}

puzzles = {"запертый шкаф", "закрытый ящик", "запертая дверь"}

def check_answer(answer):
    correct_answers = ["книга", "птица", "корабль"]
    if answer in correct_answers:
        return True
    else:
        return False

def search_keys():
    if "ключ" in room_items:
        keys["дверь в комнату"] = True
        room_items.remove("ключ")
        print("Вы нашли ключ от двери в комнату!")
    else:
        print("Ключей в комнате нет.")

def solve_puzzles():
    if "запертый шкаф" in puzzles:
        print("Вы решили головоломку со шкафом и нашли ключ от двери в коридор!")
        keys["дверь в коридор"] = True
        puzzles.remove("запертый шкаф")
    elif "закрытый ящик" in puzzles:
        print("Вы решили головоломку с ящиком и нашли кусок бумаги.")
        room_items.append("кусок бумаги")
        puzzles.remove("закрытый ящик")
    elif "запертая дверь" in puzzles:
        answer = input("Решите головоломку: что летает, плавает и ходит по земле? ")
        if check_answer(answer):
            print("Вы решили головоломку и открыли дверь!")
            keys["дверь на улицу"] = True
            puzzles.remove("запертая дверь")
        else:
            print("Неверный ответ.")

def print_room_info():
    print("Вы находитесь в комнате. В комнате есть:")
    for item in room_items:
        print("- " + item)
    print("Двери:")
    for key, value in keys.items():
        if value:
            print("- " + key + " (открыта)")
        else:
            print("- " + key + " (заперта)")


while True:
    print_room_info()
    action = choose_action()
    if action == "1":
        print("Вы осмотрели комнату.")
    elif action == "2":
        search_keys()
    elif action == "3":
        solve_puzzles()
    else:
        print("Неверный выбор действия.")
    
    if keys["дверь на улицу"]:
        print("Вы нашли выход и выбрались на свободу!")
        break