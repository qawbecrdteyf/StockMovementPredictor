import ftplib 
session = ftplib.FTP('203.124.114.1', 'almat', 'alma#007F')
file = open('/home/qawbecrdteyf/Desktop/St-matlab/prediction.csv', 'rb')
file2 = open('/home/qawbecrdteyf/Desktop/St-matlab/data.json', 'rb')
session.cwd('/chirag/')
#session.storbinary('STOR prediction.csv', file)
session.storbinary('STOR dataf.json', file2)
file.close()
file2.close()
session.quit()
