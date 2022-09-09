from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

marca = "Mattelsa"
secciones = ["mujer", "hombre", "cosas", "sale/hombre", "sale/mujer"]
fecha = date.today().strftime("%Y%m%d")

with webdriver.Chrome(executable_path="C:/WebDriver/bin/chromedriver_v104_win32/chromedriver.exe") as driver:
    for seccion in secciones:
        prod_json = "Marca| Sección| Categoría| Producto| Precio original| Vínculo| Imagen|\n"
        driver.get(f"https://www.mattelsa.net/{seccion}")
        for i in range(110):
            driver.execute_script("window.scrollTo(0, window.scrollY + 600);")
            time.sleep(1)
        seccion = seccion.replace("/", "_")
        for productos in driver.find_elements(by=By.CLASS_NAME, value="product-item"):
            item = productos.find_element(by=By.TAG_NAME, value="img")
            link_img = item.get_attribute("src")
            item = productos.find_element(by=By.TAG_NAME, value="a")
            item_link = item.get_attribute("href")
            item = productos.find_element(by=By.CLASS_NAME, value="first-product-name")
            categoria = item.text
            # item = productos.find_element(by=By.CLASS_NAME, value="last-product-name")
            producto = item_link[-(len(item_link)-(len(driver.current_url)+1)):]
            item = productos.find_element(by=By.CLASS_NAME, value="price-wrapper")
            precio = int(item.get_attribute("data-price-amount"))
            #precio_resell = int(precio*1.1)
            prod_json = prod_json + f"{marca}| {seccion}| {categoria}| {producto}| {precio}| {item_link}| {link_img}|\n"

        with open(f"{fecha}_{seccion}_{marca}.csv", "w") as docu:
            docu.write(prod_json)
