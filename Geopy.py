from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="app-michu")

location = geolocator.geocode('Quito')

print(location)

print((location.latitude), (location.longitude))

location2 = geolocator.reverse("-0.074265, -78.460383")
print(location2)