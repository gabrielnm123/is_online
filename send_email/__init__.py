import smtplib
import email.message

class SendEmail():
    def __init__(self, subject: str, from_email: str, to: str, password: str, smtp_server: str, smtp_port: str) -> None:
        self.subject = subject
        self.from_email = from_email
        self.to = to
        self.password = password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def get_body_and_ip(self, body_in_file: str, ip: str) -> None:
        with open(body_in_file, 'r') as body:
            self._body = body.read().format(ip=ip)

    def send(self) -> None:
        msg = email.message.Message()
        msg['Subject'] = self.subject
        msg['From'] = self.from_email
        msg['To'] = self.to
        password = self.password
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(self._body)
        s = smtplib.SMTP(f'{self.smtp_server}: {self.smtp_port}')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
