#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib
import re
import sys

def get_title(row):
    title_link = row.find('a', {'class':'comp-link'})
    return title_link.text

def is_title(competition, row):
    return get_title(row) == competition

def get_position(row):
    time_strings = []
    time_cell = row.find('td', {'class':'comp-time'})
    for string in time_cell.stripped_strings:
        time_strings.append(string)

    return int(re.findall('\d+', time_strings[1])[0])

def get_status(row):
    time_strings = []
    time_cell = row.find('td', {'class':'comp-time'})
    for string in time_cell.stripped_strings:
        time_strings.append(string)

    isCurrent = time_strings[0] == u'Currently'
    
    status = ''
    if isCurrent:
        status = 'Currently'
    else:
        status = 'Finished'

    return status

def get_total_contestants(row):
    time_strings = []
    time_cell = row.find('td', {'class':'comp-time'})
    for string in time_cell.stripped_strings:
        time_strings.append(string)

    return int(re.findall('\d+', time_strings[2])[0])

def get_results(user, competition):
    link = urllib.urlopen('http://www.kaggle.com/users/' + user)
    doc = link.read()

    soup = BeautifulSoup(doc)
    results = soup.find('table', {'class':'profile-comp-list'})
    results_table_rows = results.find_all('tr')

    for row in results_table_rows:
        if is_title(competition, row):
            print get_position(row)

def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: " + sys.argv[0] + 
                        ' <#/username> <competition>\n') 
        sys.exit()
    
    get_results(sys.argv[1], sys.argv[2])

main()
