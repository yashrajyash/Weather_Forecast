from fetch import fetch_data
from datetime import datetime
from sequel import *


def print_data(api_data):

    if api_data['cod'] == '404':
        print(api_data['message'].capitalize())
    else:
        weather_desc = str(api_data['weather'][0]['description'])
        temp_city = str(float(api_data['main']['temp']) - 273.15)[:4] + '`C'
        humid = str(api_data['main']['humidity']) + '%'
        wind_spd = str(api_data['wind']['speed']) + ' kmph'
        city_name = str(api_data['name'])
        city_id = str(api_data['id'])
        date_time = '[' + str(datetime.now().strftime("%d-%b-%Y | %I:%M:%S %p")) + ']'

        print('\n\n------------------------------------------------------------------------------------')
        print('Weather stats for -> {} | City-id : {} | {}'.format(city_name, city_id, date_time))
        print('------------------------------------------------------------------------------------\n')

        print('Current Temperature   :  {}'.format(temp_city))
        print('Weather Discription   :  {}'.format(weather_desc))
        print('Wind Speed            :  {}'.format(wind_spd))
        print('Humidity              :  {}\n'.format(humid))

        insert_into_table(city_id, city_name, date_time, temp_city, weather_desc, wind_spd, humid)

        yes_no = input('Do you want to check your database (Y/N) ? : ')[0].capitalize()

        if yes_no == 'Y':
            show_database()


def main():

    city = input('\nEnter the name of the city : ').strip()
    raw_data = fetch_data(city)
    print_data(raw_data)

if __name__ == '__main__':

    i = 1
    while True:
        if i == 1:
            create_table()
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