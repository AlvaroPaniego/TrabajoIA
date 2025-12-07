import ollama 
import fitz #Para subir ficheros
import io



ruta_correo_usuario = '../textos/correo_4.pdf'

modelo = 'llama3.2:1b'



#st.file_uploader() devuelve un objeto de tipo UploadedFile
#fitz.open() no admite directamente ese tipo de objetos pero sí admite streams(buffer en RAM que se comporta como un archivo)
#Por eso hay que convertir primero el objeto UploadedFile a stream con io.Bytes() y guardarlo en una variable (pdf_stream)
#Ahora fitz.open(stream = pdf_stream) puede abrirlo como si fuera un archivo en memoria


def obtener_correo_usuario (pdf_obj):

    pdf_stream = io.BytesIO(pdf_obj.read()) #convertido pdf_obj a stream (buffer en memoria que se comporta como un archivo) 
    with fitz.open(stream = pdf_stream, filetype='pdf') as correo_usr:
        texto_correo = ''

        for correo in correo_usr:
            texto_correo = texto_correo + correo.get_text('text')
 
    return texto_correo

correo_usuario = ''


def convertir_tono_correo (tono, correo, modelo):

    try:
        
        peticion_al_modelo=[
            {
                'role': 'system',
                'content': (
                f'Eres un asistente que escribe emails para una empresa de reparación de equipos informáticos\n'
                f'Tu tarea es adaptar el estilo del correo al tono indicado.\n'
                
                )  
            },

            {
                'role': 'user',
                'content': f'Por favor, reescribe este correo: {correo} en tono: {tono}'
          
            }
        ]

        respuesta = ollama.chat(model=modelo, messages=peticion_al_modelo, options ={'temperature':0.3})
        return respuesta['message']['content']

       
    except Exception as e:

        return f"Error!!!: {e}"

        

