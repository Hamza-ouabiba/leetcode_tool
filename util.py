import json
import os
class Utils:
    def ExtractProblemName(self, text):
        if not text:
            return None
        
        text_splitted = str(text).split(' ')
        
        if 'ago' in text_splitted:
            ago_index = text_splitted.index('ago')
            new_one = text_splitted[ago_index+1:]
            
            if 'Accepted' in new_one:
                accepted_index = new_one.index('Accepted')
                problem_name = ' '.join(new_one[:accepted_index])
                return problem_name
        
        return None
    def remove_duplicates_from_json(self, file_path):
        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Check if data is a list of dictionaries
        if isinstance(data, list):
            seen_problems = set()
            unique_data = []

            for item in data:
                # Assuming each item is a dictionary with a 'problem' key
                problem = item.get('problem')
                if problem not in seen_problems:
                    seen_problems.add(problem)
                    unique_data.append(item)
            
            data = unique_data
        else:
            print("Unsupported JSON format. The data must be a list of dictionaries.")
            return

        # Write the cleaned data back to the JSON file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


    def create_folders(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)

        base_path = "./problemset"

        if not os.path.exists(base_path):
            os.makedirs(base_path)

        for row in data:
            try:
                problem_name = row['problem']
                problem_path = os.path.join(base_path, problem_name)
                
                # Create the problem directory if it does not exist
                if not os.path.exists(problem_path):
                    os.makedirs(problem_path)
                
                # Create the file within the directory
                file_path = os.path.join(problem_path, 'int.cpp')
                with open(file_path, 'w') as file:
                    # You can write initial content to the file here if needed
                    file.write(row['code'])
                
                print(f"Created folder and file for problem: {problem_name}")
            except Exception as e:
                print(f"Error: {e}")
    def extract_from_json_code(self,file_path):
         with open(file_path, 'r') as file:
            data = json.load(file)

# Create an instance of Utils
util = Utils()

# # Call the ExtractProblemName method
# problem_name = util.ExtractProblemName("1 year, 5 months ago Merge Two Sorted Lists Accepted 8 ms cpp")
# print("Extracted Problem Name:", problem_name)

util.create_folders('./problems.json')
