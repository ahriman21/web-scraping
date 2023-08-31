### start selenium : 
```
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
```

#### 1. the website we want to scrap :
```
url = 'https://google.com'
driver.get(url)
```

#### 2 . print out title of web document, using 'title' property :
```
print('this is target website\'s title : ' + driver.title)
```

#### 3. get an alement :
```
input = driver.find_element(By.NAME, 'value')
```

#### 4. send value to inputs and submit (if the inputs sent data using ajax we use execute_script()):
```
input.send_keys('value')
submit_btn = driver.find_element(By.CLASS_NAME, 'contact-form-btn')
driver.execute_script('arguments[0].click();', submit_btn)
```


#### 5. wait until the element get ready on the page :
```
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.LINK_TEXT, 'text')
    )
    element.click()
finally:
    driver.quit()
```

#### note => implicity wait :
```
seconds = 4
driver.implicity_wait(seconds)
```

#### 6. go back to previous page or go forward page:
```
driver.back()
driver.forward()
```

#### 7. clear the text in a text box like search bar:
```
search_bar = driver.find_element(By.NAME, 'search')
search_bar.clear()
```


#### 8. action chains => to make actions serveral times in a sequence
```
element = driver.find_element(By.ID, 'x')
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.click(element)
for i in range(100):
    actions.perform()
```



#### END. quit browser :
```
import time
time.sleep(5)
driver.quit()
```