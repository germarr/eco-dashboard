import psycopg2
import psycopg2.extras
import csv
import pandas as pd
from datetime import datetime, timedelta
import json

# dconnector="host=postgresql_db port=5432 dbname=apidata user=gmarr password=password"
dconnector="host=173.255.226.165 port=5432 dbname=apidata user=gmarr password=password"
nameOfTheFile = "viajes_por_mes"

def get_cards(cardsdate):
    q1=f"""
        SELECT hora, sum(num_de_viajes) as viajes FROM public.viajes_por_mes
        where {cardsdate}
        group by hora
        order by hora 
        """
    conn = psycopg2.connect(dconnector)
    cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
    cur.execute(q1)
    fulldf = cur.fetchall()

    datos = {
        "lista_hora":[r["hora"] for r in fulldf],
        "lista_viajes": [r["viajes"] for r in fulldf]
    }

    return datos