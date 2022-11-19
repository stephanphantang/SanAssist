from math import radians, cos, sin, asin, sqrt
from LatLonFinder import coorfinder
#Input: two list with [latitude,longitude] output the distance in kilometers
def distance(coor1, coor2):
    lon1,lat1 =coor1
    lon2,lat2 = coor2
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. 
    r = 6371
      
    # calculate the result
    return(c * r)
     
     
# driver code
ville1 = coorfinder("Marseille")
ville2 = coorfinder("Paris")

print(distance(ville1,ville2))

