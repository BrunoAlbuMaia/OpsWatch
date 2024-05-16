import pymssql
from decouple import config

class DbSessionDinamico:

    async def connect(self,conexaoDB) -> pymssql.Cursor:
        self.__server = conexaoDB['serve']
        self.__database = conexaoDB['database']
        self.__user = conexaoDB['usuario']
        self.__passwords = conexaoDB['senha']
        try:
            self.connection = pymssql.connect(server=self.__server,
                            database=self.__database,
                            user=self.__user,
                            password=self.__passwords
                        )
            return self.connection.cursor()
        except Exception as ex:
            return f"Erro ao conectar ao banco de dados: {ex}"

    def close(self) -> None:
        '''Fecha o cursor e desconecta do banco de dados'''
        try:
            self.cursor.close()
            if not self.connection.closed:
                self.connection.close()
        except Exception as ex:
            return f"Erro ao fechar conexão: {ex}"

        