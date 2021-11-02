from app import app

from app.controllers.Parqueadero import parqueadero
from app.controllers.Bahia import bahia
from app.controllers.Persona import persona
from app.controllers.Sesion import sesion

app.register_blueprint(parqueadero)
app.register_blueprint(bahia)

app.register_blueprint(persona)
app.register_blueprint(sesion)
