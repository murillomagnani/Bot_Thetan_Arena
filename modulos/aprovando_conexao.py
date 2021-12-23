from configuracoes import *
from modulos.instalando_metamask import driver

def aprovando():
    time.sleep(2)
    pg.click(1841, 562)
    time.sleep(2)
    pg.click(1841, 562)
    time.sleep(3)
    pg.scroll(-300)
    time.sleep(2)
    pg.click(1841, 562)
    time.sleep(2)
    pg.click(1841, 562)
    time.sleep(5)
    pg.click(1841, 562)
    time.sleep(3)
    driver.get(marketplace)
    time.sleep(2)
    
    return None