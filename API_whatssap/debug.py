from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Importe a classe Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep
from random import choice,randint
import pickle
import pyperclip
from selenium.webdriver import ActionChains
#from trio import run, open_nursery, sleep

class WhatsAppAutomation:
    def __init__(self):
        options = webdriver.ChromeOptions()
        #options.add_experimental_option('useAutomationExtension',False)
        diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
        caminho_driver = os.path.join(diretorio_do_script, 'chromedriver')


        self.driver = webdriver.Chrome(executable_path=r"{}/chromedriver.exe".format(caminho_driver),options=options)
        self.caminhos_mp4 = []

    def abrir_whatsapp(self):
        self.driver.get("https://web.whatsapp.com")
        self.esperar_escaneamento_qr()

    def esperar_escaneamento_qr(self):
        input("Pressione Enter após escanear o código QR no WhatsApp Web...")

    def pressionar_tecla(self, tecla):
        action = webdriver.ActionChains(self.driver)
        action.send_keys(tecla)
        action.perform()

    def fechar_navegador(self):
        self.driver.quit()


    def salvar_cokies(self):
        cookies = self.driver.get_cookies()
        with open('cookies.pkl','wb') as cookie_file:
            pickle.dump(cookies,cookie_file)

        self.fechar_navegador()

    
    def upar_cokies(self):
        with open('cookies.pkl', 'rb') as cookie_file:
            self.cookies = pickle.load(cookie_file)

        self.driver.get('https://web.whatsapp.com')
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)




    def _pesquisa(self,pesquisa):

        elemento_pesquisa = '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p'
        _pesquisa = self.driver.find_element(By.XPATH,elemento_pesquisa)
        _pesquisa.click()
        _pesquisa.send_keys(pesquisa)

        self.driver.find_element(By.XPATH,elemento_pesquisa).send_keys(Keys.ENTER)

        sleep(randint(1,3))


    def enviar_mensagem(self,mensagem):
        sleep(2)
        elemento = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p'
        mensagem_ = self.driver.find_element(By.XPATH,elemento)
        mensagem_.click()
        #mensagem_.send_keys(mensagem)
        #sleep(randint(1,3))
        #mensagem_.send_keys(Keys.ENTER)

        pyperclip.copy(mensagem)
        act = ActionChains(self.driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        sleep(5)
        mensagem_.send_keys(Keys.ENTER)

    def pasta(self,path_img):
        self.caminhos_mp4 = []
        #_pasta_ = '/caminho/da/sua/pasta'  # Substitua pelo caminho da pasta que deseja verificar
        if not path_img == None:
            for root,dirs,files in os.walk(path_img):
                for file in files:
                    if file.endswith('.mp4') or file.endswith('.png') or file.endswith('.jpg'):
                        caminho_completo = os.path.join(root,file)
                        self.caminhos_mp4.append(caminho_completo)
        
    
    def upload_arquivo(self,arquivo,descricao):

        _up = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div'
        upl = self.driver.find_element(By.XPATH,_up).click()
        sleep(1.9)
        upload = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input'
        upl_1 = self.driver.find_element(By.XPATH,upload)
        upl_1.send_keys(r'{}'.format(arquivo))
        sleep(3.9)
        
        #photo = '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'
        #video = '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p'
        
        ultimos_d = arquivo[-4:]
        
        if ultimos_d == ".png" or ultimos_d == ".jpg":
            wait = WebDriverWait(self.driver,9)
            elements = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')))
            #element = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
            elements.click()
            elements.send_keys(descricao)
            sleep(3.9)

            enviar_ = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()

        elif ultimos_d == ".mp4":
            wait = WebDriverWait(self.driver,9)
            elements = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p')))
            #element = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
            elements.click()
            sleep(.5)
            elements.send_keys(descricao)
            sleep(3.9)

            enviar_ = self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()

        else:
            print('error 21 :')  

#'C:/Users/Lenovo/Desktop/No/API_whatssap/criativo.mp4'
#r"C:\Users\Lenovo\Desktop\No\API_whatssap\new.mp4"



    def start(self):
        print('hello word 22')

    # depurar a página na busca de elementos :(
    def Loc(self,elemento):
        elements = self.driver.find_element(By.XPATH,elemento)
        if elements:
            return f"Existe o elemento: {elements.text}"
        else:
            return f"Não existe o elemento: {elements.text}"


    def ele(self,elemento):
        return self.driver.find_element(By.XPATH,elemento).click()

    def a_click(self,loc,conteudo):
        return self.driver.find_element(By.XPATH,loc).send_keys(conteudo)


    def get(self,url):
        return self.driver.get(url)

    def msm_(self,elemento):
        msm = "💰 Entrada Confirmada"
        return self.driver.find_element(By.XPATH,elemento).send_keys(msm)



if __name__ == '__main__':

    whatsapp_bot = WhatsAppAutomation()
    whatsapp_bot.abrir_whatsapp()
    #whatsapp_bot.esperar_escaneamento_qr()

    # Exemplo de como pressionar a tecla 'Enter'
    #whatsapp_bot.pressionar_tecla(Keys.RETURN)

    #whatsapp_bot.fechar_navegador()
