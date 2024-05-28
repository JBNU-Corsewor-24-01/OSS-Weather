import pandas as pd

from util.Weather import WeatherService
from util.ParseGeoInfo import LambertConverter
from tqdm import tqdm

if __name__ == '__main__':

    df = pd.read_csv('./static/resource/LOC_CODE_EUC_KR.csv', encoding='euc-kr')

    # make nx and ny columns
    df['nx'] = 0
    df['ny'] = 0
    df['Weather'] = 0

    # fill nx and ny columns
    for idx, row in tqdm(df.iterrows()):
        try:
            nx, ny = LambertConverter().convert(row['Longitude'], row['Latitude'])
            df.at[idx, 'nx'] = nx
            df.at[idx, 'ny'] = ny

            # get weather data
            weather = WeatherService().get_weather(nx, ny)
            df.at[idx, 'Weather'] = weather
        except Exception as e:
            print(f"Failed to get weather data. {e}")
            continue

    print(df)
    df.to_csv('./output/LOC_CODE_WEATHER_EUC_KR.csv', encoding='euc-kr', index=False)
    df.to_csv('./output/LOC_CODE_WEATHER_UTF8.csv', encoding='utf-8', index=False)
