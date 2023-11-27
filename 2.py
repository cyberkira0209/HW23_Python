s=int(input("Введіть двохзначне число "))
a=s//10%10
b=s%10
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print(a, b)
