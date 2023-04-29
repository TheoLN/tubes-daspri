from csvparser import *
from Utilities import *


def HancurkanCandi (data_candi) :
    
    id = int(input("Masukkan ID candi : "))
    count = 0
    data_candi_temp = [[None for i in range (5)] for j in range(101)]
    for i in range (0,100):
        if data_candi[i][0]!=None and int(data_candi[i][0]) == id :
            jawab = str(input("Apakah anda yakin ingin menghancurkan candi ID(Y/N): "))
            count = 1
            if jawab == 'Y' or jawab == 'y' :
                data_candi = my_dellArray(data_candi, data_candi[i])
                break
    if count == 0 :
        print("Tidak ada candi dengan  ID tersebut.")
        return data_candi
    

#HancurkanCandi()
#print(data_candi)
