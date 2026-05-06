def unir(A, B):
    """
    Funcionn que recibe dos listas numericas ordenadas ascendentemente (A y B) y retorna una sola lista con todos los 
    elementos de ambas, también ordenados.
    Entradas: 
    A y B (list): Lista de numeros ordenada ascendentemente.
    Salidas: 
    list: Lista con todos los elementos de A y B, ordenados ascendentemente.
    """
    resultado = []
    while A and B:
        if A[0] < B[0]:
            resultado.append(A.pop(0)) 
        else:
            resultado.append(B.pop(0))
    
    # al que le sobren elementos, los agregamos al resultado
    resultado.extend(A)
    resultado.extend(B)


    print(resultado)


unir([1, 3, 5], [2, 4, 6])
unir([1, 2, 5], [2, 7, 9,13])
unir([], [2, 7, 9,13])