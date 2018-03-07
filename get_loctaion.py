import googlemaps
def geocode_address(loc):
    gmaps = googlemaps.Client(key='AIzaSyCiIpypih0EpKN7IMg4skrMI2mKJQsAWKk')
    geocode_result = gmaps.geocode(loc)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    #test - print results
    return lat,lon

print geocode_address('A ST & KETTNER BLVD')