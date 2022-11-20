import requests
import urllib.parse
def coorfinder(address):
    #put the address in the url
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    #get the response from the site
    response = requests.get(url).json()
    #return latitude and longitude in a form of a string
    lat = response[0]["lat"]
    lon = response[0]["lon"]
    return [float(lat),float(lon)]

