
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from ah.config import config as c

SMTP_SERVER = 'urupro.com'

def enviarMensaje(desde, hacia, asunto, mensaje):
    msg = MIMEText(mensaje)

    origen = desde
    destino = hacia
    msg['Subject'] = asunto
    msg['From'] = desde
    msg['To'] = hacia

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP(c['SMTP_SERVER'])
    s.login(c['STMP_USER'], c['SMTP_PASSWORD'])
    s.sendmail(origen, [destino], msg.as_string())
    s.quit()



def enviarMensajeAdjunto(desde, hacia, asunto, mensaje, adjuntos=None):

    msg = MIMEMultipart()
    msg['From'] = desde
    msg['To'] = COMMASPACE.join(hacia)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje))

    for f in adjuntos or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    smtp = smtplib.SMTP(c['SMTP_SERVER'])
    smtp.login(c['STMP_USER'], c['SMTP_PASSWORD'])
    smtp.sendmail(desde, hacia, msg.as_string())
    smtp.close()

