def criba(m):
    """
    Funcion que implementa la Criba de Eratóstenes para encontrar todos los números primos menores o 
    iguales a un numero entero m dado.
    Entradas: m (int): Un numero entero mayor que 2.
    Salidas: list: Una lista con los números primos de 2 a m.
    Restricciones:
    m debe ser un entero.
    """
    if type(m) != int or m<2:
        raise ValueError("m debe ser un entero menor o igual a 2.")
    
    #lista con True en todas las posiciones, excepto en 0 y 1 al principio
    es_primo = [True] * (m + 1)
    es_primo[0] = es_primo[1] = False
    
    actual = 2
    while actual*actual <= m:
        if es_primo[actual]:
            for multiplo in range(actual*actual, m + 1, actual):
                es_primo[multiplo] = False
        actual+=1
    
    primos =[num for num in range(2, m + 1) if es_primo[num]]
    
    return primos


if __name__ == "__main__":
    m = int(input("Ingrese un numero entero M > 2: "))
    try:
        primos = criba(m)
        print(f"Numeros primos entre 2 y {m}: {primos}")
    except ValueError as e:
        print(e)
    