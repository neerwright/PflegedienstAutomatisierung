from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class findDocSelenium():
    driver = None
    
    def __init__(self):
        service = Service()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)


    def search_doc(self, name, city):
        self.driver.get("https://www.arzt-auskunft.de/")
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
        
        
    def find_doc_on_search_results_page(self, name : str, surname : str, city : str):
        url = f"https://www.arzt-auskunft.de/arzt-auskunft/suche_sn/index.js?a=DL&Ft={name}+{surname}&Ft_e=&Ftg={city}&Ftg_e="
        self.driver.get(url)
        time.sleep(2)
        doc = None
        doc_name = ""
        try:
            doc = self.driver.find_element(By.CLASS_NAME, "btn-ergebnisliste-detail")
            doc_name = doc.get_attribute('innerHTML')
        except:
            pass
        print(doc_name)
        if surname in doc_name and name in doc_name:
            doc.click()
        else:
            return False
        
    def get_doc_data(self):
        street = ""
        try:
            street =  self.driver.find_element(By.XPATH("//span[@itemprop='streetAddress']"))
            #"span[itemprop='streetAddress']"
        except:
            pass
        # https://www.arzt-auskunft.de/arzt/neurologie-psychiatrie-und-psychotherapie/herrenberg/dr-heiko-huber-4987487
#<span itemprop="streetAddress">Bahnhofstraße 2/3</span>
        #zip_code =  self.driver.find_element(By.CSS_SELECTOR("[span='postalCode']")).get_attribute('innerHTML')
        #city =  self.driver.find_element(By.CSS_SELECTOR("[span='addressLocality']")).get_attribute('innerHTML')
        #tel =  self.driver.find_element(By.CSS_SELECTOR("[span='telephone']")).get_attribute('innerHTML')
        #speciality =  self.driver.find_element(By.CSS_SELECTOR("[span='medicalSpeciality']")).get_attribute('innerHTML')
        print(street)
        #print(zip_code)
        #print(city)
        #print(tel)
        #print(speciality)
        #return street, zip_code, city, tel, speciality
        
       
s = findDocSelenium()
s.find_doc_on_search_results_page("Huber", "Heiko", "Herrenberg")
time.sleep(5)
s.get_doc_data()
time.sleep(30)