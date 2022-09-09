from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

marca = "True"
categorias = ["camisetas", "buzos-y-chaquetas", "pantalones-y-sudaderas", "croptops", "bikers-y-shorts", "gorras-y-accesorios"]
fecha = date.today().strftime("%Y%m%d")

with webdriver.Chrome(executable_path="C:/WebDriver/bin/chromedriver_v104_win32/chromedriver.exe") as driver:
    for categoria in categorias:
        prod_json = "Marca| Sección| Categoría| Producto| Precio original| Vínculo| Imagen|\n"
        driver.get(f"https://www.trueshop.co/collections/{categoria}")
        for i in range(110):
            driver.execute_script("window.scrollTo(0, window.scrollY + 600);")
            time.sleep(1)
        for productos in driver.find_elements(by=By.CLASS_NAME, value="grid-view-item"):
            producto_html = productos.find_element(by=By.CLASS_NAME, value="slick-active")
            # item = producto_html.find_element(by=By.TAG_NAME, value="a")
            item_link = producto_html.get_attribute("href")
            item = producto_html.find_element(by=By.TAG_NAME, value="img")
            link_img = item.get_attribute("src")
            producto_html = productos.find_element(by=By.CLASS_NAME, value="details")
            producto = producto_html.text
            item = producto_html.find_element(by=By.CLASS_NAME, value="product-price__price")
            precio = float(((item.text).replace(".", "")).replace("$", ""))
            #except:
            #    precio = float(((item.text).replace(",", "")).replace("$", ""))
            #precio_resell = float(precio*1.1)
            if categoria == "camisetas":
                re_categoria = "CAMISETA"
                if producto.lower().find("mesh") > 0:
                    secciones = ["mujer"]
                else:
                    secciones = ["hombre", "mujer"]
            elif producto.lower().find("hoodie") > 0 or producto.lower().find("pullover") > 0 or producto.lower().find("sweater") > 0:
                re_categoria = "BUZO"
                if producto.lower().find("cropped") > 0:
                    secciones = ["mujer"]
                else:
                    secciones = ["hombre", "mujer"]
            elif producto.lower().find("jacket") > 0:
                re_categoria = "CHAQUETA"
                secciones = ["hombre", "mujer"]
            elif producto.lower().find("pants") > 0:
                re_categoria = "SUDADERA"
                secciones = ["hombre", "mujer"]
            elif producto.lower().find("jeans") > 0:
                re_categoria = "JEANS"
                secciones = ["hombre", "mujer"]
            elif producto.lower().find("jogger") > 0:
                re_categoria = "JOGGERS"
                secciones = ["hombre", "mujer"]
            elif producto.lower().find("bikini") > 0:
                re_categoria = "BIKINI"
                secciones = ["mujer"]
            elif producto.lower().find("top") > 0:
                re_categoria = "TOP"
                secciones = ["mujer"]
            elif producto.lower().find("biker") > 0:
                re_categoria = "BIKERS"
                secciones = ["mujer"]
            elif producto.lower().find("shorts") > 0:
                re_categoria = "SHORTS"
                secciones = ["mujer"]
            elif producto.lower().find("leggings") > 0:
                re_categoria = "LEGGINGS"
                secciones = ["mujer"]
            elif categoria == "croptops":
                if producto.lower().find("top") > 0 or producto.lower().find("bra") > 0:
                    re_categoria = "TOP"
                elif producto.lower().find("bodysuit") > 0:
                    re_categoria = "BODY"
                secciones = ["mujer"]
            elif categoria == "gorras-y-accesorios":
                if producto.lower().find("cap") > 0:
                    re_categoria = "GORRAS"
                elif producto.lower().find("hat") > 0:
                    re_categoria = "SOMBREROS"
                elif producto.lower().find("patch") > 0 or producto.lower().find("beanie") > 0:
                    re_categoria = "GORROS"
                elif producto.lower().find("socks") > 0:
                    re_categoria = "SOMBREROS"
                elif producto.lower().find("fannypack") > 0:
                    re_categoria = "CANGUROS"
                elif producto.lower().find("backpack") > 0:
                    re_categoria = "MORRALES"
                elif producto.lower().find("totebag") > 0:
                    re_categoria = "SHOPPING"
                elif producto.lower().find("tapabocas") > 0:
                    re_categoria = "TAPABOCAS"
                else:
                    re_categoria = "VERIFICAR CATEGORIA"

                secciones = ["cosas"]
            else:
                print(categoria)

            for seccion in secciones:
                prod_json = prod_json + f"{marca}| {seccion}| {re_categoria}| {producto}| {precio}| {item_link}| {link_img}|\n"

        with open(f"{fecha}_{categoria}_{marca}.csv", "w") as docu:
            docu.write(prod_json)