from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import getpass
import smtplib
import base64
import pickle
import datefinder
import string
import re
import os.path

#-----------------------------------------Metodos----------------------------------------------
#                       "%Y-%m-%d T %H:%M:%S"
        

def accesoGoogleApi():
        print('Acceso Google Calendar')
        #Accedemos al calendario creado en google api mediante el link el metodo de lectura y escritura
        permiso = ['https://www.googleapis.com/auth/calendar']
        Credencial = None
        #accemos uso del id de cliente  OAuth 2.0 asignado de google
        #verificamos si existe una credencial de usuario en el dispositivo mediante path
        if os.path.exists('Credencial.pkl'):
           with open("Credencial.pkl", "rb") as token:
              Credencial = pickle.load(token)#si existe la cargara como credencial de usuario
        #Si la credencial no existe o es invalida
        if not Credencial or not Credencial.valid:
           if Credencial and Credencial.expired and Credencial.refresh_token:
              Credencial.refresh(Request())#pedira una respuesta al servidor
           else:#si al refrescarla no funciona entonces usaremos nuestro json de cliente secreto para generar una nueva credencial
              IDOAuth = InstalledAppFlow.from_client_secrets_file("secreto_cliente.json", scopes=permiso)
              Credencial = IDOAuth.run_local_server(port=0)#y la almacenaremos en su respectiva variable
              with open('Credencial.pkl', 'wb') as token:#actualizamos o generamos nuestra credencial
                   pickle.dump(Credencial, token)#y la almacenamos en un pkl archivo pickle 
        return build("calendar", "v3", credentials=Credencial)#y retornamos el servicio

def accesoGmail():
        print('Acceso Gmail')
        return smtplib.SMTP_SSL(host='smtp.gmail.com', port= 465)#llamamos el servidor de smtp de gmail con el puerto 465
           
def CrearEvento(Nombre, Ubicacion, Describcion, year, mes, dia, hora, minu, Servicio):
        print('Crear evento')
        result = Servicio.calendarList().list().execute()
        calendar_id = result['items'][0]['id']
        timezone =result['items'][0]['timeZone']
        #obtenemos el calendario mediante
        result = Servicio.events().list(calendarId=calendar_id, timeZone=timezone)
        #print(result)#lo imprimimos
        Hora_inicio = datetime(year, mes, dia, hora, minu, 0)
        Hora_final = Hora_inicio + timedelta(hours=4)
        event = {
          'summary': Nombre,
          'location': Ubicacion,
          'description': Describcion,
          'start': {
            'dateTime': Hora_inicio.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
          },
          'end': {
            'dateTime': Hora_final.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
          },
          'reminders': {
            'useDefault': False,
            'overrides': [
              {'method': 'email', 'minutes': 24 * 60},
              {'method': 'popup', 'minutes': 10},
           ],
          },
        }
        #print(event)
        return Servicio.events().insert(calendarId=calendar_id, body=event, sendNotifications=True).execute()

def ConsultarEventos(Servicio):
        result = Servicio.calendarList().list().execute()
        calendar_id = result['items'][0]['id']
        Pagina = None
        result = Servicio.events().list(calendarId=calendar_id, pageToken=Pagina).execute()
        BAND=True
        while BAND==True:
         for Eventos in result['items']:
           print(Eventos['summary'])
           prueba=Eventos.get('nextPageToken')
           if not prueba:
              BAND=False

def CrearMensaje(Hacia, Servicio, ServicioG, Mensaje):
        print('Crear Mensaje')
        result = Servicio.calendarList().list().execute()
        Correo =result['items'][0]['summary']
        print(Correo)
        VerificadorP= input('Verifique Contraseña')
        Contra =VerificadorP
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',Correo.lower()):
                print("Correo correcto")
                ServicioG.login(Correo, Contra)
        else:
                print("Correo incorrecto")
        
        Msg = MIMEMultipart()
        print('Enviado por: ',Correo)
        Msg['From']=Correo
        print('Hacia: ',Hacia)
        Msg['To']= Hacia
        Msg['Subject']='Invitacion'
        #Mensaje = input ("Ingrese mensaje del correo: ")
        Msg.attach(MIMEText(Mensaje, 'plain'))
        ServicioG.send_message(Msg)
        del Msg
        ServicioG.quit()
        (print("Enviado !!!"))
        
#--------------------------------------Main-----------------------------------------------

#Asunto ='L'#input("Escriba el asunto: ")
#Mensaje ='L'#input("Escriba el Mensaje: ")
#Mensaje=CrearMensaje()

Servicio=accesoGoogleApi()
Hacia='estanciaupv@gmail.com'
Mensaje="Hola a todos y muchos Saludos"
CrearMensaje(Hacia, Servicio, accesoGmail(), Mensaje)
Nombre =input('Ingrese el Nombre de evento')
Ubicacion =input('Ingrese el Ubicacion')
Describcion =input('Ingrese el Descripcion')
year =int(input('Ingrese el año'))
mes =int(input('Ingrese el mes'))
dia =int(input('Ingrese el dia'))
hora =int(input('Ingrese el Hora'))
minu =int(input('Ingrese el Minutos'))
CrearEvento(Nombre, Ubicacion, Describcion, year, mes, dia, hora, minu, Servicio)
ConsultarEventos(Servicio)
