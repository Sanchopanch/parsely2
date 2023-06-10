from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def get_serp(key_word):
    key_word_plus = key_word.replace(' ','+')
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://www.google.com/search?q=facebook')

    exelement = driver.find_element(By.PARTIAL_LINK_TEXT, 'Facebook')
    # print(
    #     f'found link {exelement.get_attribute("href")}  with class={exelement.get_attribute("class")} and ancor = {exelement.text}')
    parDiv = exelement.find_elements(By.XPATH, "./..");
    # print(f'parent class= {parDiv[0].get_attribute("class")}')

    elementList = parDiv[0].find_elements(By.TAG_NAME, "div")
    val = elementList[0].get_attribute("class")
    # print(val)
    elementList = elementList[0].find_elements(By.TAG_NAME, "cite")
    targClass = elementList[0].get_attribute("class")
    print(f'found targ text={elementList[0].text} class={targClass}')
    targClass = targClass.replace(' ', '.')

    driver.get(f'https://www.google.com/search?q={key_word_plus}')
    rez = []

    # первая страница ***************************************************
    links = driver.find_elements(By.CSS_SELECTOR, f'cite.{targClass}')
    for el in links:
        if not el.text == '':
            # print(f' lin ={el.text}')
            rez.append(el.text.split('›')[0].replace('https://', '').replace('http://', '').strip())

    nextLink = driver.find_elements(By.ID, 'pnnext')
    driver.get(nextLink[0].get_attribute("href"))

    # вторая страница ***************************************************

    links = driver.find_elements(By.CSS_SELECTOR, f'cite.{targClass}')
    for el in links:
        if not el.text == '':
            # print(f' lin ={el.text}')
            rez.append(el.text.split('›')[0].replace('https://', '').replace('http://', '').strip())
    nextLink = driver.find_elements(By.ID, 'pnnext')
    driver.get(nextLink[0].get_attribute("href"))

    nextLink = driver.find_elements(By.ID, 'pnnext')
    driver.get(nextLink[0].get_attribute("href"))
    # третья страница ***************************************************

    links = driver.find_elements(By.CSS_SELECTOR, f'cite.{targClass}')
    for el in links:
        if not el.text == '':
            # print(f' lin ={el.text}')
            rez.append(el.text.split('›')[0].replace('https://', '').replace('http://', '').strip())

    driver.close()
    return rez

if __name__ == "__main__":
    serp = get_serp('kochetkov spb')
    print(serp)