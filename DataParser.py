import requests
from bs4 import BeautifulSoup

result = requests.get("http://www.nfl.com/stats/categorystats"
                      "?tabSeq=0&statisticCategory=PASSING&conference=null&season=2017"
                      "&seasonType=REG&d-447263-s=PASSING_YARDS&d-447263-o=2&d-447263-n=1")
#print result.status_code
#print result.headers

c = result.text
soup = BeautifulSoup(c, "html.parser")
tables = soup.findChildren('table')
my_table = tables[0]

rows = my_table.findChildren(['th', 'tr'])

# Get data from the table
for row in rows:
    cells = row.findChildren('td')
    for cell in cells:
        value = cell.string
        if value is not None:
            value = cell.string.split()
            print value[-1]
