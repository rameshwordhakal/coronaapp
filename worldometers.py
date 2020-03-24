import requests
from bs4 import BeautifulSoup

def get_statistics():
    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    trs = soup.findAll('tr', attrs = {'style': ""})

    countries = []

    for tr in trs:
        stats = {}
        for index, td in enumerate(tr):
            if index == 1:
                if td.text != "Country,Other":
                    if td.text.strip():
                        stats['country'] = td.text

            if index == 3:
                if td.text != "TotalCases":
                    if td.text.strip():
                        stats['total_cases'] = int(float(td.text.replace(',', '')))

            if index == 5:
                if td.text != "NewCases":
                    if td.text.strip():
                        stats['new_cases'] = int(float(td.text.replace(',', '')))
            
            if index == 7:
                if td.text != "TotalDeaths":
                    if td.text.strip():
                        stats['total_deaths'] = int(float(td.text.replace(',', '')))

            if index == 9:
                if td.text != "NewDeaths":
                    if td.text.strip():
                        stats['new_deaths'] = int(float(td.text.replace(',', '')))

            if index == 11:
                if td.text != "TotalRecovered":
                    if td.text.strip():
                        stats['total_recovered'] = int(float(td.text.replace(',', '')))

            if index == 13:
                if td.text != "ActiveCases":
                    if td.text.strip():
                        stats['active_cases'] = int(float(td.text.replace(',', '')))

            if index == 15:
                if td.text != "Serious,Critical":
                    if td.text.strip():
                        stats['serious_cases'] = int(float(td.text.replace(',', '')))

            if index == 17:
                if td.text != "Tot\xa0Cases/1M pop":
                    if td.text.strip():
                        stats['tot_cases'] = int(float(td.text.replace(',', '')))
        countries.append(stats)

    return list(filter(None, countries))