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
        with open(file_path, 'r') as file:
            data = json.load(file)

        if isinstance(data, list):
            seen_problems = set()
            unique_data = []

            for item in data:
                problem = item.get('problem')
                if problem not in seen_problems:
                    seen_problems.add(problem)
                    unique_data.append(item)
            
            data = unique_data
        else:
            print("Unsupported JSON format. The data must be a list of dictionaries.")
            return

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
                
                if not os.path.exists(problem_path):
                    os.makedirs(problem_path)
                
                file_path = os.path.join(problem_path, 'int.cpp')
                with open(file_path, 'w') as file:
                    file.write(row['code'])
                
                print(f"Created folder and file for problem: {problem_name}")
            except Exception as e:
                print(f"Error: {e}")

util = Utils()

# # Call the ExtractProblemName method
# problem_name = util.ExtractProblemName("1 year, 5 months ago Merge Two Sorted Lists Accepted 8 ms cpp")
# print("Extracted Problem Name:", problem_name)

#util.create_folders('./problems.json')
