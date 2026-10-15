from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://realpython.github.io/fake-jobs/")
print(driver.title)
driver.quit()