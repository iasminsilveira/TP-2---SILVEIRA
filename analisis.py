from dominio import Campania

def separar_datos(datos_crudos):
    """

    Recorre todas las filas del archivo.
    Separa las campañas válidas de las que tienen errores sin borrar ningún dato.

    """
    campanias_buenas = []
    campanias_malas = []

    for fila in datos_crudos:
        # Crea el objeto campaña con la fila actual
        campania = Campania(fila)
        
        try:
            # Intenta validarla con el filtro hecho en dominio.py
            campania.es_valida()
            # Si no saltan errores, se guarda en la lista buena
            campanias_buenas.append(campania)
            
        except ValueError as error:
            # Si el filtro encuentra un dato sucio, atrapa el error
            # y guarda la fila en la lista mala junto con el motivo
            campanias_malas.append({
                "id_campania": campania.campaign_id,
                "motivo_rechazo": str(error)
            })
            
    return campanias_buenas, campanias_malas


def calcular_rendimiento(campanias_buenas):
    """
    Agrupa las campañas por tipo y calcula cuál tuvo mejor ROI promedio.
    Devuelve la lista ordenada de mayor a menor ROI.
    
    """
    rendimiento_por_tipo = {}

    # Agrupa los datos usando un for
    for campania in campanias_buenas:
        tipo = campania.campaign_type
        
        # Si el tipo de campaña todavía no está en nuestro diccionario, lo creamos
        if tipo not in rendimiento_por_tipo:
            rendimiento_por_tipo[tipo] = {
                "presupuesto_total": 0,
                "conversiones_totales": 0,
                "cantidad_campanias": 0,
                "roi_sumado": 0
            }
        
        # Le suma los valores de la campaña actual
        rendimiento_por_tipo[tipo]["presupuesto_total"] += campania.budget
        rendimiento_por_tipo[tipo]["conversiones_totales"] += campania.conversions
        rendimiento_por_tipo[tipo]["cantidad_campanias"] += 1
        rendimiento_por_tipo[tipo]["roi_sumado"] += campania.roi

    # Calcula el promedio final para saber cuál rinde más
    resultados = []
    for tipo, datos in rendimiento_por_tipo.items():
        promedio_roi = datos["roi_sumado"] / datos["cantidad_campanias"]
        
        resultados.append({
            "tipo_campania": tipo,
            "presupuesto_total": datos["presupuesto_total"],
            "conversiones_totales": datos["conversiones_totales"],
            "promedio_roi": round(promedio_roi, 2) # Redondea a 2 decimales
        })

    # Ordena de mayor a menor el ROI promedio
    resultados.sort(key=lambda x: x["promedio_roi"], reverse=True)
    
    return resultados

def calcular_cpa_por_medio(campanias):
    datos_por_medio = {}
    # Agrupa y suma presupuesto y conversiones
    for campania in campanias:
        medio = campania.campaign_type
        if not medio or medio.strip() == "":
            medio = "Sin Especificar"
        if medio not in datos_por_medio:
            datos_por_medio[medio] = {'presupuesto': 0, 'conversiones': 0}

        datos_por_medio[medio]['presupuesto'] += float(campania.budget)
        datos_por_medio[medio]['conversiones'] += int(campania.conversions)
    
    cpa_por_medio = []

    # Calcula el Costo por Adquisición  real
    for medio, datos in datos_por_medio.items():
        if datos['conversiones'] > 0:
            cpa = datos['presupuesto'] / datos['conversiones']
        else:
            cpa = 0
        cpa_por_medio.append({'canal': medio, 'cpa': cpa})

    # Paso 3: Ordenar de menor a mayor (el CPA más bajo es el mejor)
    cpa_por_medio.sort(key=lambda x: x['cpa'])
    
    return cpa_por_medio 

def calcular_eficiencia_score(campanias):
    datos_por_medio = {}
    
    # 1. Agrupa la información
    for campania in campanias:
        medio = campania.campaign_type
        if medio not in datos_por_medio:
            datos_por_medio[medio] = {'presupuesto': 0, 'conversiones': 0, 'roi_total': 0, 'cantidad': 0}
            
        datos_por_medio[medio]['presupuesto'] += float(campania.budget)
        datos_por_medio[medio]['conversiones'] += int(campania.conversions)
        datos_por_medio[medio]['roi_total'] += float(campania.roi)
        datos_por_medio[medio]['cantidad'] += 1
        
    ranking = []
    
    # 2. Calcula ROI, CPA y Puntaje de Eficiencia
    for medio, datos in datos_por_medio.items():
        cpa = datos['presupuesto'] / datos['conversiones'] if datos['conversiones'] > 0 else 0
        roi_promedio = datos['roi_total'] / datos['cantidad'] if datos['cantidad'] > 0 else 0
        
        # Si da pérdida o no trae clientes, el puntaje es 0. Si no, calcula la eficiencia.
        if cpa > 0 and roi_promedio > 0:
            puntaje = roi_promedio / cpa
        else:
            puntaje = 0
            
        ranking.append({
            'medio': medio,
            'roi': roi_promedio,
            'cpa': cpa,
            'puntaje': puntaje
        })
        
    # 3. Ordena de mayor a menor puntaje (el mejor arriba)
    ranking.sort(key=lambda x: x['puntaje'], reverse=True)
    
    return ranking