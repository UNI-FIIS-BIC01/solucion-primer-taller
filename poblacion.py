def iniciar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    
    # poblacion_inicial = float(input("Ingrese poblacion actual (en miles de millones):"))
    # incremento = float(input("Ingrese tasa de crecimiento (en porcentaje):"))
    
    poblacion_inicial = 7.9
    incremento = 1.05
    
    print("CRECIMIENTO POBLACIONAL ANUAL")
    
    
    # 1) Poblacion: 7.98 Incremento: 0.08
    
    poblacion_previa = poblacion_inicial
    for anio in range(1, 101, 1):
        incremento_poblacion = poblacion_previa * incremento / 100
        poblacion_actual = poblacion_previa + incremento_poblacion

        print(str(anio) + ") Poblacion: " + str(round(poblacion_actual, 2)) +
                                                " Incremento: " + str(round(incremento_poblacion, 2)))
        poblacion_previa = poblacion_actual
        
    
    
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    iniciar()
