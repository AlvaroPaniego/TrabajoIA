import os
from groq import Groq

from acceso_clave import cargar_clave

api_key = cargar_clave('API_KEY')
#print (f'La clave es: {api_key}')

client = Groq(api_key = api_key)
nombre_modelo="llama-3.3-70b-versatile"

peticion = ''
tono = ''

def peticion_correo(tono, peticion):

    response = client.chat.completions.create(
    model=nombre_modelo, 
    #messages es una lista con dos diccionarios 
    messages=[  

            {'role': 'system', 
             'content': (
                f'Eres un asistente que escribe emails para una empresa de reparación de equipos informáticos\n'
                f'Tu estilo debe adaptarse al nivel de formalidad indicado en: {tono}.\n'
                f'Tus repuestas deben estar adaptadas al contexto.\n'
                f'Si la petición {peticion} no forma parte del contexto reparación de equipos informáticos, no generes el correo' 
                ), 
            },
            {'role': 'user', 'content': f'Por favor, redacta un correo en tono {tono} para la petición {peticion}'}                                
    ]
    )

    return response.choices[0].message.content