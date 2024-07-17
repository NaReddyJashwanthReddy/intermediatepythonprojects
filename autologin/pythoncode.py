from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 
def autologin(user_name,password,url):

	driver=webdriver.Chrome() 
	driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&") 


	driver.find_element(By.XPATH,'//*[@id="ap_email"]').send_keys(user_name) 


	driver.find_element(By.XPATH,'//*[@id="continue"]').click() 
	

	driver.find_element(By.XPATH,'//*[@id="ap_password"]').send_keys(password) 
	driver.find_element(By.XPATH,'//*[@id="continue"]').click() 

	#time.sleep(10) 

	#driver.close() 
 
name=input("Enter the username : ")
password=input("Enter the password : ")
autologin(name,password,)
