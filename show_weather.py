from fetch import fetch_data
from datetime import datetime
from sequel import *
import tkinter as tk


def get_weather(root):

    create_table()

    city = textField.get()
    api_data = fetch_data(city)

    if api_data['cod'] == '404':

        print('\n```````````````````````````````````````')
        print(city + ' ' + api_data['message'])
        print('```````````````````````````````````````')

    else:

        weather_desc = str(api_data['weather'][0]['description'])
        temp_city = str(float(api_data['main']['temp']) - 273.15)[:4] + '°C'
        humid = str(api_data['main']['humidity']) + '%'
        wind_spd = str(api_data['wind']['speed']) + ' kmph'
        city_name = str(api_data['name'])
        city_id = str(api_data['id'])
        date_time = '[' + str(datetime.now().strftime("%d-%b-%Y | %I:%M %p")) + ']'
        visibility = str(float(api_data['visibility'])/1000)[:4] + ' km'

        insert_into_table(city_id, city_name, date_time, temp_city, weather_desc, wind_spd, humid, visibility)

        print('\n\n------------------------------------------------------------------------------------')
        print('Weather stats for -> {} | City-id : {} | {}'.format(city_name, city_id, date_time))
        print('------------------------------------------------------------------------------------\n')

        print('Current Temperature   :  {}'.format(temp_city))
        print('Weather Discription   :  {}'.format(weather_desc))
        print('Wind Speed            :  {}'.format(wind_spd))
        print('Humidity              :  {}'.format(humid))
        print('Visibility            :  {}\n'.format(visibility))

        final_info = weather_desc + '\n' + temp_city
        final_data = '\nCity name: ' + city_name + '\nCity id: ' + city_id + '\n' + date_time + '\nHumidity: ' + humid + '\nWind speed: ' + wind_spd + '\nVisibility: ' + visibility

        label1.config(text = final_info)
        label2.config(text = final_data)


# GUI
root = tk.Tk()

root.geometry('600x450')

root.title('Weather Forecast App')

f = ("poppins", 15, "bold" )
t = ("poppins", 35, "bold")

textField = tk.Entry(root, width = 15, font = t, bg = 'grey')
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', get_weather)

label1 = tk.Label(root, font=t, bg = 'red2', fg = 'alice blue')
label1.pack()
label2 = tk.Label(root, font=f, bg = 'cyan4', fg = 'snow2')
label2.pack()

root.mainloop()