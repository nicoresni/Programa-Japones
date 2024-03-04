import csv
import random
from constantes import *
import gamelib


#ARMADOS DE DICCIONARIOS y LISTAS DE OPCCIONES***********************************************************************************************************************************

def diccionario_japones(ruta_archivo):
    """
    HAGO QUE CADA PALABRA TENGA UN DICCIONARIO, con la info de TIPO;UNIDAD;HIRAGANA;KATAKANA(si tiene)
    """
    with open(ruta_archivo,encoding="utf8") as diccionario_csv:
        diccionario = {}
        reader = csv.DictReader(diccionario_csv, delimiter=',')
        for linea in reader:
            unidad = linea["unidad"]
            palabra = linea["traduccion"]
            hiragana = linea["hiragana"]
            katakana = linea["katakana"]
            tipo = linea["tipo_palabra"]
            kanji = linea["kanji"]
            diccionario[palabra] = {"tipo":tipo,"unidad":unidad,"hiragana":hiragana,"katakana":katakana,"kanji":kanji}
    return diccionario

def palabras_por_unidad(diccionario):
    """
    DICCIONARIO DE PALABRAS POR UNIDAD
    """
    diccionario_unidad= {}
    for palabra,info in diccionario.items():
        unidad = info["unidad"]
        if unidad in diccionario_unidad:
            diccionario_unidad[unidad].append(palabra)
        else:
            diccionario_unidad[unidad] = [palabra]
    return diccionario_unidad


def palabras_por_tema(diccionario):
    """
    DICCIONARIO DE PALABRAS POR TIPO
    """
    diccionario_tipo = {}
    for palabra,info in diccionario.items():
        tipo = info["tipo"]
        if tipo in diccionario_tipo:
            diccionario_tipo[tipo].append(palabra)
        else:
            diccionario_tipo[tipo] = [palabra]
    return diccionario_tipo

def obtener_temas_disponibles(dict_temas):
    lista_temas = list(dict_temas.keys())
    opcciones_temas = ""
    for tema in lista_temas:
        tema = list(tema)
        tema[0] = tema[0].upper()
        tema = "".join(tema)
        opcciones_temas += f"-{tema}\n"
    return opcciones_temas

def obtener_diccionarios(ruta):
    japo_dict = diccionario_japones(ruta)
    unidades = palabras_por_unidad(japo_dict)
    tipos = palabras_por_tema(japo_dict)
    return japo_dict,unidades,tipos



#OBTENER PALABRAS DE DICCIONARIOS***********************************************************************************************

def obtener_palabras_de_diccionario_fijo(diccionario,seleccion,cantidad):
    """
    Recibe el Diccionario de UNIDAD o TIPOS, la seleccion y la cantidad, y devuelve la cantidad de palabras especificas pedidas.
    """
    words = random.sample(diccionario[seleccion],cantidad)
    return words

def obtener_palabras_de_diccionario_completo(diccionario,cantidad):
    """
    Recibe el diccionario de Palabras y cantidad, y devuelve la cantidad pedida
    """
    words = random.sample(list(diccionario.keys()),cantidad) #Me evito el DeprecationWarning
    return words



#ANALISIS DE CLICKS DE PANTALLA*************************************************************************************************************************

def analizar_click_inicial(x,y):
    opccion_x,opccion_y = POSICION_OPCCIONES
    dim_opc_x,dim_opc_y = OPCCIONES_DIMENCION

    indice = 0
    while True:
        if indice > 2: 
            break 
        if opccion_x<=x<=opccion_x+dim_opc_x and opccion_y<=y<= opccion_y+dim_opc_y:
            break
        indice += 1
        opccion_x += dim_opc_x + DIST_OPCIONES

    if indice == 3:
        return None
    
    return OPCIONES[indice]
    

#Pedir Datos al USUARIO*************************************************************************************************************************

def pedir_cantidad(diccionario_a_usar):
    limite_cant = len(diccionario_a_usar)
    mensaje = MENSAJE_PEDIR_NUMERO[0]
    while True:
        cantidad = gamelib.input(mensaje)
        if not cantidad:
            return cantidad
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if cantidad > 0 and cantidad < limite_cant:
                return cantidad
            mensaje = MENSAJE_PEDIR_NUMERO[1] 
            continue
        else:
            if cantidad == "TODO":
                return limite_cant
            mensaje = MENSAJE_PEDIR_NUMERO[1] 
            continue


def pedir_unidad():
    mensaje = MENSAJE_PEDIR_UNIDAD[0]
    while True:
        unidad = gamelib.input(mensaje)
        if not unidad:
            return unidad
        if unidad.isdigit():
            unidad = int(unidad)
            if unidad > 0 and unidad < CANTIDAD_DE_UNIDADES_DISPONIBLES+1:
                return unidad
            mensaje = MENSAJE_PEDIR_UNIDAD[1] 
            continue
        else:
            if unidad == "TODAS":
                return -1
            mensaje = MENSAJE_PEDIR_UNIDAD [1] 
            continue

def pedir_tipo(mensaje_opciones_disponibles,dict_temas):
    tema = gamelib.input("Ingrese una opccion de las disponibles o TODAS para práctica completa:\n"+mensaje_opciones_disponibles)
    if not tema:
        return tema
    lista_temas = list(dict_temas.keys())
    while tema.lower() not in lista_temas:
        tema = gamelib.input("Ingrese una opccion de las disponibles o TODAS para práctica completa:\n"+mensaje_opciones_disponibles)
    return tema.lower()

VOCALES_ACENTUADAS = ["á","Á","é","É","í","Í","ó","Ó","ú","Ú"]
VOCALES_SIMPLES = ["a","i","e","o","u"] 

def limpiar_cadena(cadena):
    cadena_nueva = ""
    for c in cadena:
        if c in VOCALES_ACENTUADAS:
            cadena_nueva += VOCALES_SIMPLES[VOCALES_ACENTUADAS.index(c)//2]
        else:
            cadena_nueva += c.lower()
    return cadena_nueva

#FUNCIONES DE PISTA a MOSTRAR -****************************************************************************************************************************************

def crear_pista_actual(palabra):
    palabra_secreta = []
    for c in palabra:
        if c == " ":
            palabra_secreta.append(" ")
        else:
            palabra_secreta.append("*")
    ayuda_por_turno = round(len(palabra) * PORCENTAJE_A_MOSTRAR)
    if ayuda_por_turno == 0:
        ayuda_por_turno = 1 
    return palabra_secreta,ayuda_por_turno

def cantidad_de_incognitas(palabra_secreta):
    contador = 0
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == "*":
            contador += 1
    return contador

def despejar_pista(palabra_act,palabra_secreta,ayudas_por_turno):
    ayudado = 0

    while True:
        letra = random.randrange(len(palabra_act))
        if cantidad_de_incognitas(palabra_secreta) <= ayudas_por_turno:
            return palabra_secreta
        if palabra_secreta[letra] == "*":
            palabra_secreta[letra] = palabra_act[letra]
            ayudado += 1
        if ayudado == ayudas_por_turno :
            break
    return palabra_secreta



