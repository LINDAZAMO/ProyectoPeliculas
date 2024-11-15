import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def facebook():
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size = 1020, 1200")

    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.facebook.com/?locale=es_LA")

    txtEmail = navegador.find_element(By.NAME, "email")
    txtCorreo = navegador.find_element(By.NAME, "pass")
    btnLogin = navegador.find_element(By.NAME,"login")


    txtEmail.send_keys("linda@gmail.com")
    time.sleep(2)

    txtCorreo.send_keys("linda1234")
    time.sleep(2)
    btnLogin.click()

    time.sleep(5)
    navegador.save_screenshot("imagen_test.png")
    time.sleep(10)
    navegador.close()


if __name__ == "__main__":
    facebook()