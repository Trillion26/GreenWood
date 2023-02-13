from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )

def persist_data(data, filename):
    # this function writes data in the file
    try:
        file = open(filename, "a")
        file.writelines([f"{line}\n" for line in data])
    except Exception as e:
        return e
    finally:
        file.close()
    return True