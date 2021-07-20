import json
import requests
# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
#parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
#response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
response = requests.get("https://www.reddit.com/r/learnprogramming/.json")
status_code=response.status_code
print(status_code)


# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
#response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
#print(response.content)
