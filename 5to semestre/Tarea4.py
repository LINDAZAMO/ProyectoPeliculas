#Tarea 4
#Linda Jaqueline Vazquez Zamora

import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def webscrapping(Nom_Producto, Pag_num):
    s = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1200,1200")
    navegador = webdriver.Chrome(service=s, options=options)

    data = {"nombre del producto": [], "precio": [], "calificacion": []}

    navegador.get("https://www.bestbuy.com/?intl=nosplash")
    time.sleep(5)

    search_box = WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-input")))
    search_box.send_keys(Nom_Producto)
    search_box.submit()

    for i in range(Pag_num):
        WebDriverWait(navegador, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "sku-item")))
        soup = BeautifulSoup(navegador.page_source, "html.parser")
        productos = soup.find_all("li", class_="sku-item")

        for producto in productos:
            nombre = producto.find("h4", class_="sku-title")
            precio = producto.find("div", class_="priceView-hero-price priceView-customer-price")
            calificacion = producto.find("div", class_="ratings-reviews")

            data["Nombre del Producto"].append(nombre.get_text(strip=True) if nombre else "N/A")
            data["Precio"].append(precio.get_text(strip=True) if precio else "N/A")
            data["Calificacion"].append(calificacion.get_text(strip=True) if calificacion else "N/A")

        try:
            next_button = WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "sku-list-page-next")))
            next_button.click()
            time.sleep(5)
        except Exception as e:
            print("Error, No hay más páginas que mostrar:", e)
            break

    navegador.quit()

    df = pd.DataFrame(data)
    output_dir = "Data_Frame_Play4"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df.to_csv(os.path.join(output_dir, f"{Nom_Producto}_data.csv"), index=False)

    return df

if __name__ == "__main__":
    df = webscrapping("Play4", 3)
    print(df)
