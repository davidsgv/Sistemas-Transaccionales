from app import app
#from app.controllers.Ciudad import ciudad
from app.controllers.Persona import persona


app.register_blueprint(persona)