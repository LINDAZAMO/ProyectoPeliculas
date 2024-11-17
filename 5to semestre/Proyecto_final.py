"""Archivo con las funciones para realizar el proceso Web Scraping."""

"""Importacion de librerías."""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

"""Diccionario para almacenar los datos en un dataframe."""
datos = {
    "pelicula": [],
    "fecha_estreno": [],
    "tipo_estreno": [],
    "duracion": [],
    "genero": [],
    "director": [],
    "calf_medios": [],
    "calf_usuarios": [],
    "calf_rotten_tomatoes": [],
    "nacionalidad": [],
    "distribuidora": [],
    "fecha_produccion": [],
    "presupuesto": [],
    "idioma": []
}

""""Se define la función para conectar con el navegador y página web"""
def conexion():
    driver = ChromeDriverManager().install()
    s = Service(driver)
    opc = Options()
    opc.add_argument("--start-maximized")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.rottentomatoes.com")  # Abre la página web especificada

    return navegador

# Función para buscar películas
def buscar_peliculas(navegador, pelicula):
    search_box = navegador.find_element(By.NAME, "search")
    search_box.send_keys(pelicula)
    search_box.submit()
    time.sleep(2)  # Esperar a que se cargue la página

# Función para extraer información de la película
def extraccion_informacion(soup: BeautifulSoup):
    temp_datos = {
        "pelicula": [],
        "fecha_estreno": [],
        "tipo_estreno": [],
        "duracion": [],
        "genero": [],
        "director": [],
        "calf_medios": [],
        "calf_usuarios": [],
        "calf_rotten_tomatoes": [],
        "nacionalidad": [],
        "distribuidora": [],
        "fecha_produccion": [],
        "presupuesto": [],
        "idioma": []
    }

    # Extraer información de la película
    info_general = soup.find("div", class_="movie_info")
    if info_general:
        pelicula = info_general.find("h1").text.strip()
        temp_datos["pelicula"].append(pelicula)

        # Fecha de estreno
        fecha_estreno = info_general.find("time")
        if fecha_estreno:
            temp_datos["fecha_estreno"].append(fecha_estreno.text.strip())

        # Duración
        duracion = info_general.find("span", class_="duration")
        if duracion:
            temp_datos["duracion"].append(duracion.text.strip())

        # Género
        genero = info_general.find_all("a", class_="genre")
        temp_datos["genero"].append([g.text.strip() for g in genero])

        # Director
        director = info_general.find("a", class_="director")
        if director:
            temp_datos["director"].append(director.text.strip())

        # Calificaciones
        calificaciones = info_general.find("div", class_="tomatometer")
        if calificaciones:
            temp_datos["calf_rotten_tomatoes"].append(calificaciones.text.strip())

        # Imprimir los datos en la consola
        print("Título:", temp_datos["pelicula"][0])
        print("Fecha de Estreno:", temp_datos["fecha_estreno"][0] if temp_datos["fecha_estreno"] else "N/A")
        print("Duración:", temp_datos["duracion"][0] if temp_datos["duracion"] else "N/A")
        print("Género:", ", ".join(temp_datos["genero"][0]) if temp_datos["genero"] else "N/A")
        print("Director:", temp_datos["director"][0] if temp_datos["director"] else "N/A")
        print("Calificación Rotten Tomatoes:", temp_datos["calf_rotten_tomatoes"][0] if temp_datos["calf_rotten_tomatoes"] else "N/A")
        print("\n" + "-"*40 + "\n")