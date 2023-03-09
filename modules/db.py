import pymysql.cursors


class DB:
    def __init__(
        self, DBserver: str, DBUser: str, DBPass: str, DBName: str, DBPort: int
    ):
        self._DBServer = DBserver
        self._DBUser = DBUser
        self._DBPass = DBPass
        self._DBName = DBName
        self._DBPort = DBPort

    def create_db_connection(self) -> pymysql.connections.Connection:
        try:
            return pymysql.connect(
                host=self._DBServer,
                user=self._DBUser,
                password=self._DBPass,
                database=self._DBName,
                port=self._DBPort,
                cursorclass=pymysql.cursors.DictCursor,
            )
        except pymysql.err.OperationalError as e:
            print(e)
            exit()

    def select(self, connection: pymysql.connections.Connection, query: str) -> list:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

            return result
