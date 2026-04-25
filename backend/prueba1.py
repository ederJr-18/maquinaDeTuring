from datetime import datetime
from zoneinfo import ZoneInfo
 
def obtener_hora(ciudad_zona):
    try:
        ahora = datetime.now(ZoneInfo(ciudad_zona))
        return ahora.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return "Zona horaria no válida"
# Diccionario de ciudades
ciudades = {
    "Madrid": "Europe/Madrid",
    "Bogotá": "America/Bogota",
    "Nueva York": "America/New_York",
    "Tokio": "Asia/Tokyo"
}
# Mostrar horas predefinidas
print("--- Horarios actuales ---")
for nombre, zona in ciudades.items():
    print(f"{nombre}: {obtener_hora(zona)}")
print("-" * 25)
# Investigar una ciudad específica del diccionario
nombre_ciudad = input("Ingrese el nombre de la ciudad a investigar (ej. Madrid): ")
if nombre_ciudad in ciudades:
    zona = ciudades[nombre_ciudad]
    hora = obtener_hora(zona)
    print(f"Hora en {nombre_ciudad}: {hora}")
else:
    print("La ciudad no está en la base de datos.")
 