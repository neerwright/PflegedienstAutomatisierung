
import codecs

class localDataManager():
    doctors = []
    insurances = {}
    doc_path = ""
    insurance_path = ""
    
    def __init__(self, doc_path, insurance_path):
        self.doc_path = doc_path
        self.insurance_path = insurance_path
        
        with codecs.open(doc_path, "r", "utf-8") as f:
            for doc in f:
                self.doctors.append(doc.replace("\r", "").replace("\n", ""))
                
        with codecs.open(insurance_path, "r", "utf-8") as f:
            for insurance_line in f:
                k_p_insurance = insurance_line.split(", ")
                self.insurances[k_p_insurance[0].replace("\r", "").replace("\n", "")] = k_p_insurance[1].replace("\r", "").replace("\n", "")
            
            
            
    def get_doctors(self):
        return self.doctors
    
    def get_insurances(self):
        return self.insurances
    
    def print_insurances(self):
        for k , p in self.insurances.items():
            print ("K: " + str(k))
            
            print ("P: " + str(p))
            print("-------------------")
        
    def add_doctor(self, surname, name):
        with codecs.open(self.doc_path , "a", "utf-8") as f:
            doc = f"{surname}, {name}"
            self.doctors.append(doc)
            f.write("\n" + str(doc))
            
        
    
