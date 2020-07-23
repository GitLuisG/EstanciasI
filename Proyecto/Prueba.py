from EstanciasI import *

Hacia='estanciaupv@gmail.com'
Mensaje="Hola a todos y muchos Saludos"
Nombre ='Vida salvaje'
Ubicacion ='Mexico'
Describcion ='Solo para gatos'
year =int('2019')
mes =int('09')
dia =int('30')
hora =int('12')
minu =int('00')

Conexion=ServicioGoogle()
Servicio=Conexion.accesoGoogleApi()
Conexion.CrearMensaje(Hacia, Servicio, Conexion.accesoGmail(), Mensaje)
Conexion.CrearEvento(Nombre, Ubicacion, Describcion, year, mes, dia, hora, minu, Servicio)
Conexion.ConsultarEventos(Servicio)
