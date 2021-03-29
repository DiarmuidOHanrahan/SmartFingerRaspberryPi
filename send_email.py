import smtplib
import email.utils
from email.mime.text import MIMEText

def On():
    msg = MIMEText("The light switch has turned on successfully","plain")
    msg['Subject'] = "Smart Finger"
    msg['From'] = email.utils.formataddr(("Pi","pi@raspberrypi"))
    msg['To'] = email.utils.formataddr(("Recipent","smartfingerfyp@gmail.com"))
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.set_debuglevel(True)
    server.login("smartfingerfyp@gmail.com","DCUcc2021")
    server.sendmail("pi@raspberrypi",["smartfingerfyp@gmail.com"],msg.as_string())
    server.quit()
    
def Off():
    msg = MIMEText("The light switch has turned off successfully","plain")
    msg['Subject'] = "Smart Finger"
    msg['From'] = email.utils.formataddr(("Pi","pi@raspberrypi"))
    msg['To'] = email.utils.formataddr(("Recipent","smartfingerfyp@gmail.com"))
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.set_debuglevel(True)
    server.login("smartfingerfyp@gmail.com","DCUcc2021")
    server.sendmail("pi@raspberrypi",["smartfingerfyp@gmail.com"],msg.as_string())
    server.quit()
