from UIbootstrap import *
from windia_manager import *
#from local_db import localDataManager

def main():
    doctors_list_path = "PflegedienstAutomatisierung/AutomatisierungRene/doctors.txt"
    insurance_list_path = "PflegedienstAutomatisierung/AutomatisierungRene/both_insurances.txt"
    base_ln_path = "PflegedienstAutomatisierung/AutomatisierungRene/LN.docx"
    W = WindiaManager()
    #dm = localDataManager(doctors_list_path,insurance_list_path)
    #UI = UImanager(W,dm.get_doctors(), dm.get_insurances() ,base_ln_path)
    UI = UImanager(W,"", "" ,base_ln_path)
    UI.start()

if __name__ == "__main__":
    main()

