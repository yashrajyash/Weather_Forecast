import sqlite3 as sql
import time


def show_loading(count):

    print('\nLoading.....')
    for i in range(count):
        print('$', end='')
        time.sleep(0.05)
    print('_100%')

def create_table():

    conn = sql.connect('weather.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS weather_details \
                (city_id TEXT, \
                city_name TEXT, \
                date_time TEXT, \
                temp_city TEXT, \
                weather_desc TEXT, \
                wind_spd TEXT, \
                humid TEXT, \
                PRIMARY KEY (city_id, date_time, temp_city) \
                    );")

    conn.close()

    show_loading(20)
    print('\nDatabase Connected Successfully!')


def insert_into_table(cityId, cityName, dateTime, tempCity, weatherDesc, windSpd, humid):
    
    conn = sql.connect('weather.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO weather_details \
                (city_id, city_name, date_time, temp_city, weather_desc, wind_spd, humid) \
                VALUES (?,?,?,?,?,?,?);",(cityId, cityName, dateTime, tempCity, weatherDesc, windSpd, humid))

    conn.commit()

    conn.close()

    show_loading(20)
    print('\nDatabase Updated Successfully!\n')


def show_database():
    
    conn = sql.connect('weather.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM weather_details")
    rows = cur.fetchall()

    print('\n------------------------------  <UPDATED_DATABASE>  --------------------------------\n')

    for row in rows:
        print(row)

    conn.close()


def main():
    
    create_table()
    insert_into_table(cityId = '', cityName = '', dateTime = '', tempCity = '', weatherDesc = '', windSpd = '', humid = '')
    show_database()
    show_loading(2)

if __name__ == '__main__':

    main()