# import pymssql
# from decouple import config

# class DbSession:
#     def __init__(self):
#         self.__connection_string = config('FB.Core.dbIntegrador')

#     def connect(self,as_dict: bool | None = None) -> pymssql.Cursor:
#         try:
#             connection_params = {}
#             for param in self.__connection_string.split(";"):
#                 key, value = param.split("=")
#                 connection_params[key.strip()] = value.strip()

#             self.connection = pymssql.connect(**connection_params)
            
#             return self.connection.cursor(as_dict=as_dict)
#         except Exception as ex:
#             return f"Erro ao conectar ao banco de dados: {ex}"

#     def close(self) -> None:
#         '''Fecha o cursor e desconecta do banco de dados'''
#         try:
#             self.cursor.close()
#             if not self.connection.closed:
#                 self.connection.close()
#         except Exception as ex:
#             return f"Erro ao fechar conexão: {ex}"

import pyodbc
from decouple import config

class DbSession:
    def __init__(self):
        self.__connection_string = config('OpsWatch.Core.dbIntegrador')

    def connect(self, as_dict: bool | None = None) -> pyodbc.Cursor:
        try:
            self.connection = pyodbc.connect(self.__connection_string,)
            return self.connection.cursor()
        except Exception as ex:
            return f"Erro ao conectar ao banco de dados: {ex}"

    def close(self) -> None:
        '''Fecha o cursor e desconecta do banco de dados'''
        try:
            if hasattr(self, 'cursor'):
                self.cursor.close()
            if hasattr(self, 'connection') and not self.connection.closed:
                self.connection.close()
        except Exception as ex:
            return f"Erro ao fechar conexão: {ex}"
