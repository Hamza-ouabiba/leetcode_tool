from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Chrome()

driver.get("https://leetcode.com/accounts/login/")

input("Please log in manually, then press Enter to continue...")

with open('./problems.json', 'r+') as fichier:
    data = json.load(fichier)
    
    for row in data:
        driver.get(row['url'])
        time.sleep(5) 
        
        code_container = driver.find_element(By.CSS_SELECTOR, "div.ace_layer.ace_text-layer")
        code_lines = code_container.find_elements(By.CSS_SELECTOR, "div.ace_line")
        
        code = ""
        for line in code_lines:
            code += line.text + "\n"
        
        row['code'] = code.strip()

    
    fichier.seek(0)
    
    json.dump(data, fichier, indent=4)
    
    fichier.truncate()

driver.quit()
