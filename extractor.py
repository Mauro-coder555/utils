import os

def procesar_elemento(ruta, primer_elemento=False):
    # Obtener el nombre del elemento (sin la ruta)
    nombre_elemento = os.path.basename(ruta)

    # Verificar si es una carpeta
    if os.path.isdir(ruta):
        # Si es una carpeta, procesar cada archivo dentro de ella
        for archivo in os.listdir(ruta):
            procesar_elemento(os.path.join(ruta, archivo), primer_elemento)
            primer_elemento = False  # Solo el primer elemento de todos debe evitar el espacio
    else:
        # Si es un archivo, agregar nombre y contenido a plain_code.txt
        with open('plain_code.txt', 'a') as salida:
            if not primer_elemento:
                salida.write(f"\n*** {nombre_elemento} ***\n\n")
            else:
                salida.write(f"*** {nombre_elemento} ***\n\n")
            with open(ruta, 'r') as archivo:
                salida.write(archivo.read() + '\n')

# Recorrer los argumentos pasados al script
if __name__ == "__main__":
    import sys
    primer_elemento = True
    for elemento in sys.argv[1:]:
        procesar_elemento(elemento, primer_elemento)
        primer_elemento = False  # Solo el primer elemento de todos debe evitar el espacio
