from config import GOOGLE_MAPS_KEY
import requests

gmk = GOOGLE_MAPS_KEY


class Geocoder:
    def __init__(self, query):
        self.query = query

    def geocoder_api_request(self):
        request = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={self.query}&key={gmk}")
        return request.json()

    def get_information_from_the_request(self):
        data_json = self.geocoder_api_request()

        if data_json['status'] == 'OK':
            data_results = []
            data_results.extend(data_json.get('results'))

            long_name = [
                x.get('address_components', "None") for x in data_results
            ]

            place_id = [
                x.get('place_id', "None") for x in data_results
            ]

            geometry = [
                x.get('geometry', "None") for x in data_results
            ]

            location = [
                x.get('location', 'None') for x in geometry
            ]

            lat = location[0]['lat']
            lng = location[0]['lng']
            return {
                'long_name': long_name[0][0]['long_name'],
                'status': data_json['status'],
                'lat': lat,
                'lng': lng,
                'place_id': place_id
                }
        else:
            return {
                'status': data_json['status'],
                }
