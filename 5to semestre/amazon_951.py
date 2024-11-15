import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def imagenes(paginas,busqueda):
    s = Service()
    opc = Options()
    opc.add_argument("--window-zise+1020,1200")
    navegador = webdriver.Chrome(service=s,options=opc)

    navegador.get("https://www.amazon.com.mx/")
    time.sleep(10)
    txtInput = navegador.find_element(By.ID,"twotabsearchtextbox")
    txtInput.send_keys(busqueda)
    txtInput.submit()
    time.sleep(10)

    data = {"titulo": [], "precio": []}
    for item in range(paginas):
        navegador.save_screenshot(f"CAPTURASAMAZON/{busqueda}_{item}.png")
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        productos = soup.find_all("div",
        attrs={""})

        for item in productos:
            titulo = item.find
            precio = item.find
            print(titulo.prettify())
            print(precio.prettify())
        navegador.page_source
        btnSiguiente = navegador.find_element(By.LINK_TEXT, "Siguiente")
        btnSiguiente.click()


    navegador.quit()

if __name__=="__main__":
    busqueda= "nintendo"
    paginas= 3
    imagenes(paginas,busqueda)


