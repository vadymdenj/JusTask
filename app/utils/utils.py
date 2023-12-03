from email import header
import json
import xml.etree.ElementTree as ET
import requests
from app.utils.auth_utils import get_token
# from auth_utils import get_token
BASE_API_URL = 'https://api.iq.inrix.com'
FIND_ROUTE_URL_END_POINT = '/findRoute'
ROUTE_TRAVEL_TIMES_URL_END_POINT = '/routeTravelTimes'
RESPONSE_XML_FILE_NAME = 'RESPONSE.xml'





# def getTravelTime(token, fromAddy, toAddy, depatureTime):
def getTravelTime(token, fromPoint, toPoint, departureTime):
    # Make the request to the INRIX token endpoint
    try:
        findRouteParams = {
        'wp_1': fromPoint,
        'wp_2': toPoint,
        }
        headers = {
            'Authorization': f'Bearer {token}',
            'content-type': 'application/json',
        }

        findRouteResponse = requests.get(BASE_API_URL + FIND_ROUTE_URL_END_POINT, params=findRouteParams, headers=headers)
        findRouteResponse.raise_for_status() 

        with open(RESPONSE_XML_FILE_NAME, 'wb') as f: 
            f.write(findRouteResponse.content) 

        root = ET.parse(RESPONSE_XML_FILE_NAME).getroot()
        # print(root.find('./Trip').attrib['id'])
        routId = root.find('./Trip').attrib['id']

        findRouteTravelTimeParams = {
        'routeId': routId,
        'travelTimeCount': 1,
        'travelTimeInterval': 1,
        'departureTime' : departureTime
        }
        findRouteTravelTimeResponse = requests.get(BASE_API_URL + ROUTE_TRAVEL_TIMES_URL_END_POINT, params=findRouteTravelTimeParams, headers=headers)
        
        with open(RESPONSE_XML_FILE_NAME, 'wb') as f: 
            f.write(findRouteTravelTimeResponse.content) 

        # print(findRouteTravelTimeResponse)
        root = ET.parse(RESPONSE_XML_FILE_NAME).getroot()    
        travelTime = root.find('./Trip/Route/TravelTimes/TravelTime').attrib['travelTimeMinutes']
        return travelTime

    except requests.exceptions.RequestException as e:
        return f'Request failed with error: {e}', None
    except (KeyError, ValueError) as e:
        return f'Error parsing JSON: {e}', None



# print("hi")
# print(getTravelTime(token))
# print(response.text)
# data = response.xml()
# token = get_token()

# print(getTravelTime(token, '37.770637, -122.412435', '37.781613, -122.494546', '2023-12-09T10:42:41Z'))