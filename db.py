import mysql.connector
from mysql.connector import Error
import datetime
def dataInsert(nomecadastro,username,tiktokid):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='musictiktok',
                                            user='root',
                                            port=3306,
                                            password='')
        sql_select_Query = 'INSERT INTO tiktokusers (nomecadastro,username,tiktokid) VALUES ("{0}", "{1}", {2});'.format(nomecadastro,username,int(tiktokid))
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        connection.commit()
        
    except Error as e:
        print("Error reading data from MySQL table", e)
        connection.rollback()
    finally:
        if (connection.is_connected()):
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
