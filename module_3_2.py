def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    variants = (".com", ".net", ".ru")
    if "@" not in recipient or "@" not in sender:
        print (f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}!")
    elif recipient.endswith (variants) == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}!")
    elif sender.endswith (variants) == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}!")
    elif recipient == sender:
        print ("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com" :
        print (f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}!")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!","\n","Письмо успешно отправлено с адреса {sender} на адрес {recipient}!")
run = True
while run:
    print ("\n")
    print ("Если хотите отправить письмо, нажмите 1.")
    print ("Если хотите выйти из программы, нажмите 0.")
    print("\n")
    m = int(input("Введите цифру 0 или 1: "))
    if m == 1:
        message = input ("Введите сообщение:")
        recipient = input ("Введите почту получателя:")
        n = int(input("Кто отправляет: 1. university.help@gmail.com; 2. другая почта? Введите нужный вариант: "))
        if n == 1:
            send_email(message, recipient, sender = "university.help@gmail.com")
        if n == 2:
            sender_2 = input ("Введите почту отправителя: ")
            send_email (message, recipient, sender = sender_2)
    if m == 0:
        print ("До встречи!")
        break