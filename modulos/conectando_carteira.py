from configuracoes import *
from modulos.instalando_metamask import driver

def conectando():
    driver.get(marketplace)

    btn_connect_wallet = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button._adUdUfWOz0RV3mCy5UZ:nth-child(2)")))
    btn_connect_wallet.click()

    btn_login_metamask = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".YRKFKFASV5vdfcZd0Akn")))
    btn_login_metamask.click()

    btn_switch_bsc = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Qb4y4J21KHxkP_FGgZ1P")))
    btn_switch_bsc.click()

    return None