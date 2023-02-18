import urllib.request, json

with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as url:
    data = json.load(url)

iss_position = (float(data["iss_position"]["latitude"]),
								float(data["iss_position"]["longitude"]))

# Positions are very rough, erring on covering extra ground
def aboveDuluth(point):
	if -92.81 < iss_position[0] < -91.81 and 46.61 < iss_position[1] < 46.92:
		return True
	else:
		return False

def aboveMN(point):
	if -97.5 < iss_position[0] < -89.5 and 43.5 < iss_position[1] < 48.9:
		return True
	else:
		return False

def aboveUSA(point):
	if -124.5 < iss_position[0] < -66.7 and 25.6 < iss_position[1] < 49.4:
		return True
	else:
		return False

print(f"Current iss latitude: {iss_position[0]}, longitude: {iss_position[1]}")
print("The ISS is over USA: ", aboveUSA(iss_position))
print("The ISS is over MN: ", aboveMN(iss_position))
print("The ISS is over Duluth: ", aboveDuluth(iss_position))
