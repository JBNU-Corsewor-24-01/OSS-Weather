import requests
import json


class WeatherService:
    service_key = ''
    base_url = ''

    def __init__(
            self,
            base_date: str = '20240528',
            base_time: str = '2300',
            fcst_date: str = '20240529',
            fcst_time: str = '0900'
    ):
        self.base_date = base_date
        self.base_time = base_time
        self.fcst_date = fcst_date
        self.fcst_time = fcst_time

    def get_weather(
            self,
            nx: int = 63,
            ny: int = 88,
    ) -> str:
        params = {
            'serviceKey': self.service_key,
            'numOfRows': 1000,
            'pageNo': 1,
            'dataType': 'JSON',
            'base_date': self.base_date,
            'base_time': self.base_time,
            'nx': nx,
            'ny': ny,
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = json.loads(response.text)['response']['body']['items']['item']

            selected_weather = [
                item for item in data
                if item['category'] == 'TMX'
                   and item['fcstDate'] == self.fcst_date
                   # and item['fcstTime'] == self.fcst_time
            ]

            if not selected_weather:
                raise ValueError('No data')

            return selected_weather[0]['fcstValue']
        else:
            raise ValueError(f"Failed to get data. status code: {response.status_code}")


# Example usage:
if __name__ == '__main__':
    weather_service = WeatherService()

    try:
        sky_value = weather_service.get_weather()
        print(f"Forecasted SKY value: {sky_value}")
    except ValueError as e:
        print(e)
