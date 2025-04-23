from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_hotels_trivago(destination):
    # Path to the ChromeDriver executable
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

    # Open Trivago homepage
    driver.get('https://www.trivago.com')

    # Wait for the page to load completely
    time.sleep(5)

    # Find the search bar and input the destination city
    search_bar = driver.find_element(By.CLASS_NAME, 'css-1ti2bzh')  # Inspect and adjust this based on Trivago's actual class name
    search_bar.send_keys(destination)
    search_bar.send_keys(Keys.RETURN)  # Press Enter to start the search

    # Wait for the search results to load
    time.sleep(5)

    # Scrape the hotel names (adjust the class name based on inspection)
    hotels = driver.find_elements(By.CLASS_NAME, 'item_name')  # Modify based on actual inspection of the page

    # Print the first 5 hotels
    for hotel in hotels[:5]:
        print(hotel.text.strip())  # Clean and print hotel name

    # Close the driver after scraping
    driver.quit()

# Test the function with Mumbai as an example (Change city as needed)
scrape_hotels_trivago("Mumbai")
