from UIbootstrap import *
from windia_manager import *
from local_db import localDataManager

def main():
    doctors_list_path = "AutomatisierungRene/doctors.txt"
    insurance_list_path = "AutomatisierungRene/both_insurances.txt"
    base_ln_path = "C:/Users/Verwaltung/Documents/Leistungsnachweise E, V, SGB V - Feb. 25.docx"
    
    dm = localDataManager(doctors_list_path,insurance_list_path)
    W = WindiaManager(dm)
    UI = UImanager(W,dm.get_doctors(), dm.get_insurances() ,base_ln_path)
    UI.start()

if __name__ == "__main__":
    main()

