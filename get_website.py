from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def get_html_website_code():
  options = webdriver.ChromeOptions()

  options.add_argument('headless')
  options.add_argument('window-size=1920x1080')
  options.add_argument("disable-gpu")

  driver = webdriver.Chrome(options=options)

  driver.get("https://www.sistemas.pucminas.br/sgcaluno/SilverStream/Pages/pgResp_LoginSSL.html")

  print("Entrando no site")

  driver.find_element(By.NAME, "S41_").send_keys("892628")
  driver.find_element(By.NAME, "S43_").send_keys("emanuel")
  driver.find_element(By.NAME, "S45_").click()

  print("Logando na sua conta")
  sleep(1)

  driver.find_element(By.LINK_TEXT, "Ensino Médio - 3ª série - COLÉGIO SANTA MARIA MINAS - UNIDADE CORAÇÃO EUCARÍSTICO").click()

  print("Aluno selecionado")
  sleep(1)

  driver.find_element(By.LINK_TEXT, "Avaliações").click()

  print("Página da avaliações alcançada")
  sleep(1)

  subjects_table_html = driver.find_element(By.CSS_SELECTOR, "table[width='100%'][border='0'][cellspacing='0'][cellpadding='2']").get_attribute("innerHTML")

  print("Página captada")
  return subjects_table_html

  #with open('csm_avaliacoes_page.html', 'w', encoding='utf-8') as html_file:
  #    html_file.write(subjects_table)