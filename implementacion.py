import smtplib
import re

def send_email():
    # Pedir al usuario que introduzca su correo electrónico
    while True:
        from_address = input("Introduce tu dirección de correo electrónico (dominio @gmail.com): ")
        if re.match(r'^[\w\.-]+@gmail\.com$', from_address):
            break
        else:
            print("Correo electrónico no válido. Asegúrate de que sea un correo de Gmail.")

    # Pedir al usuario que introduzca el mensaje
    message = input("Introduce el mensaje: ")

    # Pedir al usuario que introduzca el correo del destinatario
    while True:
        to_address = input("Introduce el correo electrónico del destinatario (dominio @gmail.com): ")
        if re.match(r'^[\w\.-]+@gmail\.com$', to_address):
            break
        else:
            print("Correo electrónico no válido. Asegúrate de que sea un correo de Gmail.")

    # Configurar los detalles del servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Configurar los detalles del correo electrónico
    subject = 'Correo de prueba'

    # Conectar al servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Pedir al usuario que introduzca la contraseña de su cuenta de Gmail
    password = input("Introduce la contraseña de tu cuenta de Gmail: ")

    try:
        # Autenticar con el servidor SMTP
        server.login(from_address, password)

        # Crear el mensaje de correo electrónico
        message_body = f'From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}'

        # Enviar el correo electrónico
        server.sendmail(from_address, to_address, message_body)
        print("Correo electrónico enviado exitosamente.")

    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")

    finally:
        # Cerrar la conexión con el servidor SMTP
        server.quit()

if __name__ == "__main__":
    send_email()
