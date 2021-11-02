from app import app

from app.controllers.Parqueadero import parqueadero
from app.controllers.Bahia import bahia

from app.controllers.TipoVehiculo import tipo
from app.controllers.Tarifa import tarifa

from app.controllers.Persona import persona
from app.controllers.Sesion import sesion

app.register_blueprint(parqueadero)
app.register_blueprint(bahia)

app.register_blueprint(tipo)
app.register_blueprint(tarifa)

app.register_blueprint(persona)
app.register_blueprint(sesion)
