import pandas as pd
import folium
import webbrowser

if __name__ == '__main__':

    # Load the shape of the zone (US states)
    # Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
    # You have to download this file and set the directory where you saved it
    state_geo = './static/resource/TL_SCCO_SIG_WGS84.json'

    # Load the unemployment value of each state
    # Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
    state_unemployment = './output/LOC_CODE_WEATHER_EUC_KR.csv'
    state_data = pd.read_csv(state_unemployment, encoding='euc-kr')
    state_data['Weather'] = state_data['Weather'].astype(float)
    state_data['Weather'] = state_data['Weather'].apply(lambda x: x if x > 20 else None)
    state_data['Weather'] = state_data['Weather'].fillna(state_data['Weather'].min())


    # Initialize the map:
    m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)

    m.choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=state_data,
        columns=['Code', 'Weather'],
        key_on='feature.properties.SIG_CD',
        fill_color='Reds',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='Temperature (°C)'
    )

    folium.LayerControl().add_to(m)

    # Save to html
    m.save('folium_kr.html')
    webbrowser.open_new("folium_kr.html")