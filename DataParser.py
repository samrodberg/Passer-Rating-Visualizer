import requests
import json
import logging
from bs4 import BeautifulSoup

result = requests.get("http://www.nfl.com/stats/categorystats"
                      "?tabSeq=0&statisticCategory=PASSING&conference=null&season=2017"
                      "&seasonType=REG&d-447263-s=PASSING_YARDS&d-447263-o=2&d-447263-n=1")
try:
    result.status_code == 200
except Exception as e:
    logging.exception('Bad status code: ' + str(e))

c = result.text
soup = BeautifulSoup(c, "html.parser")


# Gets statistical data for QB's such as tds, yds, comp, att, etc. does not get name of player or team
def get_qb_data(printing=True):
    data = []
    tables = soup.findChildren('table')
    my_table = tables[0]
    rows = my_table.findChildren(['th', 'tr'])
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string
            if value is not None:
                value = cell.string.split()
                value = value[0].encode('utf-8')
                data.append(value)
                if printing is True:
                    print value
    if printing is True:
        print data
    return data


# Gets QB's info specifically name and team
def get_qb_info(printing=True):
    players = soup.select("a[href^=/players/]")
    teams = soup.select("a[href^=/teams/]")
    players_list = [_.text.encode('utf-8') for _ in players]
    teams_list = [_.text.encode('utf-8') for _ in teams]
    if printing is True:
        print players_list
        print teams_list
    qb_info = zip(players_list, teams_list)
    return qb_info


# Format data for easy printing and to match table format of NFL.com
def format_data_list(printing=True):
    qb_data_format = get_qb_data(printing=False)
    qb_info_format = get_qb_info(printing=False)
    sub_lists = [qb_data_format[item:item+18] for item in range(0, len(qb_data_format), 18)]
    player_names, team_names = zip(*qb_info_format)
    index = 0
    for sub in sub_lists:
        sub.insert(1, player_names[index])
        sub.insert(2, team_names[index])
        index += 1
        if printing is True:
            print sub
    return sub_lists


# Format data as JSON for future use
def format_data_json(ranking, printing=True):
    ranking -= 1
    keys = ['rk', 'player', 'team', 'pos', 'comp', 'att', 'pct', 'att_g', 'yds', 'avg', 'yds_g', 'td', 'ints', '1st',
            '1st_percent', 'lng', '20_plus', '40_plus', 'sck', 'passer_rating']
    values = format_data_list(printing=False)
    dictionary = dict(zip(keys, values[ranking]))
    json_data = json.dumps(dictionary, indent=2)
    if printing is True:
        print json.dumps(dictionary, indent=2)
    return json_data


# Print out all data in json format
def print_all_data_json():
    for i in range(1,len(format_data_list(printing=False))):
        format_data_json(i, printing=True)