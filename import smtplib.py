import smtplib
from email.mime.text import MIMEText


smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
username = 'daiafrazao@hotmail.com'
password = 'maringa01'

def enviar_email(destinatario, assunto, corpo):
    msg = MIMEText(corpo)
    msg['Subject'] = assunto
    msg['From'] = username
    msg['To'] = destinatario

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, destinatario, msg.as_string())
    server.quit()

# Exemplo de uso
destinatario = 'daiafrazao@hotmail.com'
assunto = 'teste'
corpo = 'testando1'

destinatario = 'lois.paloschi@outlook.com'
assunto = 'teste'
corpo = 'Good Morning, Lois'

destinatario = 'daiafrazao@gmail.com'
assunto = 'teste'
corpo = 'testando'

destinatario = 'leonardoh.deoliveira@gmail.com'
assunto = 'teste'
corpo = 'Good Morning, Leonardo'

destinatario = 'annapaula2022@gmail.com'
assunto = 'teste'
corpo = 'Good Morning, Ana'


enviar_email(destinatario, assunto, corpo)
