with open('Archivos\\textolol.txt',"a",encoding="UTF-8") as archivo:
    # agregando el archivo
    archivo.write("\n")
    # usando un bucle para agergar varias lineas
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")
