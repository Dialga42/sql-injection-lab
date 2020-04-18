import os
import mysql.connector

class MysqlConnector():

    connector = None

    def __init__(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sql_injection.settings')
        print("begin database connection")
        conn = mysql.connector.connect(
            host="0.0.0.0",
            user="root",
            passwd="123456",
            database="weblab"
        )
        self.conn = conn
        print("user %s login" % conn.user)

    @staticmethod
    def getConn():
        if not MysqlConnector.connector:
            MysqlConnector.connector = MysqlConnector()
        return MysqlConnector.connector.conn