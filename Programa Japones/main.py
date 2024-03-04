import interfaces_gamelib
import gamelib
import procesamiento
from constantes import *

#FUNCION JUEGO DE PREGUNTAS*****************************************************************************************************
def juego_preguntas(palabras,diccionario_grande): 
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    puntuacion = 0

    for i in range(len(palabras)):
        palabra_act = palabras[i]
        hiragana_act, katakana_act,kanji_act = diccionario_grande[palabra_act]["hiragana"],diccionario_grande[palabra_act]["katakana"],diccionario_grande[palabra_act]["kanji"]
        lista_pista,ayudas_por_turno = procesamiento.crear_pista_actual(palabra_act)
        intentos= 0
        lista_pista_despejada = procesamiento.despejar_pista(palabra_act,lista_pista,ayudas_por_turno)
        if len(palabra_act)<= 3:
            ayudas_por_turno = 0
        while True:
            gamelib.draw_begin()
            pista_a_mostrar = "".join(lista_pista_despejada)
            interfaces_gamelib.ventana_juego_preguntas(puntuacion,i,len(palabras),hiragana_act,katakana_act,kanji_act,pista_a_mostrar,intentos)

            if intentos == INTENTOS_MAXIMOS:
                    break
            else:
                respuesta_usuario = gamelib.input("Introduzca una Respuesta")
                respuesta_usuario = procesamiento.limpiar_cadena(respuesta_usuario)
                if respuesta_usuario ==  procesamiento.limpiar_cadena(palabra_act): 
                    puntuacion += (INTENTOS_MAXIMOS-intentos)
                    break
                else:
                    lista_pista_despejada = procesamiento.despejar_pista(palabra_act,lista_pista,ayudas_por_turno)
                    intentos += 1

        while True: #ENTER para Pasar a Siguiente Pregunta
                if intentos == INTENTOS_MAXIMOS:
                    gamelib.draw_text(f"MAL, la respuesta correcta era:",300,540,size=15,fill= RESPUESTA_INCORRECTA)
                    gamelib.draw_text(f"'{palabra_act}'",300,580,size=20,fill= RESPUESTA_INCORRECTA)
                else:
                    gamelib.draw_text(f"BIEN, la respuesta correcta era:",300,540,size=15,fill= RESPUESTA_CORRECTA)
                    gamelib.draw_text(f"'{palabra_act}'",300,580,size=20,fill= RESPUESTA_CORRECTA)
                ev = gamelib.wait()
                gamelib.draw_text("Para Saltear Palabra Presionar ENTER",300,10,bold=True,fill="white",size=9)
                if not ev:
                    break
                if ev.type == gamelib.EventType.KeyPress and ev.key == 'Return':
                    break
            
        gamelib.draw_end()

            
        
    gamelib.draw_end()
    return puntuacion
#FUNCION PANTALLA FINAL*****************************************************************************************************
def juego_final(puntaje,cantidad):
    #Mostrar puntaje y salir a menu principal con ESC
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
        gamelib.draw_begin()
        interfaces_gamelib.ventana_juego_final(puntaje,cantidad)
        
        ev = gamelib.wait()

        if not ev:
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break
    gamelib.draw_end()


#FUNCION PANTALLA INICIAL *****************************************************************************************************************************************
def main():
    japo_dict,dict_unidades,dict_temas = procesamiento.obtener_diccionarios(RUTA_CSV)
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    while gamelib.is_alive():
        gamelib.draw_begin()
        interfaces_gamelib.ventana_de_inicio()
        
        ev = gamelib.wait()

        if not ev:
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break
        if ev.type == gamelib.EventType.ButtonPress:
            x, y = ev.x, ev.y 
            seleccion = procesamiento.analizar_click_inicial(x,y)


            if seleccion == "CLASICO":
                cantidad = procesamiento.pedir_cantidad(japo_dict)
                if not cantidad:
                    continue
                palabras = procesamiento.obtener_palabras_de_diccionario_completo(japo_dict,cantidad)
                puntuacion = juego_preguntas(palabras,japo_dict)
                juego_final(puntuacion,cantidad)
                
            if seleccion == "TIPOS":
                mensaje_opciones_disponibles = procesamiento.obtener_temas_disponibles(dict_temas)
                tema = procesamiento.pedir_tipo(mensaje_opciones_disponibles,dict_temas)
                if tema == "TODAS":
                    cantidad = procesamiento.pedir_cantidad(japo_dict)
                    palabras = procesamiento.obtener_palabras_de_diccionario_completo(japo_dict,cantidad)
                elif not tema:
                    continue
                else:
                    cantidad_opciones_tema = dict_temas[tema]
                    cantidad = procesamiento.pedir_cantidad(cantidad_opciones_tema)
                    palabras = procesamiento.obtener_palabras_de_diccionario_fijo(dict_temas,tema,cantidad)
                if not cantidad:
                    continue
                puntuacion = juego_preguntas(palabras,japo_dict)
                juego_final(puntuacion,cantidad)
        
            if seleccion == "UNIDAD":
                unidad = procesamiento.pedir_unidad()
                if unidad == -1:
                    cantidad = procesamiento.pedir_cantidad(japo_dict)
                    palabras = procesamiento.obtener_palabras_de_diccionario_completo(japo_dict,cantidad)
                elif not unidad:
                    continue
                else:
                    diccionario_unidad = dict_unidades[str(unidad)]
                    cantidad = procesamiento.pedir_cantidad(diccionario_unidad)
                    palabras = procesamiento.obtener_palabras_de_diccionario_fijo(dict_unidades,str(unidad),cantidad)
                if not cantidad:
                    continue
                puntuacion = juego_preguntas(palabras,japo_dict)
                juego_final(puntuacion,cantidad)
            
        
        gamelib.draw_end()

gamelib.init(main)