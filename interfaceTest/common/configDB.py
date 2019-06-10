import pymysql

from interfaceTest import readConfig
from interfaceTest.common.Log import MyLog as Log

locakReadConfig = readConfig.ReadConfig()


class MyDB:
    global host, username, password, port, database, config
    host = locakReadConfig.get_db("host")
    username = locakReadConfig.get_db("username")
    password = locakReadConfig.get_db("password")
    port = locakReadConfig.get_db("port")
    database = locakReadConfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'password': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_loger()
        self.db = None
        self.cursor = None

    def connectDb(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("connect DB successfully")

        except ConnectionError as ex:
            self.logger.error(str(ex))

    def excuteSQL(self, sql, params):
        self.connectDb()
        # excuting sql
        self.cursor.execyte(sql, params)
        # excuting  by committing to DB
        self.db.commit()
        return self.cursor;

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed")
