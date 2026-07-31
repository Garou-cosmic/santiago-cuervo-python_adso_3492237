comensales = int(input("intruduce el numero de comensale: "))
patatas_gramos = 200 * comensales
patatas_kilos = patatas_gramos / 1000
huevos = 5 * patatas_kilos
cebolla_gramos = 300 * patatas_kilos
#mostramos resultados 
print("ingredientes necesarios para", comensales, "comensales: ") 
print("huevos:", huevos)
print("cebolla:", cebolla_gramos, "gramos")