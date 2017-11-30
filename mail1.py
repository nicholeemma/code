import win32com.client
import pandas as pd
import smtplib
import xlrd

"""The first step is to create an SMTP object, each object is used for connection with one server."""  
server = smtplib.SMTP('smtp-mail.outlook.com','25') 
#https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
server.ehlo()
server.starttls()   
#Next, log in to the server  
server.login("hp-yangjiayue@live.cn","1996426") 

# 打开 xls 文件
book = xlrd.open_workbook("F:/论文/code/Excel Workbook Template.xlsx")
print( "表单数量:", book.nsheets)
print ("表单名称:", book.sheet_names())
sh = book.sheet_by_index(0)
print (u"表单 %s 共 %d 行 %d 列" % (sh.name, sh.nrows, sh.ncols))
s=sh.col(0)
for r in sh.nrows:
	print (s.row(r))
# 获取第1个表单


#file = pd.ExcelFile('F:/论文/code/Excel Workbook Template.xlsx') #Establishes the excel file you wish to import into Pandas

#df = file.parse('Sheet1') #Uploads Sheet1 from the Excel file into a dataframe

#for row in df.iterrows(): #Loops through each row in the dataframe
 #   email = str((row['Email Address']))  #Sets dataframe variable, 'email' to cells in column 'Email Addresss'
  #  subject = (row['Subject']) #Sets dataframe variable, 'subject' to cells in column 'Subject'
   # body = str((row['Email HTML Body'])) #Sets dataframe variable, 'body' to cells in column 'Email HTML Body'

    #if (pd.isnull(email) or pd.isnull(subject) or pd.isnull(body)): #Skips over rows where one of the cells in the three main columns is blank
     #   continue

   # server.sendmail("hp-yangjiayue@live.cn", email, body)


