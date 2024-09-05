from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from util import Utils

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to the LeetCode login page
driver.get("https://leetcode.com/accounts/login/")

input("Please log in manually, then press Enter to continue...")

# Open the JSON file to read and write
with open('./problems.json', 'r+') as fichier:
    data = json.load(fichier)
    
    # Iterate over each problem in the data
    for row in data:
        driver.get(row['url'])
        time.sleep(5)  # Allow time for the page to load
        
        # Locate the code container
        code_container = driver.find_element(By.CSS_SELECTOR, "div.ace_layer.ace_text-layer")
        code_lines = code_container.find_elements(By.CSS_SELECTOR, "div.ace_line")
        
        code = ""
        for line in code_lines:
            # Extract the text from each line
            code += line.text + "\n"
        
        # Add the extracted code to the row
        row['code'] = code.strip()

    
    # Move the file pointer to the beginning before writing
    fichier.seek(0)
    
    # Write back the updated data to the file
    json.dump(data, fichier, indent=4)
    
    # Truncate the file to remove any leftover content
    fichier.truncate()

# Close the WebDriver
driver.quit()
