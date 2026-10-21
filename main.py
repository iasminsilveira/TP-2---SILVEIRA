from fuentes import FuenteCSV, FuenteJSON
from analisis import separar_datos, calcular_rendimiento

def mostrar_menu():
    print("\n" + "-"*40)
    print("SISTEMA DE RENDIMIENTO DE CAMPAÑAS")
    print("-"*40)
    print("1. Cargar archivo de campañas (CSV o JSON)")
    print("2. Ver rendimiento por tipo de campaña")
    print("3. Ver reporte de campañas rechazadas (errores)")
    print("4. Salir")
    return input("\nElegí una opción (1-4): ")

def main():
    campanias_buenas = []
    campanias_malas = []
    
    # Bucle infinito para mantener el menú abierto hasta que el usuario elija Salir
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            
            print("\n!! IMPORTANTE: Tu archivo debe tener al menos estas columnas:")
            print(" - 'campaign_id' (texto con letras, números y guiones)")
            print(" - 'campaign_type' (texto, ej: 'Social Media')")
            print(" - 'budget' (número mayor a cero)")
            print(" - 'conversions' (número)")
            print(" - 'roi' (número decimal)")
            
            ruta = input("\nIngresá la ruta de tu archivo (ejemplo: data/campaigns.csv): ")
            
            # Elege qué clase usar dependiendo de la extensión del archivo
            if ruta.endswith('.csv'):
                fuente = FuenteCSV()
            elif ruta.endswith('.json'):
                fuente = FuenteJSON()
            else:
                print("\n !! Formato no soportado. El archivo debe terminar en .csv o .json")
                continue
            
            try:
                print("\nCargando datos...")
                datos_crudos = fuente.cargar(ruta)
                # Pasa los datos crudos por nuestro filtro
                campanias_buenas, campanias_malas = separar_datos(datos_crudos)
                
                print("¡Archivo procesado con éxito!")
                print(f"-> Campañas válidas listas para calcular: {len(campanias_buenas)}")
                print(f"-> Campañas con datos sucios separadas: {len(campanias_malas)}")
            except FileNotFoundError:
                print(f"\n Error: No se encontró ningún archivo en la ruta '{ruta}'")
            except Exception as e:
                print(f"\n Error inesperado al leer el archivo: {e}")
                
        
        
        elif opcion == '2':
            if len(campanias_buenas) == 0:
                print("\n Primero tenés que cargar un archivo válido (Opción 1).")
                continue
            
            resultados = calcular_rendimiento(campanias_buenas)
            print("\n" + "-"*40)
            print("TOP 3 MEDIOS DE PUBLICIDAD MÁS RENTABLES (MAYOR ROI)")
            print("-"*40)

            top_3 = resultados [:3]
            orden = ["1er Puesto", "2do Puesto", "3er Puesto"]

            for i, res in enumerate(top_3):
                orden = orden[i] if i < len(orden) else f"#{i+1}"
                print(f"{orden}: {res['tipo_campania']}")
                print(f"   ROI Promedio: {res['promedio_roi']}%")
                print(f"   Inversión Total: ${res['presupuesto_total']:,.2f}")
                print(f"   Conversiones: {int(res['conversiones_totales'])}")
                print("-" * 45)

            # Lista completa detallada
            print("\n" + "-"*45)
            print(" DETALLE GENERAL DE TODOS LOS TIPOS DE CAMPAÑA")
            print("-"*45)
            for res in resultados:
                print(f"Tipo: {res['tipo_campania']}")
                print(f"     Presupuesto Invertido: ${res['presupuesto_total']:,.2f}")
                print(f"     Conversiones Logradas: {res['conversiones_totales']}")
                print(f"     ROI Promedio: {res['promedio_roi']}%")
                print("-" * 40)
                
        elif opcion == '3':
            if len(campanias_malas) == 0:
                print("\n No hay campañas con errores o todavía no cargaste datos.")
                continue
            
            print("\n" + "-"*40)
            print("FILAS RECHAZADAS POR DATOS SUCIOS")
            print("-"*40)
            for mala in campanias_malas:
                print(f"ID: {mala['id_campania']}")
                print(f"Motivo: {mala['motivo_rechazo']}\n")
            print("Aclaración: Estas campañas se excluyeron para no arruinar el cálculo de rendimiento.")
            
        elif opcion == '4':
            print("\n¡Gracias por usar el sistema! Cerrando programa...\n")
            break
            
        else:
            print("\n!! Opción incorrecta. Por favor, ingresá un número del 1 al 4.")

# Esta línea asegura que el menú solo corra si ejecutamos este archivo directamente
if __name__ == "__main__":
    main()