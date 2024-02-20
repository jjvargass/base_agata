from appy.pod.renderer import Renderer # pip3 install appy
from odoo.exceptions import ValidationError
from time import sleep
import os
import psutil
import subprocess
import base64


def create_office_reports(self, dict_data, name_doc_download, format_output, name_template, path_template):
    """
    dict_data               - Toda la información que se implementará en el reporte. este es un diccionario.
    name_doc_download       - Nombre al documento resultado, seal el nombre del documento cuano se descargue.
    format_output           - Extención o Formato de salida para el reporte. EJ: pdf,xls,doc
    name_template           - Nombre del documento fuente o plantilla ODT o ODS. alojada en /TuModulo/reports
    path_template           - Ruta absoluta donde se aloja el template ODT o ODS.  
    """

    # Ruta Plantilla
    separador = os.path.sep  # obtiene segun el sistema operativo
    ruta_plantilla = path_template + separador + name_template

    if not os.path.exists(ruta_plantilla):
        raise ValidationError("Debe establecer plantilla de reporteS [" + name_template + "] para este módulo")

    # Obtener extencion de la plantilla
    extencion_plantilla = name_template.split(".")[-1]

    # Nombre para archivos salida
    inicial_nombre = "Reporte_"
    nombre_archivo_resultado = inicial_nombre + name_doc_download + '_' + str(self.id) + '.' + extencion_plantilla
    nombre_archivo_resultado_transformado = inicial_nombre + name_doc_download + '_' + str(self.id) + '.' + format_output

    # Carpeta Contenedora de Reportes
    carpeta = '/tmp/reportres/'
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    archivo_resultado = carpeta + nombre_archivo_resultado
    archivo_resultado_transformado = carpeta + nombre_archivo_resultado_transformado

    # Crear reporte basado en la plantilla ODT o ODS y los datos.
    try:
        renderer = Renderer(ruta_plantilla, dict_data, archivo_resultado)
        renderer.run()
    except IOError as e:
        raise ValidationError("I/O Error: {0}".format(e))
    except:
        raise ValidationError("I/O Error: {0}".format(e))

    # Convertir Reporte a Formato Salida
    #kill_process_libreoffice()
    subprocess.run(
        "soffice --headless --invisible --convert-to {} {} --outdir {} ".format(format_output, archivo_resultado, carpeta),
        shell=True,
        check=True,
        env={"HOME": carpeta},
    )

    # Ya esta creado documento en formato salida?
    while not os.path.isfile(archivo_resultado_transformado):
        sleep(1)

    # Codificar archivo
    with open(archivo_resultado_transformado, "rb") as reporte:
        encoded_report = base64.b64encode(reporte.read())
    
    # Elimina archivos creados en sisco y retorna archivo codificado 
    if(encoded_report):
        os.remove(archivo_resultado)
        os.remove(archivo_resultado_transformado)

    return encoded_report, nombre_archivo_resultado_transformado

def kill_process_libreoffice():
    PROCNAME = "soffice.bin"
    for proc in psutil.process_iter():
        if proc.name == PROCNAME:
            proc.kill()