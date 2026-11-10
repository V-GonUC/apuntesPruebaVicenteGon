camarotesDisponibles = 120
op = 0
reservaCamarotes = 0 
historialReservas = 0
print ("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

while op != 5:    
        
        print ('=== MENÚ PRINCIPAL ===')
        print ('1. Camarotes disponibles.')
        print ('2. Reservar camarote.')
        print ('3. Cancelar camarote.')
        print ('4. Historial de reservas.')
        print ('5. Salir.')

            
        try:
            op = int(input('Ingrese una opción: '))
        except:
            op = 0
           
           
        
        if op < 1 or op > 5:
            print("¡Error de opción! Ingresa un número entero positivo del 1 al 5 para continuar.")
    
        match op:
            case 1:
                print(f"La cantidad de camarotes disponibles es: {camarotesDisponibles}")
        
            case 2:
                reservaValida = False
                while reservaValida == False:
                    try:
                        reservaCamarotes = int(input("Ingrese la cantidad de camarotes que desea reservar: "))
                        if reservaCamarotes <=0:
                            print("¡Error de reserva! Ingresa un número entero positivo para reservar camarotes.")
                        elif reservaCamarotes > camarotesDisponibles:
                            print("¡Error de reserva! No hay suficientes camarotes disponibles para reservar.")
                            reservaValida = True
                        else:
                            camarotesDisponibles -= reservaCamarotes
                            historialReservas += 1
                            print(f"¡Reserva exitosa!")
                            reservaValida = True
                    except:
                            print("¡Error de reserva! Ingresa un número entero positivo para reservar camarotes.")
            
            case 3:
                try:
                    liberarCamarotes = int(input("Ingrese la cantidad de camarotes que desea liberar: "))
                    if liberarCamarotes <= 0:
                        print("¡Error de cancelación! Ingresa un número entero positivo para liberar camarotes.")
                    elif liberarCamarotes > 120 - camarotesDisponibles:
                        print("¡Error de cancelación! No hay suficientes camarotes reservados para liberar.")       
                    else:
                        camarotesDisponibles += liberarCamarotes
                        historialReservas -= 1
                        print(f"¡Cancelación exitosa!")
                except:
                    print("¡Error de cancelación! Ingresa un número entero positivo para liberar camarotes.")
            
            case 4:
                print (f"El historial de reservas es: {historialReservas}")
            
            case 5: print ("Gracias por utilizar nuestro software, hasta la próxima.")

    
  



          


