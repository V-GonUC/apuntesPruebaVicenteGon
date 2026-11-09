
chefsRegistrar = 0

while chefsRegistrar <= 0:
    try:
        chefsRegistrar = int(input("Ingrese la cantidad de chefs a registrar: "))
        if chefsRegistrar <= 0:
            print ("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")      
    except:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")