def iniciar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    
    poblacion_inicial = float(input("Ingrese poblacion actual (en miles de millones):"))
    incremento = float(input("Ingrese tasa de crecimiento (en porcentaje):"))

    print("CRECIMIENTO POBLACIONAL ANUAL")
    
    
    # 1) Poblacion: 7.98 Incremento: 0.08
    
    anio_poblacion_duplicada = None
    anio_poblacion_cuadruplicada = None
    
    poblacion_previa = poblacion_inicial
    
    seguir_iterando = True
    anio = 1
    while anio_poblacion_cuadruplicada is None:
        
        incremento_poblacion = poblacion_previa * incremento / 100
        poblacion_actual = poblacion_previa + incremento_poblacion

        if anio <= 100:
            print(str(anio) + ") Poblacion: " + str(round(poblacion_actual, 2)) +
                                                    " Incremento: " + str(round(incremento_poblacion, 2)))
        
        if anio_poblacion_duplicada is None and poblacion_actual >= poblacion_inicial * 2:
            # Una sola vez. La primera vez que esto sucede.
            anio_poblacion_duplicada = anio
        
        if anio_poblacion_cuadruplicada is None and poblacion_actual >= poblacion_inicial * 4:
            # Una sola vez. La primera vez que esto sucede.
            anio_poblacion_cuadruplicada = anio
        
        poblacion_previa = poblacion_actual
        
        anio += 1
        
    
    print("Poblacion duplicada en: " + str(anio_poblacion_duplicada))
    print("Poblacion cuadruplicada en: " + str(anio_poblacion_cuadruplicada))

    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    iniciar()
