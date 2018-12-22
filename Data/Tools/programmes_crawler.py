"""
    /!\ Dangerous area /!\
    This script downloads last entire year "programme", wich lists all races of the day and links to them.
    It's directly connecting to PMU servers ! So be really carefull with timing !
"""

import requests
from datetime import date, timedelta
import time
import math

URL = "https://tablette.turfinfo.api.pmu.fr/rest/client/1/programme/"

def write(date, content):
    with open('/home/tom/Documents/Programmation/Python/OpenBet/Data/Raw/programme_' + date + '.json', 'w+') as file:
        file.write(content)

# Download last x days
DAYS_BEFORE = 365

for i in range(DAYS_BEFORE):
    # We get today - i date, format ddmmYYYY
    d = date.today() - (timedelta(i))
    d_str = d.strftime('%d%m%Y')

    url = URL + d_str
    r = requests.get(url)
    write(d_str, r.text)

    print(str(math.floor(i / DAYS_BEFORE * 100)) + "%")
    # Don't try to reduce more, or you'll be banned of PMU servers !!
    time.sleep(10)
