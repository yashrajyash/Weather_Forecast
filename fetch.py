from requests import get
import json


def fetch_data(city_name):
    
    api_key = 'cbb6b8a7a93022bfe48120a12e239d34'
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    content = get(api_url)
    return content.json()

def main():

    city = input('Enter city name : ').strip().capitalize()
    fetch_data(city)

if __name__ == '__main__':

    main()