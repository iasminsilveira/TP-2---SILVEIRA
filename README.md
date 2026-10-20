# TP-2---SILVEIRA
Programa de análisis de rendimiento de campañas de marketing

Problema y Alcance:
Las empresas suelen invertir en distintas herramientas de marketing sin saber cuál genera el mejor rendimiento y retorno de inversión (ROI)
Los posibles usuarios son equipos de marketing o dueños de empresas que buscan optimizar la asignación de presupuesto publicitario.
El siguiente proyecto es una aplicación en consola que procesa un historial de campañas que el ususario debe subir, normaliza los datos y realiza el análisis final.
Alcance: Esta versión procesa datos tabulares y genera un reporte agrupado por tipo de campaña.

Los datos que el programa utilizará deben tener ciertas columnas específicas:

Cada fila debe representar una campaña de marketing especìfica ejecutada en un período de tiempo.

Variables principales: Tipo de campaña (campaign_type), Presupuesto (budget), Retorno de Inversión (roi) y Conversiones (conversiones)

INSTALACIÓN Y USO:
Requiere Python 3

Ejecución de la aplicación:
`python main.py`

Ejecución de las pruebas:
`python -m unittest discover tests/

Organización del código:
`main.py`: Punto de entrada y menú de la aplicación.
`fuentes.py`: Clases para la lectura y normalización de archivos CSV y JSON.
`pipeline.py`: Lógica de validación, filtrado y cálculo de ROI.
`data/`: Directorio con los datos de entrada (`campaigns.csv`) y salidas generadas.
`tests/`: Casos de prueba automatizados.
