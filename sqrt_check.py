import math

number = float(input("Введите число: "))
root = math.sqrt(number)
print(f"Корень числа: {root}")
if number >= 10:   # Проверка корени
    print("Число очень большое")
else:# Если больше 10, все в норме
    print("Число пределах нормы")
