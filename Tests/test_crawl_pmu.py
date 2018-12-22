import dryscrape
session = dryscrape.Session()
session.visit("https://www.pmu.fr/turf/21122018/R2/C1")
response = session.body()

print(response)
