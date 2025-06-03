from selenium import webdriver
from selenium.webdriver.common.by import By

# Abre el navegador Chrome
driver = webdriver.Chrome()

# Visita Google
driver.get("https://www.google.com")

# Escribe "Python Selenium" en el cuadro de búsqueda
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python Selenium")

# Envía el formulario
search_box.submit()

# Espera unos segundos y cierra el navegador
import time
time.sleep(5)
driver.quit()
