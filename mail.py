#!/usr/bin/python
import smtplib  
"""The first step is to create an SMTP object, each object is used for connection with one server."""  
server = smtplib.SMTP('smtp-mail.outlook.com','25')  
server.ehlo()
server.starttls()   
#Next, log in to the server  
server.login("hp-yangjiayue@live.cn","1996426")  
   
#Send the mail  
msg = "\nHello!" # The \n separates the message from the headers  
server.sendmail("hp-yangjiayue@live.cn", "790956043@qq.com", msg)


