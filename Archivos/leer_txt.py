# usando open para abrir un archivo, con una codificacion universal UTF-8
archivo = open("Archivos\\Notaslol.txt",encoding="UTF-8")

# leer completo
archivo = archivo.read()

# leer linea por linea
# lineas = archivo.readlines()

# leer una sola linea
# linea = archivo.readline()

# cerrar el archivo
archivo.close()

print(archivo)
