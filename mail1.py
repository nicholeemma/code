
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
#print( "表单数量:", book.nsheets)
#print ("表单名称:", book.sheet_names())
sh = book.sheet_by_index(0)
#print (u"表单 %s 共 %d 行 %d 列" % (sh.name, sh.nrows, sh.ncols))
data_list=[]
data_list.extend(sh.col_values(0))
for item in data_list:
	email=item
	server.sendmail("hp-yangjiayue@live.cn", email, 'lol')

	
# 获取第1个表单


#file = pd.ExcelFile('F:/论文/code/Excel Workbook Template.xlsx') #Establishes the excel file you wish to import into Pandas

#df = file.parse('Sheet1') #Uploads Sheet1 from the Excel file into a dataframe
#df = df.DataFrame(df)
#for row in df.rows(): #Loops through each row in the dataframe
    #email = row['Email Address'] 
     #Sets dataframe variable, 'email' to cells in column 'Email Addresss'
    #print(email)

   # 

