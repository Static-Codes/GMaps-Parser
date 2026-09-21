from utilities.BrowserScripts import parseBusinessLinksScript
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class LinkExtractor:
    @staticmethod
    def extract_links_from_queries(driver, queries):
        extracted_links = []

        for query in queries:
            print(f"\n[INFO] Entering Query Provided: '{query}'")
            driver.get("https://www.google.com/maps/place/")

            searchbox = driver.find_element(By.ID, "ucc-1")
            
            if not searchbox:
                print("[ERROR]: Unable to find the searchbox element.")
                continue

            searchbox.send_keys(query)
            time.sleep(0.08)
            searchbox.send_keys(Keys.ENTER)

            print("[INFO] Submitted, Waiting For Results, Please Wait 5 Seconds.")

            time.sleep(5)

            print("[INFO] Finding Scroll Wheel Element")
            xpath_element = '//div[contains(@aria-label, "Results for")]'
            fBody = driver.find_element(By.XPATH, xpath_element)

            scroll = 0

            if fBody:
                print("[INFO] Scroll wheel element found, scrolling through results.")
            else:
                print(
                    "[INFO] Error finding scroll wheel element, please check lines 23-24 in LinkExtractor.py"
                )

            while scroll < 20:
                try:
                    fBody.send_keys(Keys.PAGE_DOWN)
                    scroll += 1
                    time.sleep(1)
                except Exception as e:
                    print(f"[INFO] Scroll wheel element raised an error: {e}")

            print("[INFO] Scrolling finished, extracting links.")
            links = driver.execute_script(parseBusinessLinksScript)

            if links:
                extracted_links.extend(links)
                print(f"\n[INFO] {len(links)} links extracted for query: '{query}'\n")

            else:
                print(f"[INFO] Failed to extract links for query: '{query}'\n")
        return extracted_links
