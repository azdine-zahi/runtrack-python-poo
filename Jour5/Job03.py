def recursive_longueur_chaine(n):
    if n == "":
        return 0
    else:
        return 1 + recursive_longueur_chaine(n[1:])

input_string = input("Entrez une chaîne de caractères : ")
longueur = recursive_longueur_chaine(input_string)
print("La longueur de la chaîne '", input_string, "' est", longueur)
