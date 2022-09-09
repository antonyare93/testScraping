from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By

marca = "Sogno"
secciones = {
    "hombre": ["camisetas", "camisilla", "sudaderas-1", "busos-1", "pantalonetas-1", "pantalonetas", "camisetas-oversize"],
    "mujer": ["camisetas-dama", "sudaderas-2", "busos", "croptops", "shorts"],
    "cosas": ["accesorios"]}
fecha = date.today().strftime("%Y%m%d")

with webdriver.Chrome(executable_path="C:/WebDriver/bin/chromedriver_v94_win32/chromedriver.exe") as driver:
    for seccion in secciones:
        prod_json = "Marca| Sección| Categoría| Producto| Precio original| Precio reventa| Vínculo| Imagen|\n"
        for categoria in secciones[seccion]:
            driver.get(f"https://sogno87.com/collections/{categoria}")
            for elementos in driver.find_elements(by=By.CLASS_NAME, value="product-hover-11"):
                try:
                    texto = elementos.find_element(by=By.CLASS_NAME, value="badge--sold-out").text
                except:
                    texto = "none"

                if texto != 'Agotado':
                    item = elementos.find_element(by=By.CLASS_NAME, value="grid-link")
                    item_link = item.get_attribute("href")
                    item = elementos.find_element(by=By.CLASS_NAME, value="featured-image")
                    link_img = item.get_attribute("src")
                    producto = elementos.find_element(by=By.CLASS_NAME, value="grid-link__title").text
                    precio = float(elementos.find_element(by=By.CLASS_NAME, value="product_price").text.replace(",00","").replace(".","").replace("$",""))
                    precio_resell = precio * 1.1
                    prod_json = prod_json + f"{marca}| {seccion}| {categoria}| {producto}| {precio}| {precio_resell}| {item_link}| {link_img}|\n"

                    with open(f"{fecha}_{categoria}_{marca}.csv", "w") as docu:
                        docu.write(prod_json)
                    print(categoria)


