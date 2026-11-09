
chefsRegistrar = 0


while chefsRegistrar <= 0:
    try:
        chefsRegistrar = int(input("Ingrese la cantidad de chefs a registrar: "))
        if chefsRegistrar <= 0:
            print ("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")      
    except:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")

for cantidadChefs in range(chefsRegistrar):
    validadorChefs = False
    
    while validadorChefs == False:
        codigoChef = input (f"Ingrese el código del chef {cantidadChefs+1}: ")
        if len (codigoChef) < 8 or " " in codigoChef :
            print ("¡Código inválido! El código debe tener al menos 8 caracteres y no contener espacios.")
        else:
            validadorChefs = True

    try:
        experienciaChef = int(input (f"Ingrese la experiencia del chef {cantidadChefs+1} (en años): "))
        if experienciaChef < 0:
            print ("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")  
    except:
        print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
