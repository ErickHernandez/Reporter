import smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SMTP:
    def __init__(
        self, sender_email: str, sender_password: str, smtp_host: str, smtp_port: int
    ):
        self._sender_email = sender_email
        self._password = sender_password
        self._host = smtp_host
        self._port = smtp_port

    def sendFileByEmail(
        self, subject: str, body: str, receiver_email: str, attachment_filepath: str
    ):
        message = MIMEMultipart()
        message["From"] = self._sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        filename = attachment_filepath

        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self._host, self._port, context=context) as server:
            server.login(self._sender_email, self._password)
            server.sendmail(self._sender_email, receiver_email, text)
            server.quit()

    def validateEmail(self, email):
        pass
