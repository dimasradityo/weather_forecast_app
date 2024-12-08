import streamlit as st
import plotly.express as px
from backend import get_weather_data

# User input section
st.title('Weather Forecast for the Next Days')
place = st.text_input('City: ')
days = st.slider('Forecast Days:', min_value=1, max_value=5, help='Select the number of days to forecast.')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

# Displaying the temperature plot
if place:
    try:
        filtered_data = get_weather_data(place, days)

        # Displaying the temperature plot
        if option == 'Temperature':
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {
                'Clear': 'images/clear.png',
                'Clouds': 'images/cloud.png',
                'Rain': 'images/rain.png',
                'Snow': 'images/snow.png'
            }
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.error("Can't find city. Please try another keyword.")