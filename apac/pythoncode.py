# Python script for Amazon product availability checker
# importing libraries
from lxml import html
import requests
from time import sleep
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


receiver_email_id = "EMAIL_ID_OF_USER"


def check(url):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	

	page = requests.get(url, headers = headers) 
	for i in range(20):
		
		sleep(3) 
		
		doc = html.fromstring(page.content)
		
		XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
		RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
		AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
		return AVAILABILITY

	
def sendemail(ans, product):
	GMAIL_USERNAME = "YOUR_GMAIL_ID"
	GMAIL_PASSWORD = "YOUR_GMAIL_PASSWORD"
	
	recipient = receiver_email_id
	body_of_email = ans
	email_subject = product + ' product availability'
	
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	
	s.starttls() 
	
	s.login(GMAIL_USERNAME, GMAIL_PASSWORD) 
	
	headers = "\r\n".join(["from: " + GMAIL_USERNAME,
						"subject: " + email_subject,
						"to: " + recipient,
						"mime-version: 1.0",
						"content-type: text/html"])

	content = headers + "\r\n\r\n" + body_of_email
	s.sendmail(GMAIL_USERNAME, recipient, content)
	s.quit() 


def ReadAsin():

	Asin = 'B077PWK5BT'
	url = "http://www.amazon.in/dp/" + Asin
	print ("Processing: "+url)
	ans = check(url)
	arr = [
		'Only 1 left in stock.',
		'Only 2 left in stock.',
		'In stock.']
	print(ans)
	if ans in arr:
		
		sendemail(ans, Asin) 

# scheduling same code to run multiple
# times after every 1 minute 
def job():
	print("Tracking....") 
	ReadAsin()

schedule.every(1).minutes.do(job)

while True:
	
	# running all pending tasks/jobs
	schedule.run_pending() 
	time.sleep(1)
