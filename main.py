from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd

# initialize the browser
driver = webdriver.Firefox()
driver.get('https://www.meteored.com.ar/')

WebDriverWait(driver, 3)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#sendOpGdpr')))\
    .click()

WebDriverWait(driver, 3)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#search_pc')))\
    .send_keys('Rosario')

WebDriverWait(driver, 3)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/span/span[1]/form/div/ul/li[1]/a/span[2]')))\
    .click()

WebDriverWait(driver, 3)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/span[2]/span/span/ul/li[3]/a')))\
    .click()

column1 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[4]').text.split('\n')

column2 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[11]').text.split('\n')

column3 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[18]').text.split('\n')

column4 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[25]').text.split('\n')

column5 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[32]').text.split('\n')

column6 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[39]').text.split('\n')

column7 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[46]').text.split('\n')

column8 = driver.find_element(
    By.XPATH, '/html/body/span[2]/span[2]/span/span[2]/section/table/tbody/tr[53]').text.split('\n')

todays_weather = [column1, column2, column3,
                  column4, column5, column6, column7, column8]

hours = list()
temp = list()
wind = list()

for data in todays_weather:
    hours.append(data[0])
    temp.append(data[1])
    wind.append(data[4])

data_frame = pd.DataFrame(
    {'Hours': hours, 'Temperature': temp, 'Wind Speed': wind})
data_frame.to_csv('todays-time.csv', index=False)
driver.quit()
