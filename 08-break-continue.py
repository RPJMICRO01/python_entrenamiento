for numero in range(1,10):
    if numero % 2 == 0:
        print(numero)
        break

print("\n continue")
for numero in range(1,10):
    if numero % 2 == 1:
        continue
    print(numero)
