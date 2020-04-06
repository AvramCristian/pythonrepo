def curata_lista(x):
    lista_curatata = []
    for i in range(0, len(x)):
        if type(x[i]) == int:
            lista_curatata.append(x[i])
            print(lista_curatata)
        else:
            print("in pozitia", i,"lista ta contine string si a fost eliminat")
    return lista_curatata

print("lista curatata =", curata_lista([2,"erty",20, "c",5,6]))


