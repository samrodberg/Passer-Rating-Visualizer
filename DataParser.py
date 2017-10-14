import requests
from bs4 import BeautifulSoup

result = requests.get("http://www.nfl.com/stats/categorystats"
                      "?tabSeq=0&statisticCategory=PASSING&conference=null&season=2017"
                      "&seasonType=REG&d-447263-s=PASSING_YARDS&d-447263-o=2&d-447263-n=1")
#print result.status_code
#print result.headers

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

qb_data = get_qb_data(printing=False)
qb_info = get_qb_info(printing=False)


def format_data(printing=True):
    qb_data = get_qb_data(printing=False)
    qb_info = get_qb_info(printing=False)
    print qb_data
    print qb_info

format_data(printing=True)
