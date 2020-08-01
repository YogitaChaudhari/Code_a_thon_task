from rest_framework.response import Response
from rest_framework.views import APIView
import json
from math import sin, cos, sqrt, radians, asin

class Hotels(APIView):
    def get(self, request, latitude, longitude):
        lat1 = radians(float(latitude))
        long1 = radians(float(longitude))

        f = open('data.json', 'r')
        data = json.loads(f.read())

        d = {'Results':[]}
        for i in data['0-4']['HotelSearchResult']["HotelResults"]:
            lat2 = radians(i['Latitude'])
            long2 = radians(i['Longitude'])

            dlon = long2-long1
            dlat = lat2-lat1

            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            
            c = 2 * asin(sqrt(a))  
            
            r = 6371

            distance = r*c

            if distance < 100.0:
                d['Results'].append(i['HotelName'])
                

        return Response(d)

