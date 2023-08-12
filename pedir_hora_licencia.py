from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
import time
import smtplib
from email.mime.text import MIMEText
import numpy as np
import yaml

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
def main(correo_origen: str,contrasena: str,destino: list,mensaje: dict):
    """
    correo_origen : Str con el correo de origen
    contrasena: Str con la contraseña del correo origen
    destino: Lista de correos destinatarios
    mensaje: Dict con dos llaves, "cuerpo": Str con el cuerpo del correo 
                                , "asunto": Str con el asunto del correo
    """
    start_time=time.time()
    F_hora=False
    it=0
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    while not F_hora:
        med_time=time.time()
        it+=1
        print(rf"Iteración {it}, han pasado {med_time-start_time} segundos")
        driver = webdriver.Chrome(options=op)
        driver.get("https://sertex2.stonline.cl/VinaDelMar/CuposAtencion/Formularios/usuario.aspx")
        driver.implicitly_wait(10)
        time.sleep(5+np.random.rand(1)[0]*10)
        rut_box=driver.find_element(By.ID, "txtRut")
        dropdown=driver.find_element(By.ID, "tipoTramite")
        select = Select(dropdown)
        select.select_by_value("002") # Renovación
        rut_box.send_keys("196895639")
        boton=driver.find_element(By.ID, "lnkIngresar")
        boton.click()
        try:
            warning=driver.find_element(By.ID,"swal2-content")
            warning.text
            if "no hay cupos disponibles" in warning.text:
                driver.quit()
                time.sleep(180+np.random.rand(1)[0]*100)
            else:
                F_hora=True
        except NoSuchElementException:
            F_hora=True
    final_time=time.time()
    print(f"Se logró, pasaron {final_time-start_time} segundos")
    subject = mensaje["asunto"]
    body = mensaje["cuerpo"]
    sender = correo_origen
    recipients = destino
    password = contrasena
    send_email(subject, body, sender, recipients, password)
    print("HAY HORAAA")

if __name__ =='__main__':
    ruta_archivo="config.yaml"
    with open(ruta_archivo, 'r') as archivo:
        contenido = yaml.safe_load(archivo)
    correo_origen=contenido["cuenta_origen"]["correo"]
    contrasena=contenido["cuenta_origen"]["contrasena"]
    cuentas_destino=contenido["cuentas_destino"]["correos"]
    mensaje=contenido["mensaje"]

    main(correo_origen,contrasena,cuentas_destino,mensaje)
    