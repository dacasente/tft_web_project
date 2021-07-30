from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
#need to edit all of these

def delete_unit(unit_id):
    query = "DELETE FROM unit WHERE unit_id = %s " 
    args = (unit_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def delete_player(player_id):
    query = "DELETE FROM player WHERE player_id = %s"
    args = (player_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def delete_trait(trait_id):
    query = " DELETE FROM trait WHERE trait_id = %s"
    args = (trait_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def delete_unitstraits(unit_id, trait_id):
    query = "DELETE FROM unitstraits WHERE unit_id = %s AND trait_id = %s"
    args = (unit_id, trait_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)


        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def delete_items(item_id):
    query = "DELETE FROM items WHERE item_id = %s"
    args = (item_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def delete_game(game_id):
    query = "DELETE FROM game WHERE game_id = %s"
    args = (game_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)


        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def delete_gameplayercomp(comp_id):
    query = "DELETE FROM gameplayercomp WHERE comp_id = %s"
    args = (comp_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)



        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def delete_comptraits(comp_id, trait_id):
    query = "DELETE FROM comptraits WHERE comp_id = %s AND trait_id = %s"
    args = (comp_id, trait_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        
        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def delete_compunits(comp_id, unit_id):
    query = "DELETE FROM compunits WHERE comp_id = %s AND unit_id = %s"
    args = (comp_id, unit_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def delete_unititems(comp_id, unit_id, item_id):
    query = "DELETE FROM unititems WHERE comp_id = %s AND unit_id = %s AND item_id = %s"
    args = (comp_id, unit_id, item_id,)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def main():
    delete_player(1)

if __name__ == '__main__':
    main()