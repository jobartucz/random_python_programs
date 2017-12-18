import requests

use_wunderground = False
use_darksky = True

if (use_wunderground) :
    
    print ("***************************")
    print ("*** WEATHER UNDERGROUND ***")
    print ("***************************")
    print ("\n")

    # if you want to see all the data you can get back, just copy and paste this URL into a browser
    weather_request = requests.get('http://api.wunderground.com/api/7067616b88549589/conditions/q/MN/Rochester.json')
    
    # convert the data into a "JSON" object so we can search it easily
    weather_json = weather_request.json()

    # get your location
    location = weather_json['current_observation']['observation_location']['city']

    # get the temperature out of the data
    temp_in_fahrenheit = weather_json['current_observation']['temp_f'] 

    # get the inches of precipitation out of the data
    inches_precipitation = weather_json['current_observation']['precip_today_in']
    
    
    print ("Your location is: " + location)
    print ("current temperature is: " + str(temp_in_fahrenheit)) 
    print ("precipitation today will be: " + str(inches_precipitation))

elif (use_darksky):
    
    print ("****************")
    print ("*** DARK SKY ***")
    print ("****************")
    print ("\n")
   
    weather_request = requests.get('https://api.darksky.net/forecast/97312783323c22d0dfcf90c64bec9502/44.0211,-92.4350')
    weather_json = weather_request.json()

    # print out the full current forecast
    # print (weather_json['currently'])
    
    # get the temperature out of the data
    temp_in_fahrenheit = weather_json['currently']['temperature'] 

    # get the probability of precipitation out of the data
    probability_precipitation = weather_json['currently']['precipProbability']
    
    
    print ("current temperature is: " + str(temp_in_fahrenheit)) 
    print ("probability of precipitation today: " + str(probability_precipitation))



