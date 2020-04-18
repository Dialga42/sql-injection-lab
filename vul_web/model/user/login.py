import mysql.connector
from database import MysqlConnector as connector

def login(user, password):
    conn = connector.getConn()

    cursor = conn.cursor()
    login_query = "SELECT * FROM webuser WHERE (name = '" + user + "') and (password = '" + password + "');"
    print(login_query)
    cursor.execute(login_query)
    u, p = None, None
    for (_, u, p) in cursor:
        print("user=%s, password=%s"%(u, p))
        break

    return (u, p)