def bank(x,y):
     
     for i in range(y):
          x +=x/10
     return x
x = int(input("Введите размер вклада в руб: "))
y = int(input("Введите количество лет: "))
result = bank(x,y)
print(result, 'руб')