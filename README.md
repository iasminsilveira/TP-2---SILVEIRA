# TP-2-SILVEIRA
Programa de análisis de rendimiento de campañas de marketing


Problema y Alcance:
<<<<<<< HEAD
Las empresas suelen invertir en distintas herramientas de marketing sin saber cuál genera el mejor rendimiento y retorno de inversión (ROI)
Los posibles usuarios son equipos de marketing o dueños de empresas que buscan optimizar la asignación de presupuesto publicitario.
El siguiente proyecto es una aplicación en consola que procesa un historial de campañas que el ususario debe subir, normaliza los datos y realiza el análisis final.
Alcance: Esta versión procesa datos tabulares y genera un reporte agrupado por tipo de campaña.
=======
Las empresas suelen invertir su presupuesto publicitario en distintas herramientas de marketing sin saber cuál genera el mayor rendimiento real en sus ventas finales y un mejor retorno de inversión (ROI).

Los posibles usuarios son equipos de marketing o dueños de empresas que tengan publicidad propia y buscan ayudarse a tomar decisiones sobre cómo distribuir su presupuesto.
>>>>>>> 8437367 (Arregla error de bucle for para el TOP 3 en main.py)

Los datos que el programa utilizará deben tener ciertas columnas específicas:

Cada fila debe representar una campaña de marketing especìfica ejecutada en un período de tiempo.

Variables principales: Tipo de campaña (campaign_type), Presupuesto (budget), Retorno de Inversión (roi) y Conversiones (conversiones)

INSTALACIÓN Y USO:
<<<<<<< HEAD
Requiere Python 3
=======
* Python 3
* No requiere instalación de bibliotecas externas (utiliza únicamente la biblioteca estándar de Python: `csv`, `json`, `re`, `unittest`).


Ejecución de las pruebas:

El programa incluye pruebas unitarias para validar las entradas, los datos nulos y las propiedades de las funciones. Para correrlas:

python -m unittest discover tests

Organización del código:
* `main.py`: Punto de entrada que despliega el menú interactivo para el usuario.
* `fuentes.py`: Clases para la lectura segura de archivos mediante la clase base FuenteDatos y sus derivadas para CSV y JSON.
* `dominio.py`: Contiene la clase Campania y protege las reglas de negocio verificando la validez de los datos
* `analisis.py`: Lógica del paradigma funcional para procesar la lista, separar los datos sucios (sin perderlos) y calcular métricas agrupadas.
* `data`: Contiene el dataset de muestra (`campaigns.csv`).
* `tests`: Casos de prueba (`test_programa.py`) ejecuables para asegurar la calidad del código.

>>>>>>> 8437367 (Arregla error de bucle for para el TOP 3 en main.py)

Ejecución de la aplicación:
`python main.py`

<<<<<<< HEAD
Ejecución de las pruebas:
`python -m unittest discover tests/

Organización del código:
`main.py`: Punto de entrada y menú de la aplicación.
`fuentes.py`: Clases para la lectura y normalización de archivos CSV y JSON.
`pipeline.py`: Lógica de validación, filtrado y cálculo de ROI.
`data/`: Directorio con los datos de entrada (`campaigns.csv`) y salidas generadas.
`tests/`: Casos de prueba automatizados.
=======
Clonar el repositorio en la computadora del usuario.

Asegurarse que el archivo de los datos de su campaña esté dentro de la carpeta "data"

Ejecutar el siguiente comando desde la terminal:

```bash
python main.py
>>>>>>> 8437367 (Arregla error de bucle for para el TOP 3 en main.py)
