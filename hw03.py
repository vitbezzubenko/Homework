print("Введите первое число: ")
fizz = int(input())
print("Введите второе число: ")
buz = int(input())
print("Введите терминатор: ")
term = int(input())


for i in range(1, term+1):
  if i % buz == 0 and i % fizz == 0:
    print("fb")  # SG: договаривались же в строку выводить :-(
  elif i % buz == 0:  
    print("b")
  elif i % fizz == 0:
    print("f")
  else: 
    print(i)
# SG: 4-е пробела для отделения блока. Очень режет глаз