import smtplib
import re

def send_email():
    while True:
        email = input("Introduce tu dirección de correo electrónico (dominio @gmail.com): ")
        if re.match(r'^[\w\.-]+@gmail\.com$', email):
            break
        else:
            print("Correo electrónico no válido. Asegúrate de que sea un correo de Gmail.")

    message = input("Introduce el mensaje: ")

    while True:
        to_address = input("Introduce el correo electrónico del destinatario (dominio @gmail.com): ")
        if re.match(r'^[\w\.-]+@gmail\.com$', to_address):
            break
        else:
            print("Correo electrónico no válido. Asegúrate de que sea un correo de Gmail.")

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    from_address = email
    subject = 'Correo de prueba'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    password = input("Introduce la contraseña de tu cuenta de Gmail: ")

    try:
        server.login(from_address, password)

        message_body = f'From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}'

        server.sendmail(from_address, to_address, message_body)
        print("Correo electrónico enviado exitosamente.")

    except smtplib.SMTPAuthenticationError:
        print("Error de autenticación. Asegúrate de que las credenciales sean correctas.")

    finally:
        server.quit()

if __name__ == "__main__":
    send_email()
