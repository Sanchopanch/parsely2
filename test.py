from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get('https://www.google.com/search?q=facebook')
# print(driver.title)
#element = driver.find_elements_by_css_selector('.rso a')[0]
# element = driver.find_element(By.CSS_SELECTOR, 'wDsc0')

exelement = driver.find_element(By.PARTIAL_LINK_TEXT, 'Facebook')
print(f'found link {exelement.get_attribute("href")}  with class={exelement.get_attribute("class")} and ancor = {exelement.text}')
parDiv = exelement.find_elements(By.XPATH,"./..");
print(f'parent class= {parDiv[0].get_attribute("class")}')


elementList = parDiv[0].find_elements(By.TAG_NAME,"div")
val = elementList[0].get_attribute("class")
print(val)
elementList = elementList[0].find_elements(By.TAG_NAME,"cite")
targClass = elementList[0].get_attribute("class")
print(f'found targ text={elementList[0].text} class={targClass}')
targClass= targClass.replace(' ','.')

driver.get('https://www.google.com/search?q=kochetkov+spb')
rez = []

links = driver.find_elements(By.CSS_SELECTOR, f'cite.{targClass}')
for el in links:
    if not el.text == '':
        # print(f' lin ={el.text}')
        rez.append(el.text.split('›')[0].replace('https://','').replace('http://',''))

nextLink = driver.find_elements(By.ID,'pnnext')
# print(f'next button href ={nextLink[0].get_attribute("href")}')

driver.get(nextLink[0].get_attribute("href"))
links = driver.find_elements(By.CSS_SELECTOR, f'cite.{targClass}')
for el in links:
    if not el.text == '':
        # print(f' lin ={el.text}')
        rez.append(el.text.split('›')[0].replace('https://', '').replace('http://', ''))
driver.close()
print(rez)