# OpenBet

## What's OpenBet ?
The goal of OpenBet is to determine the best bet on a horse race.
I have made a similar project for football : https://github.com/t0mm4rx/Pronostaic.
With this project, I was able to predict about 60% of results. The problem is that a 60% result isn't sufficient to make money with betting. An other problem is that this software was recalculating FDJ (french betting company) odds. So I was playing directly against a team of statisticians.
With horse races, called TURF in France, you play against other player, cause it's a common pot. So the machine learning advantage is way higher. Horses are more predictable than football, and there are many data available.

## How to download data ?
The dataset we get is an archive of all races of this year. The filenames are formatted this way : "date_RxCy" with date '%d%m%y', x the event number and y the race number.
- First, in the "Data" folder, create 3 sub-subfolders : "ProgrammesRaw", "RacesRaw" and "Races"
- All the data downloading and formatting tools are in the Data/Tools folder. In these scripts, replace my home path by your own.
- Run first "programmes_crawler.py". It will download "programmes" (all races for given day) of the last year, about 100Mo and 1 hour download.
- Then run "races_crawler.py". It will download all races data descibed in the previously downloaded programmes, about 110Mo and 6 hours download. Don't try to fast it up, we are not supposed to use the API we use.
- Run "data_cleaner.py". It will merge the past downloaded files and format it the way we want. It takes a few seconds depending on your hardware. It generates 160Mo of clean data.

## Dependencies
- requests (pip install requests)
- Tensorflow
