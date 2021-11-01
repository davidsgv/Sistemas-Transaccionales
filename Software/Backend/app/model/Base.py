#from flask_mysqldb import MySQL as mysql
from app import db

def selectDB(sql_code):
    result = db.engine.execute(sql_code)
    return result

def insertBD(sql_code):
    db.session.execute(sql_code)
    db.session.commit()