def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fact(n-1)

input_number = int(input("Entrez un nombre entier : "))
factorial = recursive_fact(input_number)
print("La factorielle de", input_number, "est", factorial)