INTENTOS_MAX = 7

def ahorcado():
    """Subrutina principal del juego ahorcado:
    Entradas: ninguna.
    Salidas: el juego de ahorcado.
    Restricciones: ninguna.
    """
    global INTENTOS_MAX
    limpiarPantalla()
    imprimirPantalla()
    continuar = True
    while continuar: 
        textoOriginal = leerTextoOriginal()
        #limpiarPantalla()
        texto = preparar(textoOriginal)
        intentadas = "" 
        intentos = 0
        ronda = 1
        while intentos < INTENTOS_MAX and not adivino(texto, intentadas):
            limpiarPantalla()
            imprimirRonda(texto, intentadas, intentos, ronda)
            letraIntento = leerIntento(intentadas)
            if aciertaIntento(texto, letraIntento):
                imprimirMensajeAcierto()
            else:
                imprimirMensajeNoAcierto()
                intentos +=1
            intentadas += letraIntento
            ronda+=1
        if adivino(texto, intentadas):
            imprimirMensajeVictoria(textoOriginal)
        else:
            imprimirMensajeDerrota(textoOriginal)
        continuar = leerJuegoNuevamente()
    imprimirDespedida()

def limpiarPantalla():
    """
    Subrutina que imprime lineas en blanco para limpiar la pantalla.
    Entradas: ninguna.
    Salidas: 10 lineas en blanco.
    Restricciones: ninguna.
    """
    print("\n"*10)

def imprimirPantalla():
    """
    Subrutina que imprime lineas en blanco para limpiar la pantalla.
    Entradas: ninguna.
    Salidas: mensaje de bienvenida.
    Restricciones: ninguna.
    """
    print("Bienvenido al juego de")
    print()
    print("    ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗")
    print("    ║   ║ ║   ║ ║   ║ ║   ║ ║   ║ ║   ║ ║   ║ ║   ║")
    print("    ║ A ║ ║ H ║ ║ O ║ ║ R ║ ║ C ║ ║ A ║ ║ D ║ ║ O ║")
    print("    ║   ║ ║   ║ ║   ║ ║   ║ ║   ║ ║   ║ ║   ║ ║   ║")
    print("    ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝")
    print("Creado por Maricruz Vasquez Sandi")

def leerTextoOriginal():
    """
    Funcion que lee de la consola la palabra o frase a ser adivinada y retorna como resultado el texto leido. 
    Entradas: texto del usuario.
    Salidas: texto ingresado.
    Restricciones: ninguna.
    """
    texto = input("Ingrese la palabra o frase a adivinar. Solo puede contener letras y espacios:\n")
    while not esTextoValido(texto):
        print("El texto solo puede contener letras y espacios.")
        texto = input("Ingrese la palabra o frase a adivinar. Solo puede contener letras y espacios:\n")
    return texto

def esTextoValido(texto):
    """
    Funcion booleana que dice si un string es un texto valido para adivinar en el juego.
    Entrada: texto a analizar.
    Salidas: True si el texto solo contiene letras o espacios, False otherwise.
    Restricciones: debe ser un string.
    """
    if type(texto) != str:
        raise Exception("El texto debe ser un string.")
    if texto == "":
        raise Exception("El texto no puede ser vacio.") 
    for letra in texto:
        if letra.lower() not in " aábcdeéfghiíjklmnñoópqrstuúüvwxyz":
            return False
    return True

def preparar(texto):
    """
    Convierte el texto a minisculas, sustituye acentos y elimina espacios al incio y al final.
    Entradas: texto a preparar.
    Salidas: texto preparado.
    Restricciones: texto debe ser un string.
    """
    if type(texto) != str:
        raise Exception("El texto debe ser un string.")
    texto = texto.lower()
    testo = texto.strip()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    texto = texto.replace("ü", "u")

    return texto


def adivino(texto, intentadas):
    """
    Funcion booleana que dice si el jugador adivino el texto.
    Entradas: 
        texto: texto preparado sin tildes ni acentos.
        intentadas: letras que el jugador ha intentado.
    Salidas: True si todas las entradas del texto ya han sido intentadas, False si no.
    Restricciones: 
        - texto deben ser strings de letras sin acentos.
    """
    if type(texto) != str or type(intentadas) != str:
        raise Exception("El texto y las intentadas deben ser strings.")
    if not esTextoValido(texto):  
        raise Exception("El texto contine caracteres no validos.")
    for letra in texto:
        if letra != " ":
            if letra not in intentadas:
                return False
    return True

def imprimirRonda(texto, intentadas, intentos, ronda):
    """
    Esta funcion imprimie los mensajes requeridos para ronda del juego. 
    Imprime el numero de ronda actual, un mensaje que indica las letras que ya fueron utilizadas, 
    cantidad de intentos falllidos y tambien escrube el texto enmascarado.
    Entradas: 
        texto: texto preparado sin tildes ni acentos.
        intentadas: letras que el usuario ha intentado.
        intentos: cantidad de intentos fallidos.
        ronda: numero de ronda por la que va el juego.
    Salidas: Impresion en pantalla de la informacion de la ronda.
    Restricciones: ninguna.
    """
    print()
    print("RONDA NUMERO: ", ronda)
    print("Letras que ya fueron utilizadas: ", intentadas)
    print("Cantidad de intentos fallidos: ", intentos)
    print()
    print(enmascarar(texto, intentadas))
    print()


def enmascarar(texto, intentadas):
    """
    Retorna un string con un guion bajo por cada letra no ha sido adivinada.
    Si una letra del texto aparece en las letras intentadas, entonces le agrega com otal en lugar del guion.
    Si el texto original tiene espacios, los sustituye con guiones normales.
    Entradas: 
        texto: texto preparado sin tildes ni acentos.
        intentadas: letras que el usuario ha intentado.
    Salidas: string con el texto enmascarado.
    Restricciones: ninguna.
    """
    listaPalabras = texto.split()
    resultado = ""
    for palabra in listaPalabras:
        for letra in palabra:
            if letra in intentadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        resultado += "- "
    return resultado[:-2]

def leerIntento(intentados):
    """
    Funcion que pide al usuario que escriba una letra para adivinar. Si ya se encuentra en las intentadas
    o no es una letra debe imprimir un mensaje de error y pedirle que ingrese otra letra.
    Lee de la consola el intento del usuario y retorna como resultado el intento leido.
    Entradas: letras que el usuario ha intentado.
    Salidas: letra ingresada por el usuario.
    Restricciones: el intento debe ser una letra que no haya sido intentada antes.
    """
    print()
    letra = input("Digite una letra:")
    letra = letra.lower()
    while len(letra) != 1 or letra not in "aaábcdeéfghiíjklmnñoópqrstuúüvwxyz" or letra in intentados:
        print("Por favor ingrese una letra que no haya intentado.")
        letra = input("Digite una letra:")
        letra = letra.lower()
    print()
    return letra

def aciertaIntento(texto, letra):
    """
    Funcion booleana que dice si un intento es correcto o no.
    Entradas: 
        texto: texto que se esta adivinando.
        letra: letra que el usuario intenta adivinar.
    Salidas: True si la letra esta en el texto, False si no.
    Restricciones: ninguna.
    """
    return letra in texto

def imprimirMensajeAcierto():
    print("¡Muy bien! Adivinaste una letra. :)")

def imprimirMensajeNoAcierto():
    print("¡Oh no! Esa letra no esta en el texto. :(")  

def imprimirMensajeVictoria(textoOriginal):
    print("¡Felicidades! Adivinaste el texto: ", textoOriginal)

def imprimirMensajeDerrota(textoOriginal):
    print("Ha perdido. El texto original era: ", textoOriginal)

def leerJuegoNuevamente():
    """
    Funcion que pregunta al usuario si quiere jugar nuevamente. 
    Solo acepta S o N como respuesta.
    Entradas: ninguna.
    Salidas: True si el usuario escribe S, False si no.
    Restricciones: ninguna.
    """
    print()
    respuesta = input("¿Desea jugar de nuevo? (S/N) ")
    respuesta = respuesta.lower()
    while respuesta not in ["s", "n"]:
        print("Por favor ingrese S o N.")
        respuesta = input("¿Desea jugar de nuevo? (S/N) ")
        respuesta = respuesta.lower()
    return respuesta == "s"

def imprimirDespedida():
    print("Gracias por jugar ahorcado. Nos vemos pronto. :)")

ahorcado()