import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def scroll():
    for _ in range(10):
        driver.execute_script('window.scrollBy(0, 200)')
        time.sleep(0.1)


def mainpage(driver, url):
    driver.get(url)
    scroll()
    mainpage_html = BeautifulSoup(driver.page_source, "html.parser")

    content = mainpage_html.find("div", {"class": "eventCalendar__eventStickers"})
    for i in range(-1, -9, -1):
        content = content.findChildren(recursive=False)[i].find("div")
        print(content)
        content = mainpage_html.find("div", {"class": "eventCalendar__eventStickers"})



if __name__ == "__main__":
    driver = webdriver.Chrome()
    mainpage(driver, 'https://sport.acgnn.ru/eventCalendar')
    driver.quit()