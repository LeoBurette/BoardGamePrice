from typing import Any
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

HEADER = {'User-Agent': 'Mozilla/5.0',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'fr-FR,en;q=0.8',
       'Connection': 'keep-alive'}

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class WebClientSingleton(metaclass=SingletonMeta):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-logging'])
        options.add_argument('--headless')
        options.add_argument('--log-level=1')
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Remote("http://selenium:4444", options=options)    
        
    def getDriver(self):
        return self.driver


def generateAgent(url):
    req = Request(url)
    req.headers = HEADER
    return req

def generateWebClient():
    return WebClientSingleton().getDriver()

def getHtml(url):
    return urlopen(generateAgent(url))

def getClientRenderHtml(url):
    driver = generateWebClient()
    driver.get(url)

    sleep(1)

    elm = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    return elm