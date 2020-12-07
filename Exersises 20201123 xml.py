from bs4 import BeautifulSoup as bs
import os

content = []

projPath = os.getcwd()
result = sorted(os.listdir(projPath))
for n, item in enumerate(result):
    print(n + 1, item)
print("-" * 15)
fileName = os.path.join(projPath, result[9])   # номер файла gpx в списке объектов в директории
print(fileName)

separator = "trkpt"
# sFile = open(fileName, 'rt')
# Read the XML file
with open(fileName, "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    bs_content = bs(content, "lxml")

points = bs_content.find_all(separator)
for n, item in enumerate(points):
    pointData = list(item.strings)
    lat = float(item.get("lat"))
    lon = float(item.get("lon"))


    print(n + 1, pointData, lat, lon,)
