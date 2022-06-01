import os
from time import sleep, time
from dotenv import load_dotenv

load_dotenv()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

kerberos = os.getenv('KERBEROS') #Enter your kerberos here
pin = os.getenv('PIN') #Enter your 6 digit pin here
authentication_password = os.getenv('AUTHENTICATION_PASSWORD') #Enter your password here

chromedriver_location = "/Users/atharvchandratre/Downloads/chromedriver" #Download chromedriver and enter its download location here

securid = input("Enter 6 digit RSA key: ")

start_time = time()
print("Start time = "+str(start_time))

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://login.gs.com/vpn/index.html")

username_textbox = '//*[@id="login"]'
login_password_textbox = '//*[@id="passwd"]'
region_dropdown = '//*[@id="region"]'
apac2_region = '//*[@id="region"]/option[4]'
login_button = '/html/body/div/div[1]/div[2]/form/button'
driver.find_element_by_xpath(username_textbox).send_keys(kerberos)
driver.find_element_by_xpath(login_password_textbox).send_keys(pin+securid)
driver.find_element_by_xpath(region_dropdown).click()
driver.find_element_by_xpath(apac2_region).click()
driver.find_element_by_xpath(login_button).click()

nds_icon = '//*[@id="inner-container"]/div/div/div/div/a/div[1]/div'
wait1 = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH, nds_icon)))
driver.find_element_by_xpath(nds_icon).click()

password_textbox = '//*[@id="logings-modal-password-password"]'
authenticate_button = '/html/body/div[5]/div/div/div/div[3]/button[1]'
wait2 = WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH, password_textbox)))
driver.find_element_by_xpath(password_textbox).send_keys(authentication_password)
driver.find_element_by_xpath(authenticate_button).click()

sleep(15)
os.system("open "+"/Users/atharvchandratre/Downloads/DCNDS0248244.ica")

end_time = time()
print("End time = "+str(end_time))
print("Time Saved = "+str(end_time-start_time))

f = open("/Users/atharvchandratre/Desktop/timesaved.txt",'r') #Create this file if not created already, and change its location
timesaved = f.read()
timesaved_number = float(timesaved)
timesaved_number+=((end_time-start_time)*2.5)
f.close()
f = open("/Users/atharvchandratre/Desktop/timesaved.txt","w") #Change the location of this file here too, same as the above
f.write(str(timesaved_number))
f.close()
