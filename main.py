from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from util import Utils

def extractData():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    driver.get("https://leetcode.com/accounts/login/")

    input("Please log in manually, then press Enter to continue...")

    c = 1
    problems = []
    helper = Utils()

    with open('./problems.json', 'w') as fichier:
        while True:
            driver.get(f"https://leetcode.com/submissions/#/{c}")

            time.sleep(5)

            table_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

            if not table_rows:
                print("No more rows found at page:", c)
                break

            has_data = False
            data_row = []

            for row in table_rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                
                for cell in cells:
                    if 'Accepted' in cell.text:
                        link = cell.find_element(By.TAG_NAME, 'a')
                        if link:
                            url = link.get_attribute('href')
                            data_row.append({'line': row.text, 'url': url})
                        has_data = True
                        break 
            
            if has_data:
                print(f"Data found on page {c}:")
                for data in data_row:
                    problem_name = helper.ExtractProblemName(data['line'])
                    if problem_name:
                        problems.append({'problem': problem_name, 'state': 'Accepted', 'url': data['url']})
            else:
                print(f"No data at page {c}")
                break
            
            c += 1
        
        json.dump(problems, fichier, indent=4)

    driver.quit()
