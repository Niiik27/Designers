import re
import datetime
from django.shortcuts import render
from APP_NAMES import APP_NAMES, VERBOSE_APP_NAMES
import requests
from base64 import b64encode, b64decode

from bs4 import BeautifulSoup, ResultSet

app_name = APP_NAMES.CONTESTS
verbose_name = VERBOSE_APP_NAMES.CONTESTS
def get_date(date):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']


    # longest_length = max([len(s) for s in day_list])
    # print(max([s for s in day_list if len(s) == longest_length], key=len))
    #
    # longest_length = max([len(s) for s in month_list])
    # print(max([s for s in month_list if len(s) == longest_length], key=len))
    #
    # return 'двадацать четвёртое сентября 2023 года'#longest string

    date_list = date.split('.')
    return (day_list[int(date_list[0]) - 1] + ' ' +
        month_list[int(date_list[1]) - 1] + ' ' +
        date_list[2] + ' года')


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
            pathURL = contestImgURL.split("?")[0]
            imgExt = pathURL[pathURL.rfind('.') + 1:len(pathURL)]

            response = requests.get(contestImgURL, stream=True)
            content = response.content
            contestImgBase64 = b64encode(content).decode('utf-8')
            if not contestImgBase64: continue
            contestData['contestName'] = contestName
            contestData['contestRef'] = contestRef
            contestData['contestImg'] = contestImgURL
            contestData['imgExt'] = imgExt
            contestData['contestImgBase64'] = contestImgBase64

            contestDetales = tab.findAll('table', border="0", cellpadding="0", cellspacing="11", width="600")

            for td in contestDetales:
                contest_row = " ".join(td.text.split())
                contest_desc = re.split(r'\s+(?=[А-Я])', contest_row)
                contestData['contestDesc'] = contest_desc
            for string in contestData.get('contestDesc',[]):
                if 'тип участия' in string.lower():
                    contestData['freeFlag'] = 'бесплатный' in string.lower()
                    break


            for string in contestData.get('contestDesc',[]):
                match = re.search(r'\d{2}.\d{2}.\d{2}', string)
                regData = datetime.datetime.strptime(match.group(), "%d.%m.%y").date()
                if regData:
                    # contestData['regData'] = get_date(match.group())
                    contestData['regData'] = get_date(f'{regData.day}.{regData.month}.{regData.year}')
                    break


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



