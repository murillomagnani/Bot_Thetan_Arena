from configuracoes import *
from modulos.instalando_metamask import driver

def analise():
    lista_preco = str(driver.find_element(By.XPATH, "//span[@class='pGXts7bo6MhenRsouqyL']").text)
    lista_preco = lista_preco.replace('$', ' ')
    lista_preco = lista_preco.replace('USD', ' ')
    lista_preco = lista_preco.strip()
    lista_preco = float(lista_preco)

    qtd_gthc = str(driver.find_element(By.XPATH, "//span[@class='SQAkeqBaSU7tF1QYwm_p ByNAVfKFfGGzSd4JevUt']").text)
    qtd_gthc = qtd_gthc.replace('/', '')
    qtd_gthc = int(qtd_gthc)


    while True:
        if lista_preco <= valor_max and qtd_gthc <= gthc_max:
            btn_price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='pGXts7bo6MhenRsouqyL']")))
            btn_price.click()

            btn_buy = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='_adUdUfWOz0RV3mCy5UZ _Y9VNwyMSaCzDxM4CKiu']")))
            btn_buy.click()

            btn_checkout = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='j3_hmGlmJ95C9BOcyOFv lY43WCC5Ek_dhmKjb_Cw']")))
            btn_checkout.click()

            time.sleep(2.5)
            pg.scroll(-400)
            time.sleep(1)
            pg.click(1841, 562)

        else:
            time.sleep(1.8)
            driver.refresh()