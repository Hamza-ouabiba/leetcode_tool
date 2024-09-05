from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from util import Utils

class Scraper:
    def __init__(self,file_path):
        self.driver = None
        self.file_path = file_path
        self.helper = Utils(file_path)

    def write_code_solution(self):
        with open('./problems.json', 'r+') as fichier:
            data = json.load(fichier)
            treated_num = 0
            for row in data:
                problem_num = self.helper.get_number_of_problems()
                self.helper.display_progress_bar(problem_number=problem_num,problem_treated_num=treated_num)
                self.driver.get(row['url'])
                time.sleep(5) 
                
                code_container = self.driver.find_element(By.CSS_SELECTOR, "div.ace_layer.ace_text-layer")
                code_lines = code_container.find_elements(By.CSS_SELECTOR, "div.ace_line")
                
                code = ""
                for line in code_lines:
                    code += line.text + "\n"
                
                row['code'] = code.strip()
                treated_num += 1
            fichier.seek(0)
    
            json.dump(data, fichier, indent=4)
    
            fichier.truncate()

    def extract_problems(self, data_row):
        problems = []
        for data in data_row:
            problem_name = self.helper.ExtractProblemName(data['line'])
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
        
        page_counter = 1
        problems = []
        with open('./problems.json', 'w') as fichier:
            while True:
                self.driver.get(f"https://leetcode.com/submissions/#/{page_counter}")

                time.sleep(5)

                table_rows = self.driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

                if not table_rows:
                    print("No more rows found at page:", page_counter)
                    break

                data_row, has_data = self.get_problems(table_rows)

                if has_data:
                    print(f"Data found on page {page_counter}:")
                    problems.extend(self.extract_problems(data_row))  
                
                else:
                    print(f"No data at page {page_counter}")
                    break
                
                page_counter += 1
        
            json.dump(problems, fichier, indent=4)

        # After writing on file, remove duplicates
        self.helper.remove_duplicates_from_json()
        # Getting code solutions from submissions : 
        self.write_code_solution()
        # Then create directories for each problem
        self.helper.create_folders()

        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    scraper = Scraper('./problems.json')
    scraper.Authenticate()
    scraper.extract_data()
