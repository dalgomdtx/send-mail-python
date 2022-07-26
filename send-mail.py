import os
from email.message import EmailMessage
import ssl
import smtplib
import imghdr

email_emisor = 'email del emisor'
email_password = os.environ.get('EMAIL_PASSWORD')
email_receptor = 'email del receptor'

Titulo = 'Titulo del correo'
mensaje = """
        Mensaje del correo
      Respetando espacios en blanco y saltos de linea
    Ademas de margenes de texto
  adjutando un archivo jpg al final del mensaje
/-/-/-/-/            /-/-/-/-/
"""
#Objeto
em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = Titulo
em.set_content(mensaje)

# Adjuntar un archivo
with open('cat.jpg', 'rb') as im:
  file_data = im.read()
  file_type = imghdr.what(im.name)
  file_name = im.name
em.add_attachment(file_data, filename=file_name, subtype=file_type, maintype='image')

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
  smtp.login(email_emisor, email_password)
  smtp.sendmail(email_emisor, email_receptor, em.as_string())

print('Correo enviado correctamente a: ' + email_receptor)