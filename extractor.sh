#!/bin/bash

# Función para procesar un elemento (archivo o carpeta)
procesarElemento() {
  # Obtener el nombre del elemento (sin la ruta)
  nombreElemento=$(basename "$1")

  # Verificar si es una carpeta
  if [ -d "$1" ]; then
    # Si es una carpeta, procesar cada archivo dentro de ella
    for archivo in "$1"/*; do
      procesarElemento "$archivo"
    done
  else
    # Si es un archivo, agregar nombre y contenido a plain_code.txt
    if [ "$primerElemento" = true ]; then
      echo "== $nombreElemento ==" >> plain_code.txt
      primerElemento=false
    else
      echo -e "\n== $nombreElemento ==\n" >> plain_code.txt
    fi
    cat "$1" >> plain_code.txt
    echo "" >> plain_code.txt
  fi
}

# Inicializar el indicador de primer elemento
primerElemento=true

# Recorrer los argumentos pasados al script
for elemento in "$@"; do
  procesarElemento "$elemento"
done
