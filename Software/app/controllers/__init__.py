from app import app
#from app.controllers.Ciudad import ciudad
from app.controllers.Persona import persona
from app.controllers.Sesion import sesion


app.register_blueprint(persona)
app.register_blueprint(sesion)