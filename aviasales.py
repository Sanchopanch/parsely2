from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# display = Display(visible=1, size=(1200, 800))
# display.start()
options = Options()

options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 500)

# driver.set_page_load_timeout(7)
# driver.implicitly_wait(5)

driver.get('https://www.aviasales.ru/?params=SVX0708LED1')
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "trip-duration__input-wrapper")))
element_present = EC.presence_of_element_located((By.CLASS_NAME, 'trip-duration__input-wrapper'))
WebDriverWait(driver, 10).until(element_present)
kogda = driver.find_element(By.CLASS_NAME, 'trip-duration__input-wrapper')
kogda.click()
print(f'нажали на поле когда {kogda.__class__}')
# time.sleep(3)
# next_month = driver.find_element(By.XPATH,".//button[contains(@class,'calendar-navbar__button')] AND [contains(@class,'next')]");
# # next_month = driver.find_element(By.CLASS_NAME, 'calendar-navbar__button --next')
# print(next_month)
# next_month.click()
# print(f'нажат следующий месяц {next_month.__class__}')
time.sleep(3)

days = [driver.find_element(By.XPATH,".//div[contains(@class,'calendar-day')]")];
for day in days:
    print(f' day class={day.__class__}')
# day.click()
# print(f'нажат день {day.__class__}')
time.sleep(10)



# driver.close()
# display.stop()

