# -*- coding: utf-8 -*-

import smtplib

connection=smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection2=smtplib.SMTP_SSL()
connection.starttls()
connection.login("kumarprasanna565@gmail.com","Gpk@2017")
connection.sendmail("kumarprasanna565@gmail.com","ksivakumar920@gmail.com","two babu")
connection.quit()