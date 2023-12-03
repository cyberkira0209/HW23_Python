import random
n = int(input("Введіть n: "))
random_numbers = [random.randint(0, 10) for _ in range(n)]
print("Згенерований список:", random_numbers)
if 5 in random_numbers:
    print("True")
else:
    print("False")