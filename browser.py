from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def choose_browser():
    driver = None
    print("Choose a browser to use:")
    print("1. Chrome")
    print("2. Firefox")
    print("3. Edge")
    print("4. Safari")
    
    choice = input("Enter the number of the browser: ")
    
    if choice == '1':
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")  # Suppress Chrome logs
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Suppress DevTools logs
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
    elif choice == '2':
        firefox_options = FirefoxOptions()
        firefox_options.log.level = "fatal"  # Suppress Firefox logs
        driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
    elif choice == '3':
        edge_options = EdgeOptions()
        edge_options.add_argument("--log-level=3")  # Suppress Edge logs
        driver = webdriver.Edge(service=EdgeService(), options=edge_options)
    elif choice == '4':
        driver = webdriver.Safari()
    else:
        print("Invalid choice, using Chrome as default.")
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
    return driver