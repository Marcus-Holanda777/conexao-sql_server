from sqlalchemy import create_engine
from urllib.parse import quote_plus


class Conexao:
    config = ('Driver={};'
              'Server={};'
              'Database={};'
              'Trusted_Connection=Yes;')

    def __init__(self, server: str = 'cosmos', database: str = 'cosmos_v14b') -> None:
        self.__driver = '{ODBC Driver 17 for Sql Server}'
        self.server = server
        self.database = database
        self.stringconn = self.config.format(
            self.__driver, self.server, self.database)

        self.url = quote_plus(self.stringconn)

    def conectar(self):
        return create_engine('mssql+pyodbc:///?odbc_connect=%s' % self.url,
                             fast_executemany=True)
