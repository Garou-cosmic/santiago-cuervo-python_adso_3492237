# Actividad: Factura de consulta veterinaria

# Entrada de datos
nombre_dueño = input("Nombre del dueño de la mascota: ")
nombre_mascota = input("Nombre de la mascota: ")

print("\nTipos de consulta disponibles:")
print("1. Consulta general")
print("2. Vacunación")
print("3. Cirugía")
print("4. Peluquería")

opcion = int(input("Elige el tipo de consulta (1-4): "))

# Proceso: calcular el valor según el tipo de consulta
if opcion == 1:
    tipo_consulta = "Consulta general"
    valor = 30000
elif opcion == 2:
    tipo_consulta = "Vacunación"
    valor = 25000
elif opcion == 3:
    tipo_consulta = "Cirugía"
    valor = 150000
elif opcion == 4:
    tipo_consulta = "Peluquería"
    valor = 20000
else:
    tipo_consulta = "Opción no válida"
    valor = 0

# Salida: mostrar la factura
print("\n===== FACTURA CLÍNICA VETERINARIA =====")
print("Dueño:", nombre_dueño)
print("Mascota:", nombre_mascota)
print("Tipo de consulta:", tipo_consulta)
print("Valor a pagar:", valor)
print("========================================")