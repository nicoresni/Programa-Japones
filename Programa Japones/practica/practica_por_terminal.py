import random
from procesamiento import *
from constantes import *


#PRACTICA*************************************************************************************
def juego_con_palabras_elegidas(words):
    puntos = 0
    for p in words:
        completo = diccionario_japones(RUTA_CSV)
        k,h = completo[p]["katakana"],completo[p]["hiragana"]
        print(h,k)  #Esto tiene que mostrarse con GAMELIB

        palabra_secreta = []
        for c in p:
            if c == " ":
                palabra_secreta.append(" ")
            else:
                palabra_secreta.append("*")
        ayuda = round(len(p) * PORCENTAJE_A_MOSTRAR)#PORCENTAJE_A_MOSTRAR
        if ayuda == 0:
            ayuda = 1   
        print(ayuda)
        intento = 0
        for _ in range(INTENTOS_MAXIMOS):
            ayudado = 0
            while True:
                letra = random.randrange(len(p))
                if palabra_secreta[letra] == "*":
                    palabra_secreta[letra] = p[letra]
                    ayudado += 1
                if ayudado == ayuda :
                    break
            print("pista:","".join(palabra_secreta)) #Mostrarse con GAMELIB
            tot = INTENTOS_MAXIMOS
            rta = input("Ingresa la respuesta: ") #INPUT GAMELIB
            if rta == p:
                print("VAMO :)")    #GAMELIB
                puntos += (tot - intento)
                break
            intento += 1
            
            if intento == INTENTOS_MAXIMOS:
                print("mal... :(")  #GAMELIB
                print(f"la palabra era '{p}'") #GAMELIB
                break
        print(f"PUNTOS TOTALES:{puntos}/{len(words)*INTENTOS_MAXIMOS}") #GAMELIB
    #Hacer mensaje segun el porcentaje de acierto



japo_dict = diccionario_japones(RUTA_CSV)
unidades = palabras_por_unidad(japo_dict)
tipos = palabras_por_tema(japo_dict)
"""
palabras_1 = obtener_palabras_de_diccionario_fijo(tipos,"lectura",4)

#juego_con_palabras_elegidas(palabras_1) #El juego con Terminal es Usable"
print(len(unidades["1"]))
"""

"""
palabras_2 = obtener_palabras_de_diccionario_completo(japo_dict,5)
for p in palabras_2:
    print(limpiar_cadena(p))
"""


