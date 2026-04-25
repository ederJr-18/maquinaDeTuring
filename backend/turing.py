from datetime import datetime
import pytz # Asegúrate de que pytz esté instalado (pip install pytz)


proceso_mt_geotemporal = [
  {
    "paso": 1,
    "estado": "q_inicio",
    "lee": "Bogotá-Madrid",
    "escribe": "16:00",
    "accion": "Mover R",
    "descripcion": "Calcula la hora local en el destino"
  },
  {
    "paso": 2,
    "estado": "q_verificar_periodo",
    "lee": "16:00",
    "escribe": "PM",
    "accion": "Mover R",
    "descripcion": "Determina si es AM o PM según la hora escrita"
  },
  {
    "paso": 3,
    "estado": "q_calculo_offset",
    "lee": "Zona_05/Zona_02",
    "escribe": "+7 Horas",
    "accion": "Mover R",
    "descripcion": "Calcula la diferencia entre meridianos"
  },
  {
    "paso": 4,
    "estado": "q_finalizar",
    "lee": "Completo",
    "escribe": "REPORT_READY",
    "accion": "HALT",
    "descripcion": "Finaliza la ejecución y genera salida"
  }
]
def datosdeBogota(proceso_mt_geotemporal):
  if proceso_mt_geotemporal < 12:
    estadoDelDia = "Mañana"
  elif proceso_mt_geotemporal >= 12 and proceso_mt_geotemporal < 18:
    estadoDelDia = "Tarde"
  else:
    estadoDelDia = "Noche"


  return {
    "pais": "colombia",
    "hora": proceso_mt_geotemporal,
    "estado del dia": estadoDelDia,
    "horas de diferencias": 0
  }

def datosdeMadrid(proceso_mt_geotemporal):
  # Si la hora era 20, 20 + 6 = 26. 
  # 26 % 24 = 2 (Es decir, las 2 de la madrugada).
  hora_madrid = (int(proceso_mt_geotemporal) + 6) % 24  
  
  if hora_madrid < 12:
    estadoDelDia = "Mañana"
  elif hora_madrid >= 12 and hora_madrid < 18:
    estadoDelDia = "Tarde"
  else:
    estadoDelDia = "Noche"
    
  return {
    "pais": "españa",
    "hora": f"{hora_madrid}:00",
    "offset": "+6 Horas",
    "estado del dia": estadoDelDia
  }


def datosdeTokyo(proceso_mt_geotemporal):
  hora_tokyo = (int(proceso_mt_geotemporal) + 14) % 24  
  
  if hora_tokyo < 12:
    estadoDelDia = "Mañana"
  elif hora_tokyo >= 12 and hora_tokyo < 18:
    estadoDelDia = "Tarde"
  else:
    estadoDelDia = "Noche"
  return {
    "pais": "japon",
    "hora": f"{hora_tokyo}:00",
    "offset": "+14 Horas",
    "estado del dia": estadoDelDia
  }

def datosdeLondres(proceso_mt_geotemporal):
  hora_londres = (int(proceso_mt_geotemporal) + 5) % 24  
  
  if hora_londres < 12:
    estadoDelDia = "Mañana"
  elif hora_londres >= 12 and hora_londres < 18:
    estadoDelDia = "Tarde"
  else:
    estadoDelDia = "Noche"
  return {
    "pais": "inglaterra",
    "hora": f"{hora_londres}:00",
    "offset": "+6 Horas",
    "estado del dia": estadoDelDia
  }

def datosdeSidny(proceso_mt_geotemporal):
  hora_sidny = (int(proceso_mt_geotemporal) + 15) % 24  
  
  if hora_sidny < 12:
    estadoDelDia = "Mañana"
  elif hora_sidny >= 12 and hora_sidny < 18:
    estadoDelDia = "Tarde"
  else:
    estadoDelDia = "Noche"
  return {
    "pais": "australia",
    "hora": f"{hora_sidny}:00",
    "offset": "+15 Horas",
    "estado del dia": estadoDelDia
  }

def ciudadDefinida(ciudadEntrada):
    if ciudadEntrada == "bogota":
        return "colombia"
    elif ciudadEntrada == "madrid":
        return "españa"
    elif ciudadEntrada == "tokyo":
        return "japon"
    elif ciudadEntrada == "londres":
        return "inglaterra"
    elif ciudadEntrada == "sidny":
        return "australia"
    else:
        return "Ciudad no encontrada"

def horaMadrid():
    hora_madrid = datetime.now(pytz.timezone('Europe/Madrid'))
    return hora_madrid.strftime("%H:%M")
 # Madrid
 #cabezal [0] => d
 # lecturaDeCiudadEntrada = Mad
def turing(ciudadEntrada, proceso_mt_geotemporal):
    # Convertimos la lista proceso_mt_geotemporal a string para poder sumarla al string de ciudadEntrada
    cinta = list(ciudadEntrada + str(proceso_mt_geotemporal)) + ['*'] * 12 
    numeroDeLetrasCiudadEntrada = len(ciudadEntrada) 
    cabezal = 0 
    estado = "q0"
    lecturaDeCiudadEntrada = "" # Corregido: lectroDeCabezal no estaba definido 

    while cabezal < numeroDeLetrasCiudadEntrada:
        lecturaDeCiudadEntrada += cinta[cabezal] # Agrega letra por letra de la cinta
        cabezal += 1
        if cabezal < len(cinta) and cinta[cabezal] == "-": # Evitar error fuera de indice
           estado='q1'
        elif estado =='q1':
          return ciudadDefinida(lecturaDeCiudadEntrada)
        else:
          return "Ciudad no encontrada"

            
    
    # Retorno simulado de respuesta

# Hora de la ciudad
# Estado del dia 
# Horas de diferencias

if __name__ == "__main__":
    ciudadEntrada = input("Ingrese la ciudad que desea consultar: ")
    proceso_mt_geotemporal= datetime.now().strftime("%H:%M:%S")
    print(turing(ciudadEntrada,proceso_mt_geotemporal))

