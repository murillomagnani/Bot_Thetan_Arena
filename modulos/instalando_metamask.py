from selenium import webdriver

def instalando():
    CRX = './metamask.crx'
    PATH = './chromedriver.exe'
    global driver
    driver = webdriver.Chrome(PATH)
    
    opt = webdriver.ChromeOptions()
    opt.add_extension(CRX)
    driver = webdriver.Chrome(chrome_options=opt)
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
    driver.maximize_window()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    return None