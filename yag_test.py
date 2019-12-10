import yagmail
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

today=date.today()
today=today.strftime("%d.%m.%Y")

receiver_email = 'pierkoo@gmail.com'

message = MIMEMultipart("alternative")
message["subject"] = "2Daily wikipedia for "+today
message["From"] = 'Daily Wikipedia'
message["To"] = receiver_email.split('@')[0]


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
part2 = MIMEText(html,"html")

# Add plain/html parts to MIMEMultipart message
# The email client will try to render the last part first

message.attach(part2)
final_text=message.as_string()


body = 'Hello!'
filename='test_attachment.jpg'

# keyring to be tested
yag=yagmail.SMTP('dailyw.test@gmail.com')

yag.send(
    to=receiver_email,
    subject='subject test',
    contents=final_text,
    attachments=filename,
)
