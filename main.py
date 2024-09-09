from bs4 import BeautifulSoup
import json

def get_data():
  with open('csm_avaliacoes_page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

  # Usar BeautifulSoup para processar o HTML
  soup = BeautifulSoup(html_content, 'html.parser')

  # Iniciar lista de matérias
  subjects = []

  # Encontrar todas as seções de matérias
  tables = soup.find_all('table', width="98%")

  for table in tables:
      subject_data = {}

      # Extrair o nome da matéria
      subject_name = table.find_previous('td', class_='topoTabelaResponsavel').text.strip()
      subject_data['subject_name'] = subject_name

      # Iniciar lista de avaliações
      activities = []
      
      # Encontrar todas as tables de avaliações
      rows = table.find_all('tr', bgcolor=["#E5E5E5", "#CCCCCC"])
      for row in rows:
          columns = row.find_all('td')

          if len(columns) == 4:
              activity_data = {
                  "activity_name": columns[0].text.strip(),
                  "max": float(columns[1].text.strip()) if columns[1].text.strip() != '-' else None,
                  "grade": float(columns[2].text.strip()) if columns[2].text.strip() != '-' else None,
                  "percentage": float(columns[3].text.strip().replace(',', '.')) if columns[3].text.strip() != '-' else None
              }
              activities.append(activity_data)
      
      # Adicionar avaliações e somatório na matéria
      subject_data['activities'] = activities 

      # Encontrar o somatório
      somatorio_row = table.find('tr', bgcolor="#CCCCCC")
      if somatorio_row:
          somatorio_columns = somatorio_row.find_all('td')
          subject_data['final_grade'] = {
              "max": float(somatorio_columns[1].text.strip()),
              "grade": float(somatorio_columns[2].text.strip()),
              "percentage": float(somatorio_columns[3].text.strip().replace(',', '.'))
          }
      
      # Adicionar matéria à lista de matérias
      subjects.append(subject_data)

  # Converter a lista de matérias em JSON
  json_data = {"subjects": subjects}
  json_output = json.dumps(json_data, indent=4, ensure_ascii=False)

  # Escrever o JSON
  with open('subjects_data.json', 'w', encoding='utf-8') as json_file:
      json_file.write(json_output)