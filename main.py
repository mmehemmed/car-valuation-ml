from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time
import csv

fieldnames = [
    "price",
    "category",
    "year",
    "make",
    "mileage",
    "model",
    "fuel_type",
    "transmission",
    "engine_volume"
]



def scrape_car_details(url,browser):
    car_data = {}

    page.set_default_timeout(15000)
    
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=15000)

        catfish_element = page.query_selector("#catfish")
        car_data["price"] = catfish_element.get_attribute("data-price") #Always in AZN
        car_data["category"] = catfish_element.get_attribute("data-category-name")
        car_data["year"] = catfish_element.get_attribute("data-year")
        car_data["make"] = catfish_element.get_attribute("data-make")
        car_data["mileage"] = catfish_element.get_attribute("data-mileage")
        car_data["model"] = catfish_element.get_attribute("data-model")
        car_data["fuel_type"] = catfish_element.get_attribute("data-fuel-type")
        car_data["transmission"] =  catfish_element.get_attribute("data-transmission")
        car_data["engine_volume"] =  catfish_element.get_attribute("data-engine-volume")
    except PlaywrightTimeoutError:
        print(f"[TIMEOUT] Page took too long to load: {url}")
    except Exception as e:
        print(f"[ERROR] Could not scrape {url}: {e}")

    
    return car_data

def writeToCSV(car_data,percent):
    if car_data and "price" in car_data:
        with open("data.csv", mode="a", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(car_data)
        print("Saved car.  Completion: " + percent)
    else:
        print("Skipped empty car.")


def getLinks():
    with open("links.txt", mode="r") as txt_file:
        return txt_file.readlines()


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    links = getLinks()
    for i in range(len(links)):
        time.sleep(2)
        writeToCSV(scrape_car_details(links[i],browser),f"{i/len(links)*100:.2f}")
        
    browser.close()
    