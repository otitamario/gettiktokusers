import requests
from bs4 import BeautifulSoup
from db import dataInsert
import json
def getuser(username):
    url='https://www.tiktok.com/node/share/user/@{0}?aid=1988'.format(username)
    result = requests.get(url, headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Host':'www.tiktok.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
    })
    user=result.json()
    id=user["userInfo"]["user"]["id"]
    return id    

req = requests.get('https://pt.wikipedia.org/wiki/Lista_das_contas_mais_seguidas_no_TikTok')

if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find(name='table', attrs={'class':'wikitable sortable'})
    table_rows = table.find_all("tr")
    for tr in table_rows:
        cells = tr.find_all('td')
        if len(cells) > 0:
            username = cells[0].text.strip()
            nomecadastro= cells[1].text.strip()
            tiktokid=getuser(username[1:])
            dataInsert(nomecadastro,username[1:],tiktokid)