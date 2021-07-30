from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_unit(unit_name, cost):
    query = "INSERT INTO unit(unit_name, cost)) " \
            "VALUES(%s,%s)"
    args = (unit_name, cost)

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

def insert_player(tft_player, username, puuid, league, division):
    query = "INSERT INTO player(tft_player, username, puuid, league, division) VALUES(%s,%s,%s,%s,%s)"
    args = (tft_player, username, puuid, league, division)

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


def insert_trait(trait_name):
    query = "INSERT INTO trait(trait_name) " \
            "VALUES(%s)"
    args = (trait_name)

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

def insert_unitstraits(unit_id, trait_id):
    query = "INSERT INTO unitstraits(unit_id, trait_id) " \
            "VALUES(%s)"
    args = (unit_id, trait_id)

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

def insert_items(item_name):
    query = "INSERT INTO items(item_name) " \
            "VALUES(%s)"
    args = (item_name)

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

def insert_game(tft_match_id):
    query = "INSERT INTO game(tft_match_id) " \
            "VALUES(%s)"
    args = (tft_match_id)

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


def insert_gameplayercomp(player_id, game_id, place, player_level, last_round):
    query = "INSERT INTO gameplayercomp(player_id, game_id, place, player_level, last_round) " \
            "VALUES(%s,%s,%s,%s,%s)"
    args = (player_id, game_id, place, player_level, last_round)

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


def insert_comptraits(comp_id, trait_id, tier, num_units):
    query = "INSERT INTO comptraits(comp_id, trait_id, tier, num_units) " \
            "VALUES(%s,%s,%s,%s)"
    args = (comp_id, trait_id, tier, num_units)

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

def insert_compunits(comp_id, unit_id, star_level):
    query = "INSERT INTO compunits(comp_id, unit_id, star_level) " \
            "VALUES(%s,%s,%s)"
    args = (comp_id, unit_id, star_level)

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

def insert_unititems(comp_id, unit_id, item_id):
    query = "INSERT INTO unititems(comp_id, unit_id, item_id) " \
            "VALUES(%s,%s,%s)"
    args = (comp_id, unit_id, item_id)

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
    insert_player('WkmkJ7Dl8IZnZQBTE8gDa5AnqmafjIg6il4FadYE8ZlE7AY','bigdac', 'DOlC4965MCdnIwgaDPV9tcqbXUrKe8GjFo8eqUfjxN1dQG_MULsWgjfatXM4-XKJJX42x3kQLkFFhg','Diamond', 4)

if __name__ == '__main__':
    main()