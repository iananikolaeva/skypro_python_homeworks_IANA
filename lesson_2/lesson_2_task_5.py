def month_to_season(m):
    if m == 12 or 1 <= m <= 2:
     print("Зима")
    elif 3 <=m <= 5:
     print("Весна")
    elif 6 <= m <= 8:
      print("Лето")
    elif 9 <= m <= 11:
      print("Осень")
    else:
      print("Указанный месяц не существует")

m = int(input("Введите номер месяца: "))
month_to_season(m)