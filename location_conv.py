# Depencencies must include geopy 2.4.1
from geopy.geocoders import Nominatim

# addr variable must be a string with city and zip code included (Ex: "1234 Main St SE City, State 12345") 
# Returns an array with long and lat elements
def addr_to_loc(addr):
    geolocator = Nominatim(user_agent="vadymden")
    location = geolocator.geocode(addr)
    return f"{location.latitude}, {location.longitude}"