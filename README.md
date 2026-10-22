# TP-2-SILVEIRA
Programa de análisis de rendimiento de campañas de marketing


Problema y Alcance:
Las empresas suelen invertir en distintas herramientas de marketing sin saber cuál genera el mejor rendimiento y retorno de inversión (ROI).
Los posibles usuarios son equipos de marketing o dueños de empresas que posean publicidad propia y que buscan optimizar la asignación de presupuesto publicitario.
El siguiente proyecto es una aplicación en consola que procesa un historial de campañas que el ususario debe subir, normaliza los datos y realiza el análisis final.
**Alcance**: Esta versión procesa datos tabulares y genera un reporte agrupado por tipo de campaña.

El programa evalúa el Retorno de Inversión (ROI) general y el Costo por Adquisición (CPA) de cada medio. El ROI es la métrica que mide la rentabilidad financiera de una campaña en terminos porcentuales. El CPA indica cuánto dinero cuesta conseguir un cliente real (conversión) en cada medio.

Luego el menú presenta una opción que sirve para ver la eficiencia definitiva, cruzando el ROI y CPA juntos (ROI dividido CPA). Porque analizarlos de forma aislada puede llevar a malas interpretaciones, un medio podría tener un ROI excelente, pero un CPA tan alto que termine rápidamente con todo el presupuesto disponible. Genera un ranking definitivo para la empresa.

Las siguientes condiciones se deben cumplir obligatoriamente en el CSV o Json que suba el usuario:

Cada fila debe representar una campaña de marketing ejecutada en un período de tiempo.

Las siguientes columnas con sus nombres exactos (en inglés y minúsculas) para que el sistema pueda procesarlas correctamente:

* **`campaign_id`**: Identificador único de la campaña (formato de texto o código alfanumérico).
* **`campaign_type`**: El medio o canal publicitario utilizado en la campaña (ej. Email, Social Media, Online Display Ads). Se utiliza para agrupar y comparar el rendimiento.
* **`budget`**: El presupuesto total de dinero invertido en esa campaña (valor numérico).
* **`conversions`**: La cantidad de clientes o conversiones reales logradas (valor numérico entero).
* **`roi`**: El porcentaje de Retorno de Inversión (valor numérico, acepta decimales y números negativos en caso de pérdidas).

*(Si alguna fila del archivo no contiene exactamente estas columnas, tiene valores vacíos o tipos de datos inválidos (como letras en la columna de presupuesto), el programa filtrará esa campaña automáticamente y la enviará al reporte de campañas rechazadas).*


## INSTALACIÓN Y USO:

* Requiere **Python 3**
* No requiere instalación de bibliotecas externas (utiliza únicamente la biblioteca estándar de Python: `csv`, `json`, `re`, `unittest`).


**Ejecución de las pruebas:**

El programa incluye pruebas unitarias para validar las entradas, los datos nulos y las propiedades de las funciones. Para correrlas:

python -m unittest discover tests

Organización del código:
* `main.py`: Punto de entrada que despliega el menú interactivo para el usuario.
* `fuentes.py`: Clases para la lectura segura de archivos mediante la clase base FuenteDatos y sus derivadas para CSV y JSON.
* `dominio.py`: Contiene la clase Campania y protege las reglas de negocio verificando la validez de los datos
* `analisis.py`: Lógica del paradigma funcional para procesar la lista, separar los datos sucios (sin perderlos) y calcular métricas agrupadas y de costos (ROI y CPA).
* `data`: Contiene el dataset de muestra (`campaigns.csv`).
* `tests`: Casos de prueba (`test_programa.py`) ejecuables para asegurar la calidad del código.


**Ejecución de las pruebas:**

python -m unittest discover tests/


**Ejecución de la aplicación:**

1. 2.Clonar el repositorio en la computadora del usuario.

2. Asegurarse que el archivo de los datos de su campaña esté dentro de la carpeta "data"

3. Ejecutar el siguiente comando desde la terminal:

```bash
python main.py
