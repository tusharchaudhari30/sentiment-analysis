import re

data = "feels sad @TusharChaudhari coz i wasnt able to play with the guys!!!  http://plurk.com/p/wxiux  ♥§☻↓"
data = re.sub(
    r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', data)
data = re.sub('[^A-Za-z0-9\s]+', '', data)
data = re.sub('@', '', data)
data = data.lower()
print(data)
