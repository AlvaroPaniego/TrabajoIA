import ollama 
import fitz #Para subir ficheros


ruta_correo_usuario = '../textos/correo_1.pdf'

modelo = 'llama3.2:1b'

def obtener_correo_usuario (ruta):

    correo_usr = fitz.open(ruta)
    texto_correo = ''
    for correo in correo_usr:
        texto_correo = texto_correo + correo.get_text()
    return texto_correo

correo_usuario = ''


def convertir_tono_correo (tono, correo, modelo):

    try:
        
        peticion_al_modelo=[
            {
                'role': 'system',
                'content': (
                f'Eres un asistente que escribe emails para una empresa de reparación de equipos informáticos\n'
                f'Tu estilo debe adaptarse al nivel de formalidad indicado en: {tono}.\n'
                f'Tus repuestas deben estar adaptadas al contexto.\n'
                f'Si la petición {correo} no forma parte del contexto reparación de equipos informáticos, no generes el correo' 
                )  
            },
            {
                'role': 'user',
                'content': f"Redacta un nuevo correo con el siguiente tono: {tono} en base al correo: {correo}"
            }
        ]

        respuesta = ollama.chat(model=modelo, messages=peticion_al_modelo)
        return respuesta['message']['content']

        #print (respuesta['message']['content'])
        
    except Exception as e:

        return f"Error!!!: {e}"

        


#SALIDAS:

correo_usuario = obtener_correo_usuario(ruta_correo_usuario)
print('\n\033[91m(CORREO USUARIO)\033[0m\n')
print(correo_usuario)
print('\n\033[92m(CORREO CORREGIDO)\033[0m\n')
print(convertir_tono_correo('formal', correo_usuario, modelo))

