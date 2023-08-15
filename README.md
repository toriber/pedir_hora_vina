# Aplicación de Notificación de Disponibilidad de Hora para Pedir Licencia en Viña del Mar

Esta es una aplicación de Python que te permite recibir una notificación por correo electrónico cuando haya una hora disponible para pedir licencia en la Municipalidad de Viña del Mar.

## Configuración

1. Clona o descarga este repositorio a tu máquina local.

2. Abre el archivo `config.yaml` en un editor de texto.

3. Modifica el archivo `config.yaml` con la siguiente información:

```yaml
cuenta_origen:
  correo: sucorreo@sudominio.cl
  contrasena: aquivasucontrasena
cuentas_destino:
  correos:
  - cuenta1_destino@sudominio.cl
  - cuenta2_destino@sudominio.cl
mensaje: 
  cuerpo: Hola que tal este es el mensaje que enviaras cuando se consiga la hora!
  asunto: AAA HAY HORA 
rut: 193335559
```
## Instalación
1. Instala las dependencias necesarias ejecutando el siguiente comando
```bash
pip install -r requirements.txt 
```
## Uso
1. Ejecuta el script principal para verificar la disponibilidad de hora
```bash
python pedir_hora_licencia.py
```
2. Si hay una hora disponible, recibirás un correo en la dirección especificada en `config.yaml`
## Contribución
Si encuentras errores o mejoras, siéntete libre de contribuir abriendo un problema o enviando una solicitud de extracción.
## Creditos
Esta aplicación fue creada por el usuario toriber, para más contenido revisar [mi perfil en GitHub](https://github.com/toriber)
