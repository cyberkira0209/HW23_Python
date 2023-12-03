A = int(input("Введіть значення A: "))
B = int(input("Введіть значення B: "))
if A >= B:
    print("Помилка: A повинно бути менше за B")
else:
    p = 1
    for n in range(A, B + 1):
        if n % 2 == 0 and n % 3 == 0:
            p *= n
    print("Добуток чисел:", p)