import boto3
from datetime import datetime, timedelta

def is_weekend():
    # Obtiene el día de la semana (0 = lunes, 1 = martes, ..., 6 = domingo)
    current_day_of_week = datetime.utcnow().weekday()

    # Devuelve True si es sábado o domingo, False si es un día de la semana
    return current_day_of_week in [5, 6]

print(f"Es fin de semana?: {is_weekend()}")