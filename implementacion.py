import smtplib
import re

def send_email():
    # Pedir al usuario que introduzca su correo electrónico
    while True:
        from_address = input("Introduce tu dirección de correo electrónico : ")
        if re.match(r'^[\w\.-]+@alumno\.huergo\.edu\.ar$', from_address):
            break
        else:
            print("Correo electrónico no válido. Asegúrate de que sea un correo de Gmail.")

    # Pedir al usuario que introduzca el mensaje
    message = input("Introduce el mensaje: ")

    # Crear una lista vacía para almacenar los correos electrónicos de los destinatarios
    to_addresses = []

    # Pedir al usuario que introduzca los correos electrónicos de los destinatarios
    while True:
        to_address = input("Introduce el correo electrónico del destinatario o ingresa 'q' para finalizar: ")
        if to_address.lower() == 'q':
            break
        elif re.match(r'^[\w\.-]+@alumno\.huergo\.edu\.ar$', to_address):
            to_addresses.append(to_address)
        else:
            print("Correo electrónico no válido.")

    # Configurar los detalles del servidor SMTP
    smtp_server = 'smtp.alumno.huergo.edu.ar'
    smtp_port = 587

    # Configurar los detalles del correo electrónico
    subject = 'Correo de prueba'

    # Conectar al servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Pedir al usuario que introduzca la contraseña de su cuenta
    password = input("Introduce la contraseña de tu cuenta: ")

    try:
        # Autenticar con el servidor SMTP
        server.login(from_address, password)

        for to_address in to_addresses:
            # Crear el mensaje de correo electrónico
            message_body = f'From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}'

            # Enviar el correo electrónico
            server.sendmail(from_address, to_address, message_body)
            print(f"Correo electrónico enviado a: {to_address}")

        print("Todos los correos electrónicos han sido enviados exitosamente.")

    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")

    finally:
        # Cerrar la conexión con el servidor SMTP
        server.quit()

if __name__ == "__main__":
    send_email()
