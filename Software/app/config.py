#Configuracaiones para flask
import os
import urllib

secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


DEBUG = True

#PWD = os.path.abspath(os.curdir)	
#SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)

#SQLALCHEMY_DATABASE_URI = "Persist Security Info=False;User ID=transaccionales;Password=340$Uuxwp7Mcxo7Khy;Initial Catalog=Parqueadero;Server=MySqlServer"

string_connection = "DRIVER={SQL Server};Database=Parqueadero;SERVER=.;UID=transaccionales;PWD=340$Uuxwp7Mcxo7Khy"
string_connection = urllib.parse.quote_plus(string_connection)
string_connection = "mssql+pyodbc:///?odbc_connect=%s" % string_connection

SQLALCHEMY_DATABASE_URI = string_connection

SQLALCHEMY_TRACK_MODIFICATIONS = False