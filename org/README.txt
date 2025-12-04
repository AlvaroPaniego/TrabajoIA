
ÍNDICE
---------------------------------------------------------------------

1. DESCRIPCIÓN

	1.a. Proyecto
	1.b. Descripción
	
2. REQUERIMIENTOS
3. ORGANIZACIÓN DEL ÁRBOL DE DIRECTORIOS DEL PROYECTO
4. MÓDULOS
5. PAQUETES A INSTALAR
6. IMPORTACIONES DENTRO DE CÓDIGO
7. ¿CÓMO SE CARGA UNA CLAVE DESDE UNA CAPETA CON RUTA PERSONALIZADA?
8. ENTORNO
9. NOTA
---------------------------------------------------------------------


1. DESCRIPCIÓN
---------------
1.a Proyecto: Asistomail (he puesto este nombre por poner uno pero si no te gusta lo cambiamos)

1.b.Descripción: Interfaz web que facilita al usuario la redacción de correos electrónicos filtrados por nivel de formalidad (tono). 
			 	 La empresa a la que va destinada es de reparación de equipos informáticos. 
			 	 La comunicación de correos será principalmente hacia 
			     diferentes departamentos, entre trabajadores y clientes, y entre trabajadores y empresas de suministro. 
			 
			 Los niveles del formalidad serán 3: 	

		- Nivel 1: El nivel más formal que irá dirigido principalmente p.ej. a clientes y jefes de departamento, de planta, etc.
		- Nivel 2: El nivel neutro que irá dirigido a p.ej. empresas de suministro de componentes, para pedidos, etc..
		- Nivel 3: El nivel informal que irá dirigido p.ej. a compañeros de departamento para comunicar progresos y dudas.
		
		
2. REQUERIMIENTOS
-----------------

	- Es necesario que el programa pueda elegir entre modelos locales y API.
	- Las API_KEYS se guardaran en un archivo .env en una carpeta claves
	  que se leerá desde código a través de la librería python-dotenv.
	  
	- La interfaz de usuario se realiza con streamlit.
	
	- Necesitamos correos de ejemplos para los distintos niveles para pasarselos al modelo 
	  y que pueda dar una salida acorde a la formalidad.
	  
	- La salida se hará en un documento .txt o bien directamente en pantalla o ambas ¿...?
	
	- El código irá separado en diferentes módulos, para separar el flujo principal de las funciones o demás ¿...?
	
	(...)
	
	
	SOBRE EL MODELO LOCAL:
	
		- El modelo local será el encargado de redactar el correo.
		- El modelo local recibe un pdf con un email en un tono (formal, neutro, informal)
		- El modelo local tomará pdf y redactará una salida con el tono especificado por el usuario

3. ORGANIZACIÓN DEL ÁRBOL DE DIRECTORIOS DEL PROYECTO (o cómo tu veas, ya me dices)
-----------------------------------------------------------------------------------

carpetaProyecto/
|--codigo/
|	|- main.py
| 	|- acceso_claves.py
|	|- funciones.py
|	|- (...)
|--claves/
|	|-apy_key.env
|--org/
|	|-README.txt
|--img/
|	|-portada.jpg
|	|-(...)
|--.gitignore/
|--(...)
	
	
4. MODULOS
----------

	- modelo_local.py: para funciones y demás relacionado con el modelo local
	- modelo_api.py. para funciones relacionadas con modelos vía API
	- acceso_clave.py
	- (...)

5. FUNCIONES
------------

-

6. PAQUETES A INSTALAR
----------------------

	1. Primero establecer la versión de Python globalmente con: pyenv global 3.12.8
	2. Dentro del EV activado instalar los paquetes: 

		a. streamlit
   			pip install streamlit
   
		b. ollama
   			pip install ollama

		c. langchain-ollama
   			pip install langchain-ollama

		d. langchain-core
   			pip install langchain-core

		e. python-dotenv
   			pip install python-dotenv
   
		f. Groq
   			pip install groq
			
		g. python-dotenv: Para usar API_KEY en un archivo .enc
			 pip install python-dotenv
			 
		h. Para cargar ficheros de texto (pdf)
			pip instal PyMuPDF 
			nótese: el import luego es: import fitz (Esto funciona porque PyMuPDF expone el módulo como 'fitz')
		

Nota:
Aunque langchain-ollama depende de langchain-core, es mejor instalar ambos explícitamente 
para evitar errores de importación.


7. IMPORTACIONES DENTRO DEL CÓDIGO
----------------------------------
Código:

- Librerías de uso general:

import streamlit as st 
import fitz
 
#PIL está en el core de python no es necesario hacer pip install...
from PIL import Image

- Librerías para usar python-dotenv y cargar la API_KEY desde archivo .env

import os
from dotenv import load_dotenv

- Para modelo local:

import ollama
from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

- Para modelo desde API

from groq import Groq
		


8.¿CÓMO SE CARGAN LAS CLAVES DESDE UN ARCHIVO EN UNA CARPETA CON RUTA PERSONALIZADA?
------------------------------------------------------------------------------------

	- Previamente:

 			Instalar python-dotenv con el Entorno Virtual activado.

   			pip install python-dotenv
   

	- Suponemos que el fichero .env con la API_KEY esta en carpeta claves y el main.py otra carpeta codigo:

			
		mi_proyecto/
		|--claves/
		|  	|- apy_key.env
		|--codigo/
			|- main.py
		
	Si se hace directamente en el main.py:
	--------------------------------------
	
    - Contenido del archivo .env en la carpeta claves.
	
		API_KEY=tu_clave_secreta
	
	- Código para acceder al directorio de la clave y cargar la clave
	
		from dotenv import load_dotenv
		import os

		# Construir ruta relativa al archivo .env
			env_path = os.path.join(os.path.dirname(__file__), "..", "claves", ".env")
			load_dotenv(dotenv_path=env_path)

		# Acceder a la clave
		api_key = os.getenv("API_KEY")

		# Verificación opcional (no imprimir en producción)
		print(api_key)
	

	Si se hace desde un módulo.py:
	------------------------------
	
	- Módulo: acceso_clave.py
	
		- Código:
		
		from dotenv import load_dotenv
		import os

		def cargar_clave(clave_env: str, ruta_clave: str = "../claves/api_key.env") -> str:
		load_dotenv(dotenv_path=ruta_clave)
    	clave = os.getenv(clave_env)
    	if clave is None:
        	raise ValueError(f"La clave '{clave_env}' no se encuentra en {ruta_clave}")
    	return clave
		
		
		- Uso desde el main:
		
		from acceso_clave import cargar_clave
		api_key = cargar_clave("API_KEY")
	
		- # Verificación opcional (no imprimir en producción)
		  print(api_key)
		  
	- Si se pone la ruta de la clave en una constante:
	
		from dotenv import load_dotenv
		import os

		RUTA_CLAVE: str = '../claves/api_key.env' 

		def cargar_clave(clave_env: str, ruta_clave_env: str = RUTA_CLAVE) -> str:
    	load_dotenv(dotenv_path=ruta_clave_env)
    	clave = os.getenv(clave_env)
    	if clave is None:
        	raise ValueError(f'La clave {clave_env} no se encuentra en: {ruta_clave_env}')
    	return clave

	
		
Nota:

- En def cargar_clave (...) -> str (la flecha indica el tipo de valor que la función devuelve)
- En 	def cargar_clave(nombre_variable: str, ruta_env: str = "../claves/api_key.env") -> str:
  se puede NO especificar el nombre del archivo api_key.env y poner:
  
 	def cargar_clave(nombre_variable: str, ruta_env: str = "../claves/.env") -> str:
	
  Con esto busca el archivo por extensión y podríamos cambiar en nombnre del archi si queremos en algún momento
  pero creo que es más claro especificando en nombre del archivo.
	
9. ENTORNO
----------
Python version: 3.12.8 (instalada con pyenv-win).Nota: cambiar a esta versión antes de crear el entorno virtual con
Entorno virtual creado con: python -m venv venv
Activación: \Scripts\activate

10.NOTAS
--------

