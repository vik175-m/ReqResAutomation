
import requests
import configparser


'''
Load the config parser file for api and base url
'''

config = configparser.ConfigParser()
config.read('config/config.ini')

class APIRequestMethods:

    @staticmethod
    def get(endpoint):
        url=config['API']['base_url'] + endpoint
        response = requests.get(url)

        print('GET :', url)
        print('Status COde :', response.status_code)
        print('Response Data :', response.json())

        return response

    @staticmethod
    def post(endpoint, data):
        url=config['API']['base_url'] + endpoint
        response = requests.post(url,json=data)

        print('POST :', url)
        print('Status COde :', response.status_code)
        print('Response Data :', response.json())
        assert response.status_code == 201
        assert response.json() is not None

        return response

    @staticmethod
    def put(endpoint, data):
        url = config['API']['base_url'] + endpoint
        response = requests.put(url, json=data)

        print('PUT :', url)
        print('Status COde :', response.status_code)
        print('Response Data :', response.json())
        assert response.status_code == 200
        assert response.json() is not None

        return response

    @staticmethod
    def patch(endpoint, data):
        url = config['API']['base_url'] + endpoint
        response = requests.post(url, json=data)

        print('PATCH :', url)
        print('Status COde :', response.status_code)
        print('Response Data :', response.json())
        assert response.status_code == 200
        assert response.json() is not None
        return response

    @staticmethod
    def delete(endpoint):
        url = config['API']['base_url'] + endpoint
        response = requests.post(url)

        print('DELETE :', url)
        print('Status COde :', response.status_code)
        print('Response Data :', response.json())
        assert response.status_code == 204

        return response




