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

    return resultados