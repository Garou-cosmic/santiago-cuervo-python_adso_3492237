# pedimos los datos al usuario 
kilometros = float(input("ingresa el numero de kilometros recorridos: "))
litros = float(input("ingresa el numero de litros consumidos: "))
if kilometros != 0:
    # calculamos el consumo por kilometro
    consumo = litros / kilometros
    print("el consumo de combustible por kilometro es:", consumo, "litros/km")
else:
    print("error: no se puede calcular el consumo porque los kilometros recorridos son 0.")