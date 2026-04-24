  # Вход с помощью логина и пороля.
login = input("Введите имя: ").strip()
password = input("Введите пароль: ")
if login == "admin" and password == "1234":
    print("Вход разрешен")
else:
    print("Ошибка доступа")
