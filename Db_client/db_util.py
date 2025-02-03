import mysql.connector as sql
import time
from .db_props import DBPropertyUtil

        
class DBConnUtil():
    @staticmethod
    def makeConnection():
        parameters = DBPropertyUtil.getParameter()
        # print(parameters["host"],parameters["database"],parameters["user"],parameters["password"])
        conn = sql.connect(host=parameters["host"], database=parameters["database"], user=parameters["user"],
                           password=parameters["password"])
        # print(parameters)
        if conn.is_connected():
            time.sleep(0.5)
            print("Connections successful")
            return conn

        else:
            print("Unable to connect")
            
# DBConnUtil.makeConnection()
