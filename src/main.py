from fuentes import FuenteCSV, FuenteJSON
from analisis import separar_datos, calcular_rendimiento
from analisis import calcular_cpa_por_medio
from analisis import calcular_cpa_por_medio, calcular_eficiencia_score

def mostrar_menu():
    print("\n" + "-"*40)
    print("SISTEMA DE RENDIMIENTO DE CAMPAÑAS")
    print("-"*40)
    print("1. Cargar archivo de campañas (CSV o JSON)")
    print("2. Ver retorno de inversión (ROI) por tipo de campaña")
    print("3. Ver reporte de campañas rechazadas (errores)")
    print ("4. Ver medio más barato para adquirir clientes (Costo por adquisición)")
    print ("5. Ver recomendación final, ROI vs CPA")
    print("6. Salir")
    return input("\nElegí una opción (1-6): ")

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
            except KeyError:
                print("\nERROR: El archivo tiene columnas faltantes o mal escritas.")
                print("Verifica que existan todas las columnas obligatorias indicadas arriba.")
                print("Por favor", "soluciona esto y vuelve a intentar la Opción 1.\n")
                campanias_buenas = []
                campanias_malas = []
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
            puesto = ["1er Puesto", "2do Puesto", "3er Puesto"]

            for i, res in enumerate(top_3):
                puesto_actual = puesto[i] if i < len(puesto) else f"#{i+1}"
                print(f"{puesto_actual}: {res['tipo_campania']}")
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
           
            if len(campanias_buenas) == 0:
                print("\n Primero tenés que cargar un archivo válido (Opción 1).")
                continue

            ranking_cpa = calcular_cpa_por_medio(campanias_buenas)
            print("\n--- COSTO POR ADQUISICIÓN (CPA) ---")
            print("¿Cuánto cuesta conseguir 1 cliente en cada medio?")
            for i, item in enumerate(ranking_cpa, start=1):
                print(f"{i}º Puesto: {item['canal']} - CPA: ${item['cpa']:.2f}")

        elif opcion == '5':

            if len(campanias_buenas) == 0:
                print("\n Primero tenés que cargar un archivo válido (Opción 1).")
                continue
            
            ranking_final = calcular_eficiencia_score(campanias_buenas)
            print("\n--- RECOMENDACIÓN DEFINITIVA DE INVERSIÓN ---")
            print("Evaluando el cruce de mayor ROI y menor CPA...")
            
            for i, item in enumerate(ranking_final, start=1):
                destaque = " Conviene invertir en: " if i == 1 else "   "
                print(f"{i}º {destaque} {item['medio']}")
                print(f"   -> ROI Promedio: {item['roi']:.2f}% | CPA: ${item['cpa']:.2f} | Score: {item['puntaje']:.2f}\n")
        
        elif opcion == '6':
            print("\n¡Gracias por usar el sistema! Cerrando programa...\n")
            break
            
        else:
            print("\n!! Opción incorrecta. Por favor, ingresá un número del 1 al 6.")

# Esta línea asegura que el menú solo corra si ejecutamos este archivo directamente
if __name__ == "__main__":
    main()