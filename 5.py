A = int(input("Введіть значення A: "))
B = int(input("Введіть значення B: "))
n=0
for n in range(A, B + 1):
    print((str(n) + ' ') * n)