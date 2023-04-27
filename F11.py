from csvparser import *
from Utilities import *
from main2 import *

def HancurkanCandi () :
    global data_candi
    id = int(input("Masukkan ID candi : "))
    count = 0
    data_candi_temp = [[None for i in range (5)] for j in range(101)]
    for i in range (1,101):
        if data_candi[i][0]!=None and int(data_candi[i][0]) == id :
            jawab = str(input("Apakah anda yakin ingin menghancurkan candi ID: "))
            count = 1
            if jawab == 'Y' or jawab == 'y' :
                data_candi[i][0] = None
                data_candi[i][1] = None
                data_candi[i][2] = None
                data_candi[i][3] = None
                data_candi[i][4] = None
                break
    if count == 0 :
        print("Tidak ada candi dengan  ID tersebut.")
        return
    j = 0
    
    for i in range(101) :
        if data_candi[i][0] != None  :
            data_candi_temp[j][0] = data_candi[i][0]
            data_candi_temp[j][1] = data_candi[i][1]
            data_candi_temp[j][2] = data_candi[i][2]
            data_candi_temp[j][3] = data_candi[i][3]
            data_candi_temp[j][4] = data_candi[i][4]
            j += 1

    for i in range(101):
        data_candi[i][0] = data_candi_temp[i][0]
        data_candi[i][1] = data_candi_temp[i][1]
        data_candi[i][2] = data_candi_temp[i][2]
        data_candi[i][3] = data_candi_temp[i][3]
        data_candi[i][4] = data_candi_temp[i][4]

HancurkanCandi()
print(data_candi)
