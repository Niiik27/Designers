import re

from django.shortcuts import render
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
import requests
from bs4 import BeautifulSoup, ResultSet

app_name = APP_NAMES.CONTESTS
verbose_name = VERBOSE_APP_NAMES.CONTESTS

def parse_contests(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    contestTables = soup.findAll('table', border="0", cellpadding="0", cellspacing="0", width="100%")
    # print(soup)
    print('PARSED')
    for tab in contestTables:
        if tab.h3 is not None:
            contestName = " ".join(tab.h3.text.split())
            ref = f"https://www.architime.ru/{tab.h3.a.get('href')}"
            img = f"https://www.architime.ru/{tab.td.a.img.get('src')}"
            print(contestName)
            print(ref)
            print(img)
        contestDetales = tab.findAll('table', border="0", cellpadding="0", cellspacing="11", width="600")
        # ResultSet.
        contest_desc=""
        for td in contestDetales:
            contest_row = " ".join(td.text.split())
            contest_desc = re.split(r'\s+(?=[А-Я])', contest_row)
        print(contest_desc)




parse_contests('https://www.architime.ru/compexibition.htm')


def contestsView(request):
    return render(request, template_name=f'./{app_name}/{app_name}.html', context={'page_name':verbose_name,'page_style':app_name})
