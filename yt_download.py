import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv 
import os

def convert_download(url):
    driver.get("https://ytmp3.cc/en9/")
    url_input = driver.find_element_by_id('input')
    url_input.send_keys(url)
    convert_button = driver.find_element_by_id('submit')
    convert_button.click()
    time.sleep(1.5)
    download_button = driver.find_elements_by_link_text('Download')
    print (len(download_button))
    download_button = download_button[0]
    download_button.click()
    time.sleep(2)

parser = argparse.ArgumentParser()
parser.add_argument('--url',dest=url,help="Enter url from youtube to be Downloaded")
parser.add_argument('--bin-location',help="Path for the .exe file of chrome",default=r"C:\Program Files\Google\Chrome\Application\chrome.exe")
parser.add_argument()
args = parser.parse_args()
chromedriver = r"{}\chromedriver.exe".format(os.path.dirname(os.path.realpath(__file__)))
downloads_path = r"{}\downloads".format(os.path.dirname(os.path.realpath(__file__)))

if not os.path.exists(downloads_path):
    os.mkdir(downloads_path)

options = webdriver.ChromeOptions() 
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument(r"download.default_directory={}".format(downloads_path))
driver = webdriver.Chrome(options=options, executable_path=chromedriver, )
with open('urls.csv',newline='') as csv_file:
    reader = csv.reader(csv_file)
    for url in reader:
        convert_download(url)
        print(f"Succesfully downloaded {url}!")
driver.quit()