import smtplib
import re
#lxpkuscllmssplxl
def get_smtp_server(email):
    if re.match(r'^[\w\.-]+@gmail\.com$', email):
        return 'smtp.gmail.com', 587
    elif re.match(r'^[\w\.-]+@(outlook|hotmail)\.(com|es)$', email):
        return 'smtp-mail.outlook.com', 587
    else:
        return None, None

def send_email():
    # Pedir al usuario que introduzca su dirección de correo electrónico
    while True:
        from_address = input("Introduce tu dirección de correo electrónico: ")
        if re.match(r'^[\w\.-]+@(gmail|outlook|hotmail)\.(com|es)$', from_address):
            break
        else:
            print("Dirección de correo electrónico no válida.")

    # Pedir al usuario que introduzca el mensaje
    message = input("Introduce el mensaje: ")

    # Crear una lista vacía para almacenar las direcciones de correo de los destinatarios
    to_addresses = []

    # Pedir al usuario que introduzca las direcciones de correo de los destinatarios
    while True:
        to_address = input("Introduce la dirección de correo del destinatario o ingresa 'q' para finalizar: ")
        if to_address.lower() == 'q':
            break
        elif re.match(r'^[\w\.-]+@[\w\.-]+\.[\w\.-]+$', to_address):
            to_addresses.append(to_address)
        else:
            print("Dirección de correo electrónico no válida.")

    # Obtener el servidor SMTP correspondiente según el dominio del remitente
    smtp_server, smtp_port = get_smtp_server(from_address)

    if smtp_server is None:
        print("No se pudo determinar el servidor SMTP para el remitente.")
        return

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
            message_body = f'From: {from_address}\nTo: {to_address}\nSubject: Correo de prueba\n\n{message}'

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
