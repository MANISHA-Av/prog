import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.starttls()
ob.login('ishitaraj103@gmail.com','Thisismanisha@123')
subject="sending emails using python"
body="this is manisha"
message="subject :{}\n\n{}".format(subject,body)
#(message)
listOfAddress=['vikashlashmi@gmail.com','vikash@hurreytech.com']
ob.sendmail("ishitaraj103@gmail.com",listOfAddress,message)
print('send successfully')
ob.quit()
