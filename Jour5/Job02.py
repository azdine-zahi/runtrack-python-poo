def recursive_puissance(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        temp = recursive_puissance(x, n/2)
        return temp * temp
    else:
        return x * recursive_puissance(x, n-1)

input_number = int(input("Entrez un nombre entier : "))
input_puissance = int(input("Entrez la puissance à laquelle élever ce nombre : "))
result = recursive_puissance(input_number, input_puissance)
print(input_number, "^", input_puissance, "=", result)
