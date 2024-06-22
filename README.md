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
---

### Versión Python (GUI):

#### Instalar la librería PyQt5

```python
pip install PyQt5
```

Ejecutar script y seleccionar en la ventana gráfica la opción "Seleccionar Archivo" si queremos extraer el contenido de un archivo
o "Seleccionar carpeta" si queremos extraer el contenido de todos los archivos de una carpeta.


```bash
python extractor_gui.py ruta/carpeta1 ruta/archivo1.txt ruta/carpeta2
```

Se podrán seleccionar archivos y carpetas en la cantidad deseada y en cualquier orden. Para facilitar esto, los mismos seran listados en la ventana
con el fin de ver todo lo que vamos seleccionando.
Finalmente damos click en "Procesar selección" y se mostrara un cartel indicando el estado de éxito de la operacion.

---

### Versión Python (Linea de comandos):

Ejecutar script con los nombres de archivos y/o carpetas de las cuales queramos extraer el contenido

```bash
python extractor.py ruta/carpeta1 ruta/archivo1.txt ruta/carpeta2
```

---

### Versión Bash (Linea de comandos):

Dar permisos de ejecución

```bash
chmod +x extractor.sh
```

Ejecutar script con los nombres de archivos y/o carpetas de las cuales queramos extraer el contenido
```bash
./extractor.sh ruta/carpeta1 ruta/archivo1.txt ruta/carpeta2
```

---


#### Estos scripts consolidan el contenido de archivos y carpetas, independientemente del tipo de archivo (JSON, HTML, TXT, etc.), en un solo archivo plain_code.txt con el titulo y una separaciòn clara para cada archivo en cuestión, listo para ser procesado por IA. Puedes pasar tantos archivos y carpetas como desees como argumentos. ¡Espero que les sea útil!
