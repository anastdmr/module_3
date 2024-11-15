calls = 0
def count_calls ():
    global calls
    calls += 1
    return calls
def string_info (my_str):
    count_calls()
    my_set = []
    my_set.append (len(my_str))
    my_set.append (my_str.upper())#верхний регистр
    my_set.append (my_str.lower())#нижний регистр
    return my_set
def is_contains(my_str, list_to_search):
    count_calls()
    if my_str.lower() in (item.lower() for item in list_to_search):
        search_result = True
    else:
        search_result = False
    return search_result
#сделаю меню
run = True
while run:
    print ("Меню:")
    print ("1. Ввести строку и получить ее длину, верхний/нижний регистр.")
    print ("2. Ввести строку и список и проверить ее вхождение в него.")
    print ("3. Посмотреть количество вызовов.")
    print ("0. Завершить программу.")
    m = int(input("Выберите нужный пункт:"))
    if m == 0:
        print ("Пока!")
        break
    elif m == 1:
        str_1 = input("Введите строку:")
        print(string_info(str_1))
    elif m == 2:
        str_2 = input("Введите строку:")
        set_1 = input("Введите список для поиска значения:").split()
        print(is_contains(str_2, set_1))
    elif m == 3:
        print ("Количество вызов функций = ",calls)