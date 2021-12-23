from configuracoes import *
from modulos.instalando_metamask import driver


def logando():
    btn_get_start = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".first-time-flow__button")))
    btn_get_start.click()

    btn_import_wallet = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".first-time-flow__button")))
    btn_import_wallet.click()

    btn_no_thanks = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-container__footer-button")))
    btn_no_thanks.click()

    input_login_metamask = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input")))
    input_login_metamask[0].send_keys(wallet)
    input_login_metamask[1].send_keys(password)
    input_login_metamask[2].send_keys(password)
    input1 = driver.find_elements(By.CSS_SELECTOR,'.first-time-flow__checkbox')
    input1[1].click()

    btn_import = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".first-time-flow__button")))
    btn_import.click()

    time.sleep(5)

    btn_all_done = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".first-time-flow__button")))
    btn_all_done.click()

    return None