from fetch import fetch_data
from datetime import datetime

def print_data(api_data):

    if api_data['cod'] == '404':
        print(api_data['message'].capitalize())
    else:
        weather_desc = api_data['weather'][0]['description']
        temp_city = float(api_data['main']['temp']) - 273.15
        humid = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        city_name = api_data['name']
        city_id = api_data['id']
        date_time = datetime.now().strftime("%d-%b-%Y | %I:%M:%S %p")

        print('\n------------------------------------------------------------------------------------')
        print('Weather stats for -> {} | City-id : {} | [{}]'.format(city_name, city_id, date_time))
        print('------------------------------------------------------------------------------------\n')

        print('Current Temperature   :  {:.2f} deg Celcius'.format(temp_city))
        print('Weather Discription   :  {}'.format(weather_desc))
        print('Wind Speed            :  {} kmph'.format(wind_spd))
        print('Humidity              :  {} %\n'.format(humid))

def main():

    city = input('\nEnter the name of the city : ').strip()
    raw_data = fetch_data(city)
    print_data(raw_data)

if __name__ == '__main__':

    i = 1
    while True:
        if i == 1:
            main()
            i = 0
        print('\n------------------------------------------------------------------------------------')
        print('Search another city?')
        op = input("Enter 'Y' for yes and 'N' for exit : ").strip()[0]
        print('------------------------------------------------------------------------------------\n')
        if(op.upper() == 'Y'):
            main()
        else:
            exit()