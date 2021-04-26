def iniciar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    
    poblacion_inicial = float(input("Ingrese poblacion actual (en miles de millones):"))
    incremento = float(input("Ingrese tasa de crecimiento (en porcentaje):"))
    
    print("CRECIMIENTO POBLACIONAL ANUAL")
    
    
    # 1) Poblacion: 7.98 Incremento: 0.08
    anio = 1
    poblacion_actual = 7.98
    incremento_poblacion = 0.08
    print(str(anio) + ") Poblacion: " + str(poblacion_actual) + " Incremento: " + str(incremento_poblacion) )
    
    

    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    iniciar()
