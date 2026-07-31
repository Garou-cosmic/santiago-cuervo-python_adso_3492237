# pedir el precio del producto 
precio = float(input("ingresa el precio del producto:"))
# pedir el porcentaje del IVA
iva = float(input("ingresa el porcetaje del iva (ejemplo: 19, sin el simbolo &): "))
# calcular el valor del IVA 
valor_iva = precio * iva /100
# calcular el precio total 
total = precio + valor_iva 
# mostrar el resultado
print("el precio total a pagar es:", total)