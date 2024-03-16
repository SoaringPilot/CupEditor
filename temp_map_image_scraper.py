# Python program to get a google map
# image of specified location using
# Google Static Maps API

# importing required modules
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Enter your api key here
api_key = "AIzaSyCKlgfABXh7dYM3gZG3CLBcoW0nT9NaL9M"

# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"

center = "Dehradun"

# zoom defines the zoom
# level of the map
zoom = 10

# get method of requests module
# return response object
# r = requests.get(url + "center =" + center + "&zoom =" +
#                  str(zoom) + "&size = 400x400&key =" +
#                  api_key + "sensor = false")
# Bhanson = 36.0208333,-80.5163889, Zoom 15 is good
# r = requests.get("http://maps.googleapis.com/maps/api/staticmap?center=${location.coords.lat},${location.coords.lng}&zoom=17&size=400x350&sensor=false&markers=${location.coords.lat},${location.coords.lng}&scale=2&key=AIzaSyCKlgfABXh7dYM3gZG3CLBcoW0nT9NaL9M")
string0 = "http://maps.googleapis.com/maps/api/staticmap?center="
string1 = "&size=2000x2000&zoom=16&markers="
string2 = "&scale=2&key=AIzaSyCKlgfABXh7dYM3gZG3CLBcoW0nT9NaL9M&maptype=satellite"
lat = "36.0208333"
long = "-80.5163889"
r = requests.get(string0 + lat + "," + long + string1 + lat + "," + long + string2)

# wb mode is stand for write binary mode
f = open('image.png', 'wb')

# r.content gives content,
# in this case gives image
f.write(r.content)

# close method of file object
# save and close the file
f.close()

img = mpimg.imread(f.name)
plt.imshow(img)
plt.show()
