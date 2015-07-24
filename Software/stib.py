import requests
from xml.etree import ElementTree as ET


url = "http://m.stib.be/api/getitinerary.php?line=5&iti=1"
response = requests.get(url)

stops = ET.fromstring(response.content)

# root = stops.getroot()
for stop in stops:
    print"%18s" % (stop.find("name").text),
    present = stop.find("present")
    if present is not None:
        print("\t" + stop.find("present").text),

    print("")

print("")
url = "http://m.stib.be/api/getitinerary.php?line=5&iti=2"
response = requests.get(url)

stops = ET.fromstring(response.content)

# root = stops.getroot()
for stop in stops:
    print"%18s" % (stop.find("name").text),
    present = stop.find("present")
    if present is not None:
        print("\t" + stop.find("present").text),

    print("")

url = "http://m.stib.be/api/getwaitingtimes.php?&halt=8711"
response = requests.get(url)

waitingTimes = ET.fromstring(response.content)

# root = stops.getroot()
print("")
for time in waitingTimes:
    destination = time.find("destination")
    minutes = time.find("minutes")
    if minutes is not None and destination is not None:
        print "%18s" % (destination.text),
        print("\t" + minutes.text + "'"),
        print("")


url = "http://m.stib.be/api/getwaitingtimes.php?&halt=8712"
response = requests.get(url)

waitingTimes = ET.fromstring(response.content)

# root = stops.getroot()
print("")
for time in waitingTimes:
    destination = time.find("destination")
    minutes = time.find("minutes")
    if minutes is not None and destination is not None:
        print "%18s" % (destination.text),
        print("\t" + minutes.text + "'"),
        print("")

