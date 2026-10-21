import re

class Campania:
    def __init__(self, fila):
        # 1. Asignamos los valores tal como vienen del archivo (como texto)
        # Si la columna no existe, ponemos un '0' de texto por defecto
        self.campaign_id = fila.get('campaign_id', '')
        self.campaign_type = fila.get('campaign_type', 'Desconocido')
        self.budget = fila.get('budget', '0')
        self.conversions = fila.get('conversions', '0')
        self.roi = fila.get('roi', '0')

    def es_valida(self):
        patron = r"^[a-zA-Z0-9\-]+$"   # solo permite letras, números y guiones
        if not re.fullmatch(patron, self.campaign_id):
            raise ValueError("El ID de campaña está vacío o tiene símbolos raros.")

        try:
            # Intentamos convertir los textos a números con decimales (float)
            presupuesto_num = float(self.budget)
            conversiones_num = float(self.conversions)
            roi_num = float(self.roi)
        except ValueError:
            # Si por ejemplo alguien escribió "mil" en vez de 1000, o dejó en blanco, salta este error
            raise ValueError("El presupuesto, conversiones o ROI no son números válidos.")

        if presupuesto_num <= 0:
            raise ValueError("El presupuesto debe ser mayor a cero.")
        
        if conversiones_num < 0:
            raise ValueError("Las conversiones no pueden ser negativas.")

        # si los datos están bien, guardamos los datos limpios
        self.budget = presupuesto_num
        self.conversions = conversiones_num
        self.roi = roi_num

        return True