#pedir el numero al usuario 
numero = int(input("ingresa un numero de dos digitos:"))
# calculamos el digito de las unidades (residuo de dividir entre 10) y digito de las decenas (division entre 10)
unidades = numero % 10 
decenas = numero // 10
#mostramos los resultados 
print("el digito de las decenas es:", decenas)
print("el digito de las unidades es:", unidades)
