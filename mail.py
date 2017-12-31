#!/usr/bin/python
import smtplib  
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
"""The first step is to create an SMTP object, each object is used for connection with one server."""  
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = "hp-yangjiayue@live.cn"
password = "yjy1996426"
to_addr = "790956043@qq.com"
smtp_server = "smtp-mail.outlook.com"

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'RS GC MTAXI <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'本月不合规出行确认', 'utf-8').encode()

server = smtplib.SMTP('smtp-mail.outlook.com','587')  
server.ehlo()
server.starttls()   
#Next, log in to the server  
server.login("hp-yangjiayue@live.cn","yjy1996426")  
   
#Send the mail  
 # The \n separates the message from the headers  
server.sendmail("hp-yangjiayue@live.cn", "790956043@qq.com", msg.as_string())
server.quit()