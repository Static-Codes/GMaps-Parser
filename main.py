import ctypes
import warnings
import time
import asyncio

from utilities.QueryLoader import QueryLoader
from utilities.BackupManager import BackupManager
from utilities.BrowserManager import BrowserManager
from utilities.LinkExtractor import LinkExtractor
from utilities.FileWriter import FileWriter
from utilities.BrowserLauncher import BrowserLauncher
from utilities.DataExtractor import DataExtractor
from utilities.CSVWriter import CSVWriter
from utilities.LinkLoader import LinkLoader

# Part 1: Extracting Links Using Selenium
ctypes.windll.kernel32.SetConsoleTitleW("Google Maps Parser")
warnings.filterwarnings('ignore')

print("[INFO] Backing up last session..")
BackupManager.backup_old_links_files()

print("[INFO] Starting extractor, this may take a couple seconds.")
driver = BrowserManager.initialize_browser() 

queries = QueryLoader.load_queries()
extracted_links = LinkExtractor.extract_links_from_queries(driver, queries)

if not extracted_links:
    print("[INFO] No links were extracted, please check your terminal for any errors, then try again.")
    exit()

print(f"[INFO] Found {len(extracted_links)} links.")

if FileWriter.write_links_to_file("google_maps_links.txt", extracted_links):
    print("[INFO] Please wait 5 seconds, while the parser starts.")
    time.sleep(5)
    print("[INFO] Parser loaded!")
    driver.quit()

else:
    print("[INFO] Failed to write links to file.")
    print("[INFO] Writing to `linksBackup/links_backup.txt`") 
    print("[INFO] Please copy this file elsewhere or it will be overwritten in the next session!")

    if not FileWriter.write_links_to_file("linksBackup/links_backup.txt", extracted_links):    
        print("[INFO] Failed to write links to backup file, exiting....")
        exit()
    
    print("[INFO] Links written to backup, exiting...")
    exit()

# Part 2: Parsing Extracted Links Using Pyppeteer
ctypes.windll.kernel32.SetConsoleTitleW("Google Maps Link Parser")
warnings.filterwarnings('ignore')

async def main(urls):
    browser, page = await BrowserLauncher.initialize_browser()
    business_data = []

    for url in urls:
        data = await DataExtractor.extract_data(page, url)
        business_data.extend(data)

    await browser.close()
    print("Finished")

    CSVWriter.write_to_csv(business_data)

links_file = "google_maps_links.txt"
urls = LinkLoader.load_links(links_file)

if not urls:
    print("No URLs loaded, exiting...")
    exit()

print(f'{len(urls)} URLs loaded!')
print(f'Estimated parsing time: {len(urls)*2} seconds.')

try:
    asyncio.get_event_loop().run_until_complete(main(urls))
except Exception as e:
    print(f"Error during processing: {e}")
