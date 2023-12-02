# Depencencies must include geopy 2.4.1
from geopy.geocoders import Nominatim

# addr variable must be a string with city and zip code included
def addr_to_loc(addr):
    geolocator = Nominatim(user_agent="vadymden")
    location = geolocator.geocode(addr)
    return addr
    #print(location.address)
    #print((location.latitude, location.longitude))
    #print(location.raw)