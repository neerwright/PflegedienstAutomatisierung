from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class findDocSelenium():
    driver = None
    service = None
    surname = ""
    name = ""


    def __init__(self):
        self.service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=options)


    def search_doc(self, name, city):
        self.driver.get("https://www.arzt-auskunft.de/")
        time.sleep(2)
        
        self.driver.find_element(By.ID, "cookiescript_accept").click()
        time.sleep(2)

        try:
            self.driver.find_element(By.NAME, "Ft").send_keys(name)
        except:
            pass
        try:
            self.driver.find_element(By.NAME, "Ftg").send_keys(city)
        except:
            pass
        
        self.driver.find_element(By.ID, "ergebnisseButton").click()
        
        
    def find_doc_on_search_results_page(self, name : str , city : str):
        url = f"https://www.arzt-auskunft.de/arzt-auskunft/suche_sn/index.js?a=DL&Ft={name}&Ft_e=&Ftg={city}&Ftg_e="
        #https://www.arzt-auskunft.de/arzt-auskunft/suche_sn/index.js?a=DL&Ft=Huber&Ft_e=&Ftg=Herrenberg&Ftg_e=
        self.driver.get(url)
        time.sleep(2)
        self.driver.find_element(By.ID, "cookiescript_accept").click()

        doc = None
        doc_name = ""
        try:
            doc = self.driver.find_element(By.CLASS_NAME, "btn-ergebnisliste-detail")
            doc_name = doc.get_attribute('innerHTML')
            self.get_name(doc_name)
        except:
            pass
        print(doc_name)
        
        doc.click()
        
    def get_name(self, text):
        text =  text.replace("Frau", "").replace("Herr", "").replace("Prof.", "").replace("Dr.", "").replace("med.", "").replace("Dipl.-Psych.", "").replace("dent", "")
        text = ' '.join(text.split())
        print(text.split(" "))
        text = text.split(" ")
        self.name = text[0]
        self.surname = text[1]
        
    def get_doc_data(self):
        time.sleep(2)
        #self.driver.get("https://www.arzt-auskunft.de/arzt/anaesthesiologie-allgemeinmedizin/herrenberg/dr-florian-weiss-7450301")
        # time.sleep(3)
        #self.driver.find_element(By.ID, "cookiescript_accept").click()
        #time.sleep(2)
        
        street =  self.driver.find_element(By.XPATH,("//div[@itemprop='address']/span[@itemprop='streetAddress']")).text
        #print("element: " + str(street))
        #print("inner" + street.get_attribute('innerHTML'))
        #print("txt: " + street.text)
            #"span[itemprop='streetAddress']"
        
        # https://www.arzt-auskunft.de/arzt/neurologie-psychiatrie-und-psychotherapie/herrenberg/dr-heiko-huber-4987487
            #<span itemprop="streetAddress">Bahnhofstraße 2/3</span>
        zip_code =  self.driver.find_element(By.XPATH, ("//div[@itemprop='address']/span[@itemprop='postalCode']")).text
        city =  self.driver.find_element(By.XPATH, ("//div[@itemprop='address']/span[@itemprop='addressLocality']")).text
        tel =  self.driver.find_element(By.XPATH, ("//span[@itemprop='telephone']/a[1]")).text
        #speciality =  self.driver.find_element(By.XPATH, ("//h2[@class='fs-5']/span[@itemprop='medicalSpeciality']")).text
        print(street)
        print(zip_code)
        print(city)
        print(tel)
        #print(speciality)
        return street, zip_code, city, tel#, speciality
        
       
#s = findDocSelenium()
#s.get_name("Herr Dr. med. Heiko Huber")
#s.find_doc_on_search_results_page("Huber", "Heiko", "Herrenberg")
#time.sleep(5)
#s.get_doc_data()
#time.sleep(300000)