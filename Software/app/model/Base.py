#from flask_mysqldb import MySQL as mysql
from app import db

def select_db(sql_code):
    result = db.engine.execute(sql_code)
    return result