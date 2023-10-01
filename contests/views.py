import re

from django.shortcuts import render
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
import requests
from base64 import b64encode, b64decode

from bs4 import BeautifulSoup, ResultSet

app_name = APP_NAMES.CONTESTS
verbose_name = VERBOSE_APP_NAMES.CONTESTS


def parse_contests(url):
    res = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    contestTables = soup.findAll('table', border="0", cellpadding="0", cellspacing="0", width="100%")
    # print(soup)
    # print('PARSED')
    for tab in contestTables:

        if tab.h3 is not None:
            contestData = {}
            contestName = " ".join(tab.h3.text.split())
            contestRef = f"https://www.architime.ru/{tab.h3.a.get('href')}"
            contestImgURL = f"https://www.architime.ru/{tab.td.a.img.get('src')}"

            response = requests.get(contestImgURL, stream=True)
            content = response.content
            contestImgBase64 = b64encode(content).decode('utf-8')

            contestData['contestName'] = contestName
            contestData['contestRef'] = contestRef
            contestData['contestImg'] = contestImgURL
            contestData['contestImgBase64'] = contestImgBase64

            contestDetales = tab.findAll('table', border="0", cellpadding="0", cellspacing="11", width="600")

            for td in contestDetales:
                contest_row = " ".join(td.text.split())
                contest_desc = re.split(r'\s+(?=[А-Я])', contest_row)
                contestData['contestDesc'] = contest_desc

            res.append(contestData)
    return res


def contestsView(request):
    context = {}
    contestsData = parse_contests('https://www.architime.ru/compexibition.htm')

    context['contests'] = contestsData
    context['page_name'] = verbose_name
    context['page_style'] = app_name
    # return context

    return render(request, template_name=f'./{app_name}/{app_name}.html', context=context)



