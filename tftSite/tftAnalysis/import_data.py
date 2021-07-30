from tft_api import *
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

api_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-5e863ef6-d38a-4f51-9fd3-8d7481743bd4"
}


def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')


def insert_player(tft_player, username, puuid, league):
    query = "INSERT INTO player(tft_player,username, puuid, league) " \
            "VALUES(%s,%s)"
    args = (tft_player, username, puuid, league)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_player(tft_player, username, puuid, league):
    query = "INSERT INTO player(tft_player,username, puuid, league) " \
            "VALUES(%s,%s)"
    args = (tft_player, username, puuid, league)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def main():
    insert_player()

if __name__ == '__main__':
    main()
