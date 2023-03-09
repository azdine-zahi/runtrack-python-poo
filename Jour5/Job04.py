def recursive_nombre_max(nombres):
    if len(nombres) == 1:
        return nombres[0]
    else:
        return max(nombres[0], recursive_nombre_max(nombres[1:]))

input_list = input("Entrez une liste de nombres : ")
nombres = [int(x) for x in input_list.split()]
nombres_max = recursive_nombre_max(nombres)
print("Le plus grand nombre dans la liste", nombres, "est", nombres_max)
