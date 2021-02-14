import sqlite3 as sql


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

    print('\nDatabase Connected Successfully!')


def insert_into_table(cityId, cityName, dateTime, tempCity, weatherDesc, windSpd, humid):
    
    conn = sql.connect('weather.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO weather_details \
                (city_id, city_name, date_time, temp_city, weather_desc, wind_spd, humid) \
                VALUES (?,?,?,?,?,?,?);",(cityId, cityName, dateTime, tempCity, weatherDesc, windSpd, humid))

    conn.commit()

    conn.close()

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

if __name__ == '__main__':

    main()