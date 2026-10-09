import phonenumbers
import opencage
import folium

from myphone import number
from myphone import number_2
from myphone import number_3

from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

# current_number=number
# current_number=number_2
current_number=number_3
# -------------------------------------------------------------------------------------- location
pepnumber = phonenumbers.parse(current_number)
location = geocoder.description_for_number(pepnumber, "en")
print("location  ---", location)

#-------------------------------------------------------------------------------------- service_pro
service_pro = phonenumbers.parse(current_number)
print("service_pro ---", carrier.name_for_number(service_pro, "en"))


#-------------------------------------------------------------------------------------- geocoder
key = 'fb02bf3e35bd454cacdc8771567c1e8e'

geocoder = OpenCageGeocode(key)

query = str(location)
result = geocoder.geocode(query)
# print("result --- ",result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

#------------------------------------------------------------------------------------ myMap
myMap = folium.Map(location=[lat,lng], zoom_start = 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("Current_location.html")






