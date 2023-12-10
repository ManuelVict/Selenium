import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#config
op = Options()
op.add_argument("--headless")
op.add_argument("--disable-gpu")
driver = webdriver.Chrome()
driver.get('https://saucedemo.com')
title = driver.title
#getUsers
listUsers = driver.find_element(by=By.ID, value="login_credentials")
finalListUser = listUsers.text.splitlines()
finalListUser.pop(0)
user=random.choice(finalListUser)
#getPassword
credentials = driver.find_element(by=By.CLASS_NAME, value="login_password")
password = credentials.text.splitlines()
password = password.pop(1)
#Login
driver.find_element(by = By.ID, value = "user-name").send_keys(user)
driver.find_element(by = By.ID, value = "password").send_keys(password)
driver.find_element(by = By.ID, value = "login-button").click()
#getProducts
listProducts=[]
products=driver.find_elements(by = By.CLASS_NAME, value = "inventory_item_name")
for item in products:
    listProducts.append(item.text)
#makeObject
data={
    "username":user,
    "password":password,
    "login_header":title,
    "product_lines":listProducts
}
#print
print(data)


