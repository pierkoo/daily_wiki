import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

today=date.today()
today=today.strftime("%d.%m.%Y")


port = 465 #For SSL
password = ''
sender_email = 'dailyw.test@gmail.com'
#receiver_email = sender_email
receiver_email = 'pierkoo@gmail.com'

message = MIMEMultipart("alternative")
message["subject"] = "1Daily wikipedia for "+today
message["From"] = 'Daily Wikipedia'
message["To"] = receiver_email.split('@')[0]

text = """\
        Hi,
        how are you?
        Your daily dose of Wikipedia:
        www.wikipedia.pl"""

html = """\
        <html>
            <body>
                <p>Hi!<br>
                    How are you? <br>
                    Your daily dose of <a href="http://www.wikipedia.pl">
                    Wikipedia </a>
                </p>
                <img src="test_attachment.jpg">
            </body>
        </html>
        """
# turn these into plain/html MIMEText objects
part1 = MIMEText(text,"plain")
part2 = MIMEText(html,"html")

# Add plain/html parts to MIMEMultipart message
# The email client will try to render the last part first

message.attach(part1)
#message.attach(part2)


filename="test_attachment.jpg"

#open file in binary mode
with open(filename,"rb") as attachment:
    # Add file as application/ octet-stream
    #Email  client can usually download this automatically as attachment

    part=MIMEBase("application","octet-stream")
    part.set_payload(attachment.read())

# encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename={filename}",
)

# Add attachment to message and convert message to string:

message.attach(part)
final_text=message.as_string()

# Create a secure SSL connection and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, final_text)
