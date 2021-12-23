import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

marketplace = 'https://marketplace.thetanarena.com/?sort=PriceAsc'

wallet = 'your metamask wallet here'
password = 'your password here'

valor_max = 0.025
gthc_max = 150000