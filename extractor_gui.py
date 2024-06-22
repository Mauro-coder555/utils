import os
from PyQt5.QtWidgets import QApplication, QFileDialog, QVBoxLayout, QPushButton, QListWidget, QWidget, QLabel, QHBoxLayout, QMessageBox

def procesar_elemento(ruta, primer_elemento=False):
    nombre_elemento = os.path.basename(ruta)

    if os.path.isdir(ruta):
        for archivo in os.listdir(ruta):
            procesar_elemento(os.path.join(ruta, archivo), primer_elemento)
            primer_elemento = False
    else:
        with open('plain_code.txt', 'a') as salida:
            if not primer_elemento:
                salida.write(f"\n*** {nombre_elemento} ***\n\n")
            else:
                salida.write(f"*** {nombre_elemento} ***\n\n")

            # Intentar leer el archivo en varias codificaciones
            content = None
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    with open(ruta, 'r', encoding=encoding) as archivo:
                        content = archivo.read()
                        break
                except UnicodeDecodeError:
                    continue

            if content is None:
                print(f"Error: No se pudo leer el archivo {ruta} en las codificaciones disponibles.")
            else:
                salida.write(content + '\n')

def seleccionar_archivos():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.ExistingFiles)
    dialog.setOption(QFileDialog.DontUseNativeDialog, True)
    dialog.setNameFilter("Archivos de texto (*.txt);;Todos los archivos (*)")
    dialog.setViewMode(QFileDialog.Detail)

    if dialog.exec_():
        rutas = dialog.selectedFiles()
        return rutas
    return []

def seleccionar_carpetas():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    dialog.setOption(QFileDialog.DontUseNativeDialog, True)
    dialog.setViewMode(QFileDialog.Detail)

    if dialog.exec_():
        rutas = dialog.selectedFiles()
        return rutas
    return []

class FileSelectorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Selector de Archivos y Carpetas')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.label = QLabel('Seleccione archivos y carpetas:')
        layout.addWidget(self.label)

        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        button_layout = QHBoxLayout()

        self.select_files_button = QPushButton('Seleccionar archivos', self)
        self.select_files_button.clicked.connect(self.show_file_dialog)
        button_layout.addWidget(self.select_files_button)

        self.select_folders_button = QPushButton('Seleccionar carpetas', self)
        self.select_folders_button.clicked.connect(self.show_folder_dialog)
        button_layout.addWidget(self.select_folders_button)

        self.process_button = QPushButton('Procesar Selección', self)
        self.process_button.clicked.connect(self.process_selection)
        button_layout.addWidget(self.process_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def show_file_dialog(self):
        rutas = seleccionar_archivos()
        for ruta in rutas:
            self.file_list.addItem(ruta)

    def show_folder_dialog(self):
        rutas = seleccionar_carpetas()
        for ruta in rutas:
            self.file_list.addItem(ruta)

    def process_selection(self):
        primer_elemento = True
        error_occurred = False  # Variable para rastrear errores

        for i in range(self.file_list.count()):
            elemento = self.file_list.item(i).text()
            try:
                procesar_elemento(elemento, primer_elemento)
                primer_elemento = False
            except Exception as e:
                print(f"Error al procesar {elemento}: {e}")
                error_occurred = True

        # Mostrar mensaje antes de cerrar
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)

        if error_occurred:
            msg_box.setText("Hubo algunos errores al procesar los archivos.")
            msg_box.setWindowTitle("Error")
        else:
            msg_box.setText("Todos los archivos se procesaron correctamente.")
            msg_box.setWindowTitle("Éxito")

        msg_box.exec_()
        self.close()  # Cerrar la aplicación después de mostrar el mensaje


if __name__ == "__main__":
    app = QApplication([])
    selector_app = FileSelectorApp()
    selector_app.show()
    app.exec_()
