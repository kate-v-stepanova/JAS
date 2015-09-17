# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bs4 import BeautifulSoup
import datetime

def parse(filename=None):
    if filename is None:
        filename = "JobStatistics.html"
    file = open(filename, 'r+')
    print 'file:', file
    html = file.read()
    file.seek(0)

    print 'html:'

    try: # in case of problems with german symbols ä, ö, ü
        soup = BeautifulSoup(html)
    except UnicodeEncodeError:
        soup = BeautifulSoup(html.decode('ascii'))


    file.write(soup.prettify().encode('utf-8'))

    tbody = soup.tbody
    print tbody
    result = []
    for tr in tbody.find_all('tr')[1:]:
        tds = tr.find_all('td')
        company = tds[0].get_text().strip()
        a = tds[0].a
        url = a.get('href') if a else ''

        location = tds[1].get_text().strip()

        position = tds[2].get_text().strip()
        a = tds[2].a
        position_url = a.get('href') if a else ''
        app_date = datetime.datetime.strptime(tds[3].get_text().strip(), "%d.%m.%Y").date()
        status = tds[4].get_text().strip()

        job_app = {'company': company,
                   'webiste': url,
                   'location': location,
                   'job_position': position,
                   'job_url': position_url,
                   'date': app_date,
                   'status': status}
        result.append(job_app)
    return result
