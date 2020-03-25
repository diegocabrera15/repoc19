from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="app-michu")

location = geolocator.geocode('Quito')

print(location)
