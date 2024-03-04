import gamelib
from constantes import *
#FUNCION AUXILIAR COLOR-----------------

def color_mensaje_segun_puntuacion(puntuacion,total_palabras):

    puntaje_maxima = total_palabras*3
    evolucion_puntaje = puntaje_maxima*0.2
    indice_color = 0
    puntaje_comparativo = evolucion_puntaje*2
    while True:
        if puntuacion == puntaje_maxima:
            indice_color = 4
            break
        if puntuacion < puntaje_comparativo:
            break
        indice_color += 1
        puntaje_comparativo += evolucion_puntaje

    return COLORES_PUNTUACION[indice_color],MENSAJE_PUNTUACION[indice_color]

#FUNCIONES de VENTANA**********************************************************************************************
def ventana_de_inicio():
    gamelib.draw_rectangle(0,0,ANCHO_VENTANA,ALTO_VENTANA,fill="#FAE5D3")
    gamelib.draw_image(RUTA_TITULO,150,25)
    gamelib.draw_text("Para Salir del Programa Presionar ESC",300,10,bold=True,fill="black",size=9)
    gamelib.draw_text("-Seleccione qué Modo de Juego le Gustaría Jugar ガム STARTS ON!!!",300,260,bold=True,fill=COLOR_TEXTO_INICIO,size=13)
    gamelib.draw_rectangle(70,550,530,570,fill="white")
    gamelib.draw_text("-Puntaje: 1er Intento-> 3 puntos // 2do Intento -> 2 puntos // 3er Intento -> 1 punto",300,560,bold=True,size=9,fill=COLOR_TEXTO_INICIO)
    opccion_x,opccion_y = POSICION_OPCCIONES
    dim_opc_x,dim_opc_y = OPCCIONES_DIMENCION
    for i in range(len(OPCIONES)):
        gamelib.draw_rectangle(opccion_x,opccion_y,opccion_x+dim_opc_x,opccion_y+dim_opc_y,fill=OPCCIONES_COLOR[i])
        gamelib.draw_text(f"{OPCIONES[i]}",opccion_x+dim_opc_x/2,opccion_y+dim_opc_y/2,bold=True,size=15,fill="white")
        opccion_x += dim_opc_x + DIST_OPCIONES

    #EXPLICACIONES
    gamelib.draw_text("CLASICO: Elijes la Cantidad de Palabras al Azar(o Todas)",300,388,bold=True,fill=OPCCIONES_COLOR[0])
    gamelib.draw_text(", y tienes que Obtener la mejor puntuación posible.",300,388+20,bold=True,fill=OPCCIONES_COLOR[0])

    gamelib.draw_text("TIPOS: Elijes Tema(tipo de Palabra) para practicar con Cantidad de Palabras.",300,446,bold=True,fill=OPCCIONES_COLOR[1])
    gamelib.draw_text("Debes obtener la mejor puntuación posible.",300,446+20,bold=True,fill=OPCCIONES_COLOR[1])
    gamelib.draw_text(f"UNIDAD: Elijes Unidad del みんあのにほんご(Hasta unidad {CANTIDAD_DE_UNIDADES_DISPONIBLES})",300,504,bold=True,fill=OPCCIONES_COLOR[2])
    gamelib.draw_text(" y cantidad de palabras. Debes obtener la mejor punctuacion posible",300,504+20,bold=True,fill=OPCCIONES_COLOR[2])




def ventana_juego_preguntas(puntuacion,indice_act,palabras_tot,hiragana_act,katakana_act,kanji_act,pista_a_mostrar,intentos):
    gamelib.draw_rectangle(0,0,ANCHO_VENTANA,ALTO_VENTANA,fill="#2C4E71")
    gamelib.draw_text(f"Palabra {indice_act+1} de {palabras_tot}",100,30,bold=True,fill="white",size=15)

    #TEXTO GRANDE------------------------------------------
    gamelib.draw_rectangle(25,50,575,350,fill=COLOR_CUADRO_MUESTRA) 

    gamelib.draw_text("Hiragana",POSICION_MUESTRA_HOR,POSICION_MUESTRA_VER-ENCABEZADO,size=14,fill="black")
    gamelib.draw_text(f"{hiragana_act}",POSICION_MUESTRA_HOR,POSICION_MUESTRA_VER,size=30,fill= COLOR_HIRAGANA)

    gamelib.draw_text("Katakana",POSICION_MUESTRA_HOR,POSICION_MUESTRA_VER + DISTANCIA_MUESTRA_VER -ENCABEZADO,size=14,fill="black")
    gamelib.draw_text(f"{katakana_act}",POSICION_MUESTRA_HOR,POSICION_MUESTRA_VER + DISTANCIA_MUESTRA_VER,size=30,fill=COLOR_KATAKANA)
    gamelib.draw_text("Kanji",POSICION_MUESTRA_HOR,POSICION_MUESTRA_VER + DISTANCIA_MUESTRA_VER*2 -ENCABEZADO,size=14,fill="black")
    gamelib.draw_text(f"{kanji_act}",POSICION_MUESTRA_HOR,POSICION_MUESTRA_VER + DISTANCIA_MUESTRA_VER*2,size=30,fill=COLOR_KANJI) #Cuando lo hagas es size 30

    #PISTA-----------------------------------------------------
    gamelib.draw_rectangle(163,350,437,375,fill=COLOR_PISTA_ENCABEZADO)
    gamelib.draw_text("Pista para Resolver",300,362,fill="black")
    gamelib.draw_rectangle(25,375,575,420,fill=COLOR_PISTA)
    gamelib.draw_text(f"{pista_a_mostrar}",300,400,size=23,fill= COLOR_HIRAGANA)

    #PUNTUACION-------------------------------------------------
    gamelib.draw_rectangle(25,430,290,520,fill=COLOR_PISTA)
    gamelib.draw_text("Puntuacion",158,450,size=14,fill="black")
    gamelib.draw_text(f"{puntuacion}",158,490,fill="black",size=30)

    #INTENTOS-------------------------------------------
    gamelib.draw_rectangle(310,430,575,520,fill=COLOR_PISTA)
    gamelib.draw_text("Intentos",443,450,size=14,fill="black")
    gamelib.draw_text(f"{intentos}/{INTENTOS_MAXIMOS}",443,490,fill="black",size=30)





def ventana_juego_final(puntuacion,total_palabras):
    gamelib.draw_rectangle(0,0,ANCHO_VENTANA,ALTO_VENTANA,fill=COLOR_FINAL_FONDO)
    gamelib.draw_text("Para Volver al Menu Principal Presionar ESC",300,10,bold=True,fill="white",size=9)
    gamelib.draw_image(RUTA_FIN_JUEGO,25,25)
    gamelib.draw_text("Puntuación Final",300,300,bold=True,fill=COLOR_LETRAS_FINAL,size=22)

    #OBTENCION DE COLOR y MENSAJE 
    color_numeros_mensaje, mensaje_puntaje = color_mensaje_segun_puntuacion(puntuacion,total_palabras)
    
    #PUNTAJE
    gamelib.draw_rectangle(225,320,375,375,outline=COLOR_CUADRO_PUNTAJE,fill="white")
    gamelib.draw_text(f"{puntuacion}",300,348,bold=True,fill =color_numeros_mensaje,size=35)

    #CARTEL MENSAJE
    gamelib.draw_rectangle(25,390,575,430,outline=COLOR_CUADRO_PUNTAJE,fill="white")
    gamelib.draw_text(f"{mensaje_puntaje}",300,410,size=15,bold=True,fill=color_numeros_mensaje)


    #CUADRO PORCENTAJE EFECTIVIDAD
    gamelib.draw_text("Porcentaje",190,475,bold=True,fill=COLOR_LETRAS_FINAL,size=22)
    gamelib.draw_rectangle(135,500,245,580,outline=COLOR_CUADRO_PUNTAJE,fill="white")

    puntaje_maximo = total_palabras*3
    porcentaje = (puntuacion*100)/(puntaje_maximo)

    gamelib.draw_text(f"{round(porcentaje,2)}%",190,540,bold=True,fill =color_numeros_mensaje,size=23)

    #CUADRO TOTAL NETO
    gamelib.draw_text("Balance",410,475,bold=True,fill=COLOR_LETRAS_FINAL,size=22)
    gamelib.draw_rectangle(355,500,465,580,outline=COLOR_CUADRO_PUNTAJE,fill="white")
    gamelib.draw_text(f"{puntuacion}/{puntaje_maximo}",410,540,bold=True,fill =color_numeros_mensaje,size=20)
