from csvparser import *
from Utilities import *


def HancurkanCandi (data_candi) :
    
    id = int(input("Masukkan ID candi : "))
    for i in range (my_length(data_candi)):
        
        if data_candi[i][0]!=None and int(data_candi[i][0]) == id :
            jawab = str(input("Apakah anda yakin ingin menghancurkan candi ID(Y/N): "))

            if jawab == 'Y' or jawab == 'y' :
                data_candi = my_dellArray(data_candi, data_candi[i])
                return data_candi
                
     print("Tidak ada candi dengan  ID tersebut.")
     return data_candi
    

#HancurkanCandi()
#print(data_candi)
