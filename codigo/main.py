import fitz
import streamlit as st
from PIL import Image
import os
from groq import Groq

from modelo_api import peticion_correo


salir = False

while not salir:

    os.system('cls')

    tono = input('|Asistomail|: ¿Qué tono quieres que use en el correo? (formal, neutro, informal): ')
    peticion = input('|Asistomail|: ¿Qué correo escribo?: ')
    print(f'\n|Asistomail|:  {peticion_correo(tono, peticion)}')
    
    opc = input('¿Quieres que redacte otro correo?: pulsa [n] = no -- [s] = sí -> ').strip().lower()
     
    while opc != 'n' and opc != 's':
        opc = input('Tecla incorrecta: ¿Continuar?: pulsa [n] = no -- [s] = sí -> ').strip().lower()
    
    if opc == 'n':
        salir = True  
         
#strip quita los posible espacios y lower convierte a minúsculas