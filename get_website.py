from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from main import get_data

def get_website():
  driver = webdriver.Chrome()
  driver.get("https://www.sistemas.pucminas.br/sgcaluno/SilverStream/Pages/pgResp_LoginSSL.html")

  driver.find_element(By.NAME, "S41_").send_keys("892628")
  driver.find_element(By.NAME, "S43_").send_keys("emanuel")
  driver.find_element(By.NAME, "S45_").click()

  sleep(1)

  driver.find_element(By.LINK_TEXT, "Ensino Médio - 3ª série - COLÉGIO SANTA MARIA MINAS - UNIDADE CORAÇÃO EUCARÍSTICO").click()

  sleep(1)

  driver.find_element(By.LINK_TEXT, "Avaliações").click()

  sleep(1)

  subjects_table = driver.find_element(By.CSS_SELECTOR, "table[width='100%'][border='0'][cellspacing='0'][cellpadding='2']").get_attribute("innerHTML")

  with open('csm_avaliacoes_page.html', 'w', encoding='utf-8') as html_file:
      html_file.write(subjects_table)

  get_data()

get_website()