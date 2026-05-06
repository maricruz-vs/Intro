def encontrar(cadena):
    """
    Función que encuentra la longitud de la palabra más corta y más larga en una cadena dada.
    Entradas: cadena (str): La cadena de texto a analizar.
    Salidas: Imprime la longitud de la palabra más corta y más larga.
    Restricciones: ninguna, si noy palabras validas el programa lo indica.
    """
    palabras = []
    palabra_actual = []
    for char in cadena:
        if char.isalpha():
            palabra_actual.append(char)
        else:
            if palabra_actual:
                palabras.append(''.join(palabra_actual))
                palabra_actual = []

    #se agrega la ultima palabra si la cadena termina con una letra, porque esto no se hace en el ciclo anterior
    if palabra_actual:
        palabras.append(''.join(palabra_actual))
    
    if not palabras:
        print("No se encontraron palabras validas.")
        return
    
    
    longitudes = [len(palabra) for palabra in palabras]
    
    mas_corta = min(longitudes)
    mas_larga = max(longitudes)
    
    print("Mas corta:", mas_corta)
    print("Mas larga:", mas_larga)
    

if __name__ == "__main__":
    cadena = input("Ingrese una cadena: ")
    encontrar(cadena)