import yagmail
from datetime import datetime

today=str(datetime.now())
#today=today.strftime("%d.%m.%Y")

receiver_email = {'pierkoo@gmail.com':'pierkoo'}


html = 'message.html'


filename='test_attachment.jpg'

# keyring to be tested
yag=yagmail.SMTP({'dailyw.test@gmail.com':'Daily Wiki'})

yag.send(
    to=receiver_email,
    subject='DailyW for '+today,
    contents=[html],
)
