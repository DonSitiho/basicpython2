# Guardo la secuencia completa de la preproinsulina en una variable.
# Uso \ para dividir la línea porque es muy larga.
preproInsulin = (
"malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
)
# Ahora guardo las partes de la insulina en variables separadas.
# Esto es para trabajar mejor con cada parte.
lsInsulin = "malwmrllpllallalwgpdpaaa" 
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt" 
aInsulin = "giveqcctsicslyqlenycn" 
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Aquí junto la cadena B y la cadena A.
# El símbolo + sirve para pegar textos.
insulin = bInsulin + aInsulin

# Ahora voy a imprimir cosas en pantalla.

# Imprimo un mensaje primero.
print("La secuencia de la preproinsulina humana es:")

# Aquí imprimo lo que guardé en la variable.
print(preproInsulin)

# Aquí imprimo texto y le agrego la cadena A.
print("La secuencia de la insulina humana, cadena A: " + aInsulin)

