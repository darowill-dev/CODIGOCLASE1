from decouple import config
from personabase import PersonaBase

if config("LLAVE_REINO_UNIVERSO", default=""):
    print("La llave del reino universo está configurada.")
    new_persona=PersonaBase()
    new_persona.presentarse()
else:
    print("La llave del reino unverso no está activada. Por favor, configúrela en el archivo .env.")