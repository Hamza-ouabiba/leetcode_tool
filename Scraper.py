from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from util import Utils

class Scraper:
    def __init__(self):
        self.driver = None
        
    def write_code_solution(self):
        with open('./problems.json', 'r+') as fichier:
            data = json.load(fichier)
        
            for row in data:
                self.driver.get(row['url'])
                time.sleep(5) 
                
                code_container = self.driver.find_element(By.CSS_SELECTOR, "div.ace_layer.ace_text-layer")
                code_lines = code_container.find_elements(By.CSS_SELECTOR, "div.ace_line")
                
                code = ""
                for line in code_lines:
                    code += line.text + "\n"
                
                row['code'] = code.strip()
                
            fichier.seek(0)
    
            json.dump(data, fichier, indent=4)
    
            fichier.truncate()

    def extract_problems(self, data_row):
        helper = Utils()
        problems = []
        for data in data_row:
            problem_name = helper.ExtractProblemName(data['line'])
            if problem_name:
                problems.append({'problem': problem_name, 'state': 'Accepted', 'url': data['url']})
        return problems

    def get_problems(self, table_rows):
        data_row = []
        has_data = False
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
        return data_row, has_data

    def Authenticate(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://leetcode.com/accounts/login/")
        input("Please log in manually, then press Enter to continue...")
    
    def extract_data(self):
        if not self.driver:
            return None
        
        helper = Utils()
        c = 1
        problems = []
        with open('./problems.json', 'w') as fichier:
            while True:
                self.driver.get(f"https://leetcode.com/submissions/#/{c}")

                time.sleep(5)

                table_rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

                if not table_rows:
                    print("No more rows found at page:", c)
                    break

                data_row, has_data = self.get_problems(table_rows)

                if has_data:
                    print(f"Data found on page {c}:")
                    problems.extend(self.extract_problems(data_row))  # Changed to extend list
                
                else:
                    print(f"No data at page {c}")
                    break
                
                c += 1
        
            json.dump(problems, fichier, indent=4)

        # After writing on file, remove duplicates
        helper.remove_duplicates_from_json('./problems.json')
        # Getting code solutions from submissions : 
        self.write_code_solution()
        # Then create directories for each problem
        helper.create_folders('./problems.json')

        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    scraper = Scraper()
    scraper.Authenticate()
    scraper.extract_data()
