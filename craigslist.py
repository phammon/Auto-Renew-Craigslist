#!/bin/env python
from pprint import pprint
from selenium import webdriver
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = "your email here"
msg['To'] = "your email here"
msg['subject'] = "Craiglist Listing has been re-listed!"

body = "Your listing for [your item here] has automatically been updated for you, click the link to see your listing [your link here]"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("your email here", "your password here")

text = msg.as_string()
server.sendmail("your email here", "your password here", text)
server.quit()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('link here to update')

button = driver.find_element_by_css_selector('form.manage.renew')
button.click()

#cronjob to automaticall run your script every few days
#PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
#30 10 * * 1,4,7 python /Path-to-script/craigslist.py
