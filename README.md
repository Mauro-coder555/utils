# File Content Consolidation Scripts

Estos scripts en Bash y Python te permiten consolidar el contenido de múltiples archivos y carpetas en un solo archivo de texto (`plain_code.txt`). Esto es útil para pasar el contenido a una IA de procesamiento de texto sin tener que abrir y copiar cada archivo manualmente.

## Características

- Procesa recursivamente archivos y carpetas.
- Compatible con cualquier tipo de archivo (JSON, HTML, TXT, etc.).
- Agrega el nombre del archivo y su contenido al archivo de salida (`plain_code.txt`).
- Evita agregar un espacio en blanco antes del primer archivo.

## Uso 🚀

### Clonar el Repositorio

```bash
git clone https://github.com/Mauro-coder555/utils.git
cd utils
```

### Versión Bash:

Dar permisos de ejecución

```bash
chmod +x extractor.sh
```

Ejecutar script con los nombres de archivos y/o carpetas de las cuales queramos extraer el contenido
```bash
./extractor.sh ruta/carpeta1 ruta/archivo1.txt ruta/carpeta2
```

### Versión Python:

Ejecutar script con los nombres de archivos y/o carpetas de las cuales queramos extraer el contenido

```bash
python extractor.py ruta/carpeta1 ruta/archivo1.txt ruta/carpeta2
```

#### Estos scripts consolidan el contenido de archivos y carpetas, independientemente del tipo de archivo (JSON, HTML, TXT, etc.), en un solo archivo plain_code.txt, listo para ser procesado por IA. Puedes pasar tantos archivos y carpetas como desees como argumentos. ¡Espero que les sea útil!
