from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/Admin/Desktop/Oleksii/chromedriver/chromedriver")
url = "https://www.linkedin.com/jobs/search/?currentJobId=3431384206&f_WT=2&geoId=101282230&keywords=node.js&location=Germany&refresh=true"

try:
    driver.get(url=url)
    driver.maximize_window()
    for i in range(1, 100):
        
        time.sleep(5)
        print(f"*** Vacancy №{i} ***")
        job = driver.find_element(By.XPATH, f"//*[@id=\"main-content\"]/section[2]/ul/li[{i}]/div/a")
        job.click()
        time.sleep(5)
        
        company_Name = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/h4/div[1]/span[1]/a").text
        print("Company Name: ", company_Name)
        
        position = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/a/h2").text
        print("Position: ", position)

        print(f"Company LinkedIn: https://de.linkedin.com/company/{company_Name}")

        location = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/h4/div[1]/span[2]").text
        print("Location: ", location)

        level = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[1]/span").text
        print("Level: ", level)

        posted = driver.find_element(By.XPATH, "/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/h4/div[2]/span[1]").text
        print("Posted: ", posted)

        i += 1
        print("\n")
        
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

