import base64
import httplib2

from email.mime.text import MIMEText

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from google_auth_oauthlib.flow import InstalledAppFlow
permiso = ['https://www.googleapis.com/auth/gmail.send']
memoria = Storage('gmail.storage')
IDOAuth = InstalledAppFlow.from_client_secrets_file("secreto_cliente_Gmail.json", scopes=permiso)
http = httplib2.Http()
credentials = memoria.get()
if credentials is None or credentials.invalid:
  credentials = run_flow(IDOAuth, memoria, http=http)

Servicio=build('gmail', 'v1', credentials=credentials)
http = credentials.authorize(credentials)

message = MIMEText("Message")
message['to'] = "correousertb@gmail.com"
message['from'] = "estanciaupv@gmail.com"
message['subject'] = "Subject"
body = {'raw': base64.b64encode(message.as_bytes())}

Servicio.users().messages().send(userId="me",body=body).execute()
