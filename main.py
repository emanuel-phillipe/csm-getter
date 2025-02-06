from bs4 import BeautifulSoup
import json
from get_website import get_html_website_code

def get_data(html_page_code):
    html_content = html_page_code

    # processar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    subjects = []

    # encontra no site as tabelas das matérias
    tables = soup.find_all('table', width="98%")

    for table in tables:
        subject_data = {}

        # pegar o nome de cada matéria
        subject_name = table.find_previous('td', class_='topoTabelaResponsavel').text.strip()
        subject_data['subject_name'] = subject_name

        activities = []
        
        # encontra as atividades dentro das matérias
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
        
        # adiciona as atividades dentro de cada matéria
        subject_data['activities'] = activities 

        # pega o total da matéria no site
        somatorio_row = table.find('tr', bgcolor="#CCCCCC")
        if somatorio_row:
            somatorio_columns = somatorio_row.find_all('td')
            subject_data['final_grade'] = {
                "max": float(somatorio_columns[1].text.strip()),
                "grade": float(somatorio_columns[2].text.strip()),
                "percentage": float(somatorio_columns[3].text.strip().replace(',', '.'))
            }
        
        subjects.append(subject_data)

    json_data = {"subjects": subjects}
    json_output = json.dumps(json_data, indent=4, ensure_ascii=False)

    with open('subjects_data.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_output)
        print("Arquivo JSON gerado")

    return json_output

html = get_html_website_code()
print(get_data(html))
