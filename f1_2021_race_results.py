import requests
from bs4 import BeautifulSoup

links = [
    'https://www.motorsport.com/f1/results/2021/bahrain-gp-483475/',
    'https://www.motorsport.com/f1/results/2021/emilia-romagna-gp-490126/',
    'https://www.motorsport.com/f1/results/2021/portuguese-gp-527685/',
    'https://www.motorsport.com/f1/results/2021/spanish-gp-483481/',
    'https://www.motorsport.com/f1/results/2021/monaco-gp-483492/',
    'https://www.motorsport.com/f1/results/2021/azerbaijan-gp-483496/',
    'https://www.motorsport.com/f1/results/2021/french-gp-483502/',
    'https://www.motorsport.com/f1/results/2021/styrian-gp-533054/',
    'https://www.motorsport.com/f1/results/2021/austrian-gp-483505/',
    'https://www.motorsport.com/f1/results/2021/british-gp-483508/',
    'https://www.motorsport.com/f1/results/2021/hungarian-gp-483511/',
    'https://www.motorsport.com/f1/results/2021/belgian-gp-483515/',
    'https://www.motorsport.com/f1/results/2021/dutch-gp-483518/',
    'https://www.motorsport.com/f1/results/2021/italian-gp-483521/',
    'https://www.motorsport.com/f1/results/2021/russian-gp-/',
    'https://www.motorsport.com/f1/results/2021/turkish-gp-532228/',
    'https://www.motorsport.com/f1/results/2021/united-states-gp-/',
    'https://www.motorsport.com/f1/results/2021/mexican-gp-483539/',
    'https://www.motorsport.com/f1/results/2021/brazilian-gp-483553/',
    'https://www.motorsport.com/f1/results/2021/qatar-gp-538207/',
    'https://www.motorsport.com/f1/results/2021/saudi-arabia-gp-/',
    'https://www.motorsport.com/f1/results/2021/abu-dhabi-gp-483561/'
]

races = [
    'bahrain-gp',
    'emilia-romagna-gp',
    'portuguese-gp',
    'spanish-gp',
    'monaco-gp',
    'azerbaijan-gp',
    'french-gp',
    'styrian-gp',
    'austrian-gp',
    'british-gp',
    'hungarian-gp',
    'belgian-gp',
    'dutch-gp',
    'italian-gp',
    'russian-gp',
    'turkish-gp',
    'united-states-gp',
    'mexican-gp',
    'brazilian-gp',
    'qatar-gp',
    'saudi-arabia-gp',
    'abu-dhabi-gp'
]

for i in range(len(links)):
    print(links[i])
    page = requests.get(links[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')
    result_lines = []
    for row in rows:
        row_text = [x.text.strip() for x in row.find_all('td')]
        result_lines.append(','.join(row_text))
        with open('race/race_'+races[i]+'.txt', 'w') as file:
            for line in result_lines:
                file.write(line+'\n')