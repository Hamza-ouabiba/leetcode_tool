from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from util import Utils

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to the LeetCode login page
driver.get("https://leetcode.com/accounts/login/")

# Wait for manual login
input("Please log in manually, then press Enter to continue...")

# Initialize variables
c = 1
problems = []
helper = Utils()

# Open JSON file to write data
with open('./problems.json', 'w') as fichier:
    while True:
        # Navigate to the submissions page
        driver.get(f"https://leetcode.com/submissions/#/{c}")

        # Wait for the page to load
        time.sleep(5)

        # Find all table rows
        table_rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

        # Check if rows are found
        if not table_rows:
            print("No more rows found at page:", c)
            break

        # Initialize flag and data container
        has_data = False
        data_row = []

        for row in table_rows:
            # Find all cells in the row
            cells = row.find_elements(By.TAG_NAME, "td")
            
            for cell in cells:
                if 'Accepted' in cell.text:
                    # Find link if it exists
                    link = cell.find_element(By.TAG_NAME, 'a')
                    if link:
                        url = link.get_attribute('href')
                        data_row.append({'line': row.text, 'url': url})
                    has_data = True
                    break  # Exit the cell loop once 'Accepted' is found
        
        if has_data:
            print(f"Data found on page {c}:")
            for data in data_row:
                problem_name = helper.ExtractProblemName(data['line'])
                if problem_name:
                    problems.append({'problem': problem_name, 'state': 'Accepted', 'url': data['url']})
        else:
            print(f"No data at page {c}")
            break
        
        # Move to the next page
        c += 1
    
    # Write data to JSON file
    json.dump(problems, fichier, indent=4)

# Close the WebDriver
driver.quit()
