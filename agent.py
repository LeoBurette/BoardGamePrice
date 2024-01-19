from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HEADER = {'User-Agent': 'Mozilla/5.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def generateAgent(url):
    req = Request(url)
    req.headers = HEADER
    return req

def getHtml(url):
    return urlopen(generateAgent(url))

def getClientRenderHtml(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    options.add_argument('--headless')
    options.add_argument('--log-level=1')
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    elm = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    driver.close()
    return elm