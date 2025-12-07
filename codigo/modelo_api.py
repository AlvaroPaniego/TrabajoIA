import os
from groq import Groq

from acceso_clave import cargar_clave

#api_key = cargar_clave('API_KEY', 'TrabajoIA/claves/api_key.env')
api_key = cargar_clave('API_KEY', '../claves/api_key.env')
#print (f'La clave es: {api_key}')

client = Groq(api_key = api_key)
nombre_modelo="llama-3.3-70b-versatile"
conversation_history = []

def chat_with_memory(user_input):
    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=nombre_modelo,
        messages=conversation_history,
        temperature=0.4
    )

    reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return reply