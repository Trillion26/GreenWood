from concurrent.futures import ProcessPoolExecutor, wait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from scraper.scraper import get_driver, persist_data

class ScrapeQuotes:
    def __init__ (self, url):
        self.url = url
        self.driver = get_driver()

    def load_page(self):
        self.driver.get(self.url)

    def scrape_quotes(self):
        quotes_list = []
        quotes = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "quote"))
        )
        for quote in quotes:
            quotes_list.append(self.clean_output(quote))
        self.close_driver()
        return quotes_list

    def clean_output(self, quote):
        raw_quote = quote.text.strip().split("\n")
        raw_quote[0] = raw_quote[0].replace("", '"')
        raw_quote[0] = raw_quote[0].replace("", '"')
        raw_quote[1] = raw_quote[1].replace("by", "")
        raw_quote[1] = raw_quote[1].replace("(about)", "")
        raw_quote[2] = raw_quote[2].replace("Tags: ", "")
        return ",".join(raw_quote)

    def close_driver(self):
        self.driver.close()

def main(tag):
    scrape = ScrapeQuotes("https://quotes.toscrape.com/tag/" + tag)
    scrape.load_page()
    quotes = scrape.scrape_quotes()
    persist_data(quotes, "quotes.csv")

if __name__ == " __main__":
    
    print("Loading")
    
    tags = ["love", "truth", "books", "life", "inspirational"]

    # list to store the processes
    processList = []

    # initialize the mutiprocess interface
    with ProcessPoolExecutor() as executor:
        for tag in tags:
            processList.append(executor.submit(main, tag))

    # wait for all the threads to complete
    wait(processList)