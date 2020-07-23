import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Correo de acceso al servidor
MY_ADDRESS = 'correousertb@gmail.com'
# Password de acceso a la cuenta de email
PASSWORD = 'Luisgerardo3'

# Configurar el servidor de correo
s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
s.login(MY_ADDRESS, PASSWORD)
# Iniciar sesion con los datos de acceso al servidor SMTP

# Crear el Mensaje
msg = MIMEMultipart()

message = "Hola mundo!"

# Imprimir el mensaje
print(message)

# Configurar los parametros del mensaje
msg['From']=MY_ADDRESS
msg['To']= "estanciaupv@gmail.com"
msg['Subject']="Enviar email - Python"

# Agregar el texto del mensaje al mensaje
msg.attach(MIMEText(message, 'plain'))

# Enviar el mensaje
s.send_message(msg)
del msg

# Finaliar sesion SMTP
s.quit()
(print("Enviado !!!"))
