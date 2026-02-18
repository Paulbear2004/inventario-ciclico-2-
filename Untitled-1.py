
inventario = {
    'FA080079.06': 40 ,
    'FA080076.06': 56 ,
    'FA080079.05': 48 ,
    'FA076028.09': 40 ,
    'FA080081.06': 40 ,
}
codigo = input("Ingrese el código que busca: ").strip()
reportado = inventario.get(codigo)
if reportado is not None:
    print(f"Reportados: {reportado}")
else:
    print(f"Código {codigo} no encontrado en el inventario.")
    reportado = 0
contados = []
print("Ingrese los códigos contados uno por línea. Deje vacío y presione Enter para finalizar.")
while True:
        try:
            linea = input("contados: ").strip()
        except EOFError:
            break
        if linea == "":
            break
        else:
          contados.append(linea)

print(f"Contados: {(contados)}")
print("\nResumen del conteo:")
print(f"Reportados: {reportado}")
print(f"Contados: {(contados)}")
print(f"Diferencia: {len(contados) - reportado}")
if (contados) == reportado:
        print("Todo está completo.")
elif len(contados) < reportado:
        print(f"Faltan {reportado - len(contados)} unidades.")
else:
        print(f"Sobra(n) {len(contados) - reportado} unidades.")
        print(f"⚠️ ALERTA: Contaste {len(contados)} unidades pero el sistema reporta {reportado}")
contados = []
print("Ingrese los códigos contados uno por línea. Deje vacío y presione Enter para finalizar.")
while True:
    try:
        linea = input("contados: ").strip()
    except EOFError:
        break
    if linea == "":
        break
    else:
        try:
            cantidad = int(linea)
            contados.append(cantidad)
        except ValueError:
            print(f"Error: '{linea}' no es un número válido. Intente de nuevo.")

print(f"Contados: {contados}")
print("\nResumen del conteo:")
print(f"Reportados: {reportado}")
print(f"Contados: {sum(contados)}")
print(f"Diferencia: {sum(contados) - reportado}")
if sum(contados) == reportado:
    print("Todo está completo.")
elif sum(contados) < reportado:
    print(f"Faltan {reportado - sum(contados)} unidades.")
else:
    print(f"Sobra(n) {sum(contados) - reportado} unidades.")

    print(f"Faltan {reportado - sum(contados)} unidades.")
    print(f"⚠️ ALERTA: Contaste {sum(contados)} unidades pero el sistema reporta {reportado}")
