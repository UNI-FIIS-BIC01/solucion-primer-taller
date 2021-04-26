def iniciar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    
    # poblacion_inicial = float(input("Ingrese poblacion actual (en miles de millones):"))
    # incremento = float(input("Ingrese tasa de crecimiento (en porcentaje):"))
    
    poblacion_inicial = 7.9
    incremento = 1.05
    
    print("CRECIMIENTO POBLACIONAL ANUAL")
    
    
    # 1) Poblacion: 7.98 Incremento: 0.08
    
    anio_poblacion_duplicada = None
    anio_poblacion_cuadruplicada = None
    
    poblacion_previa = poblacion_inicial
    for anio in range(1, 101, 1):
        incremento_poblacion = poblacion_previa * incremento / 100
        poblacion_actual = poblacion_previa + incremento_poblacion

        print(str(anio) + ") Poblacion: " + str(round(poblacion_actual, 2)) +
                                                " Incremento: " + str(round(incremento_poblacion, 2)))
        
        if anio_poblacion_duplicada is None and poblacion_actual >= poblacion_inicial * 2:
            # Una sola vez. La primera vez que esto sucede.
            anio_poblacion_duplicada = anio
        
        poblacion_previa = poblacion_actual
        
    
    print("Poblacion duplicada en: " + str(anio_poblacion_duplicada))
    print("Poblacion cuadruplicada en: " + str(anio_poblacion_cuadruplicada))

    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    iniciar()
