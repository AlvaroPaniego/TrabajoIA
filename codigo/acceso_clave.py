from dotenv import load_dotenv
import os

RUTA_CLAVE: str = '../claves/api_key.env'

def cargar_clave(clave_env: str, ruta_clave_env: str = RUTA_CLAVE) -> str:
    load_dotenv(dotenv_path=ruta_clave_env)
    clave = os.getenv(clave_env)
    if clave is None:
        raise ValueError(f'La clave {clave_env} no se encuentra en: {ruta_clave_env}')
    return clave

"""
Dentro del main.py hay que hacer:

from acceso_clave import cargar_clave

api_key = cargar_clave('API_KEY')
print (f'La clave es: {api_key}')

"""